# -*- coding: utf-8 -*-
import pandas as pd
import datetime

def duo_questions(df):
    if len(df) == 2:
        return df

def basic_weights(df):
    date_now = min(datetime.datetime(2020, 11, 3), datetime.datetime.now())
    days_out = (date_now - df['end_date']).dt.days
    election_out = ((datetime.datetime(2020, 11, 3)) - df['end_date']).dt.days
    df['effect'] = (df['sample_size'] / ((1 + days_out) * election_out))
    return df

def state_results(df):
    candidate_df = df.groupby('answer')
    return candidate_df.apply(candidate_results)
    
def candidate_results(df):
    normalizer = 1 / df['effect'].sum()
    df['norm_effect'] = df['effect'] * normalizer
    df['norm_result'] = df['pct'] * df['norm_effect']
    return df['norm_result'].sum()

def demos_state_pct(df):
    sex_sums = df.loc[df['SEX']!=0].groupby('SEX')['POPESTIMATE2018'].sum()
    origin_sums = df.loc[df['ORIGIN']!=0].groupby('ORIGIN')['POPESTIMATE2018'].sum()
    race_sums = df.groupby('RACE')['POPESTIMATE2018'].sum()
    df['generation'] = pd.cut(df['AGE'], [15, 21, 37, 53, 72, 86], labels = ['gen_z', 'millenials', 'gen_x', 'boomers', 'silent'])
    generation_sums = df.groupby('generation')['POPESTIMATE2018'].sum()
    sex_sums = sex_sums / sex_sums.sum()
    origin_sums = origin_sums / origin_sums.sum()
    race_sums = race_sums / race_sums.sum()
    generation_sums = generation_sums / generation_sums.sum()
    sex_sums.index = ['male', 'female']
    origin_sums.index = ['not_hispanic', 'hispanic']
    race_sums.index = ['white', 'black', 'native', 'asian', 'pacific']
    sums_df = pd.concat([sex_sums, origin_sums, race_sums, generation_sums])
    return sums_df

polls = pd.read_csv('president_polls_historical.csv')
electoral_votes = pd.read_csv('electoral_votes.csv')
statesnotin = pd.read_csv('statesnotin.csv')
demos = pd.read_csv('sc-est2018-alldata5.csv')
generations = pd.read_csv('age_generations.csv')
polls = polls.loc[((polls['answer'] == 'Biden') | (polls['answer'] == 'Trump'))]
question_group = polls.groupby('question_id')
polls = question_group.apply(duo_questions)
polls.dropna(how='all', inplace=True)
polls['end_date'] = pd.to_datetime(polls['end_date'])
polls = basic_weights(polls)
polls.loc[polls['state'].str.contains('Maine').fillna(False), 'state'] = 'Maine'
polls.loc[polls['state'].str.contains('Nebraska').fillna(False), 'state'] = 'Nebraska'
state_polls = polls.groupby('state')
state_avgs = state_polls.apply(state_results)
state_avgs['diff'] = state_avgs['Biden'] - state_avgs['Trump']
state_avgs['undecided'] = 100 - (state_avgs['Biden'] + state_avgs['Trump'])
state_avgs['lean_score'] = state_avgs['diff'] / (1 + state_avgs['undecided'])
state_avgs['limit_lean_score'] = state_avgs['lean_score']
state_avgs['limit_lean_score'] = state_avgs['limit_lean_score'].where(
    state_avgs['limit_lean_score'] <= 50, 50).where(
        state_avgs['limit_lean_score'] >= -50, -50)
state_avgs = electoral_votes.merge(state_avgs, how='left', left_on='state', right_index=True)
chosen_statesnotin = statesnotin.loc[statesnotin['state'].isin(state_avgs.loc[state_avgs['limit_lean_score'].isna(),'state'].values)]
state_avgs.dropna(inplace=True)
state_avgs = pd.concat([state_avgs, chosen_statesnotin], ignore_index=True)
state_avgs['est_biden'] = (1 + state_avgs['limit_lean_score']) * state_avgs['votes'] / 2
state_avgs['est_trump'] = (1 - state_avgs['limit_lean_score']) * state_avgs['votes'] / 2
state_avgs['pct_biden'] = (state_avgs['limit_lean_score'] / 2) + 0.5
state_avgs['pct_trump'] = 1 - ((state_avgs['limit_lean_score'] / 2) + 0.5)
biden_votes = state_avgs['est_biden'].sum()
trump_votes = state_avgs['est_trump'].sum()
state_avgs['result'] = pd.cut(state_avgs['limit_lean_score'], [-50, -1.99, -0.99, -0.5, 0.5, 0.99, 1.99, 50], labels = ['safe trump', 'likely trump', 'lean trump', 'toss-up', 'lean biden', 'likely biden', 'safe biden'])
state_avgs = state_avgs.sort_values('limit_lean_score', ignore_index = True)
count = 0
vote_list = []
for vote in state_avgs['votes']:
    count += vote
    vote_list.append(count)
state_avgs['cumulative_votes'] = pd.Series(vote_list)
state_avgs['trump_votes_away'] = state_avgs['cumulative_votes'] - 269
state_avgs['votes_away_magnitude'] = state_avgs['trump_votes_away'].abs()
state_avgs['importance'] = state_avgs['votes'] / state_avgs['votes_away_magnitude']
sorted_mag = state_avgs['votes_away_magnitude'].sort_values()
state_avgs['tipping_rank'] = pd.Series(range(1,52), index=sorted_mag.index)
state_avgs['importance_2'] = state_avgs['votes'] / state_avgs['tipping_rank']

demos_state = demos.groupby('NAME')
demos_breakdown = demos_state.apply(demos_state_pct)
demos_df = state_avgs.loc[state_avgs['limit_lean_score'].abs() != 1].merge(demos_breakdown, left_on = 'state', right_index=True)
demos_importance = demos_df.loc[:,'male':].multiply(demos_df['importance'], axis='index').sum()
demos_importance_2 = demos_df.loc[:,'male':].multiply(demos_df['importance_2'], axis='index').sum()
overall_importance = demos_df.loc[:,'male':].sum()
demos_importance = demos_importance / demos_importance.max()
demos_importance_2 = demos_importance_2 / demos_importance_2.max()
overall_importance = overall_importance / overall_importance.max()
