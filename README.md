# electoral_model_2020
A simple electoral model test for the 2020 U.S. presidential election.

Made using the polling data from fivethirtyeight. Gives a rough comparison of likelihood of winning between different states and an estimation of what the vote totals will be, but not actual numeric chances of winning.

The most relevant and useful part of this model is the tipping point state ranks - by taking into account the comparative chances of each candidate winning each state as well as the electoral votes of each state, I found which states are most likely to be the tipping point state that causes a candidate to win and thus which states are the most important in the election - not all votes are worth the same!

There's also some work around which demographics' votes are most influential in deciding the presidential election but as expected the largest demographics by population are also the most influential. I may update this to normalize by size of the population in the U.S. at some point in order to get something more useful.

Created this in May 2020 and made just a few changes since then in order to fix some broken things rather than alter what the model says - I wear any mistaken predictions proudly.

| state                | votes | Biden | Trump | lean\_score | result       | cumulative\_votes | tipping\_rank |
| -------------------- | ----- | ----- | ----- | ----------- | ------------ | ----------------- | ------------- |
| West Virginia        | 5     | 32.11 | 66.69 | \-15.74     | safe trump   | 5                 | 49            |
| Oklahoma             | 7     | 36.39 | 62.63 | \-13.24     | safe trump   | 12                | 48            |
| Wyoming              | 3     | 32.42 | 65.90 | \-12.47     | safe trump   | 15                | 46            |
| South Dakota         | 3     | 37.75 | 60.41 | \-7.99      | safe trump   | 18                | 44            |
| Arkansas             | 6     | 39.33 | 59.16 | \-7.88      | safe trump   | 24                | 42            |
| Kentucky             | 8     | 40.37 | 58.06 | \-6.89      | safe trump   | 32                | 40            |
| North Dakota         | 3     | 39.68 | 58.49 | \-6.66      | safe trump   | 35                | 38            |
| Mississippi          | 6     | 39.69 | 58.25 | \-6.08      | safe trump   | 41                | 37            |
| Alabama              | 9     | 38.17 | 59.29 | \-5.96      | safe trump   | 50                | 34            |
| Idaho                | 4     | 40.07 | 57.80 | \-5.66      | safe trump   | 54                | 33            |
| Louisiana            | 8     | 37.99 | 59.06 | \-5.34      | safe trump   | 62                | 32            |
| Alaska               | 3     | 44.84 | 53.60 | \-3.42      | safe trump   | 65                | 31            |
| Utah                 | 6     | 43.28 | 54.45 | \-3.41      | safe trump   | 71                | 30            |
| Nebraska             | 5     | 44.39 | 53.70 | \-3.19      | safe trump   | 76                | 29            |
| Tennessee            | 11    | 45.09 | 53.28 | \-3.12      | safe trump   | 87                | 28            |
| Kansas               | 6     | 44.34 | 53.49 | \-2.89      | safe trump   | 93                | 27            |
| Indiana              | 11    | 43.96 | 53.66 | \-2.87      | safe trump   | 104               | 25            |
| Missouri             | 10    | 44.01 | 53.47 | \-2.69      | safe trump   | 114               | 24            |
| South Carolina       | 9     | 43.42 | 53.44 | \-2.42      | safe trump   | 123               | 23            |
| Montana              | 3     | 45.82 | 51.29 | \-1.41      | likely trump | 126               | 22            |
| Ohio                 | 18    | 47.51 | 50.06 | \-0.74      | lean trump   | 144               | 19            |
| Texas                | 38    | 48.37 | 49.27 | \-0.27      | toss-up      | 182               | 15            |
| Iowa                 | 6     | 48.88 | 49.13 | \-0.08      | toss-up      | 188               | 14            |
| Florida              | 29    | 49.15 | 48.28 | 0.24        | toss-up      | 217               | 9             |
| Nevada               | 6     | 49.70 | 48.11 | 0.50        | toss-up      | 223               | 8             |
| Georgia              | 16    | 50.70 | 46.95 | 1.12        | likely biden | 239               | 4             |
| North Carolina       | 15    | 51.08 | 46.83 | 1.37        | likely biden | 254               | 2             |
| Pennsylvania         | 20    | 51.59 | 45.92 | 1.63        | likely biden | 274               | 1             |
| Michigan             | 16    | 52.13 | 45.00 | 1.84        | likely biden | 290               | 3             |
| Arizona              | 11    | 51.95 | 45.78 | 1.89        | likely biden | 301               | 5             |
| Maine                | 4     | 54.58 | 41.63 | 2.71        | safe biden   | 305               | 6             |
| Wisconsin            | 10    | 54.07 | 43.48 | 3.07        | safe biden   | 315               | 7             |
| Minnesota            | 10    | 54.95 | 42.03 | 3.21        | safe biden   | 325               | 10            |
| New Hampshire        | 4     | 53.99 | 44.34 | 3.61        | safe biden   | 329               | 11            |
| New Mexico           | 5     | 55.24 | 42.77 | 4.17        | safe biden   | 334               | 12            |
| Virginia             | 13    | 56.61 | 40.62 | 4.23        | safe biden   | 347               | 13            |
| Illinois             | 20    | 57.84 | 39.52 | 5.03        | safe biden   | 367               | 16            |
| Colorado             | 9     | 56.52 | 41.65 | 5.25        | safe biden   | 376               | 17            |
| New Jersey           | 14    | 59.32 | 37.71 | 5.45        | safe biden   | 390               | 18            |
| Oregon               | 7     | 59.25 | 38.84 | 7.02        | safe biden   | 397               | 20            |
| Washington           | 12    | 61.78 | 35.51 | 7.09        | safe biden   | 409               | 21            |
| New York             | 29    | 62.86 | 34.24 | 7.33        | safe biden   | 438               | 26            |
| California           | 55    | 61.97 | 35.66 | 7.80        | safe biden   | 493               | 35            |
| Hawaii               | 4     | 65.24 | 31.72 | 8.30        | safe biden   | 497               | 36            |
| Connecticut          | 7     | 61.01 | 37.17 | 8.47        | safe biden   | 504               | 39            |
| Delaware             | 3     | 61.07 | 37.24 | 8.84        | safe biden   | 507               | 41            |
| Maryland             | 10    | 66.34 | 30.67 | 8.94        | safe biden   | 517               | 43            |
| Rhode Island         | 4     | 62.99 | 35.03 | 9.39        | safe biden   | 521               | 45            |
| Vermont              | 3     | 69.31 | 27.67 | 10.35       | safe biden   | 524               | 47            |
| Massachusetts        | 11    | 68.52 | 28.88 | 11.01       | safe biden   | 535               | 50            |
| District of Columbia | 3     | 91.84 | 6.49  | 31.98       | safe biden   | 538               | 51            |
