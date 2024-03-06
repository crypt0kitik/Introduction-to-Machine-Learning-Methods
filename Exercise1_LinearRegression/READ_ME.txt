About the Linear Regression project

--> Originally I had a dataset that contained top IMDB movies updated till 15 Dec 2023. This file in the csv fromat and it contains 11 columns namely: Moive Name, Rating, Votes, Meta Score, Genre, PG Rating, Year, Duration, Cast, Director. The data has 1950 row

--> The Linear regression model answers for the question: what affects more to make a movie to gain more votes and fans?

--> Link for the original dataset: https://www.kaggle.com/datasets/kianindeed/imdb-movie-dataset-dec-2023 

--> Steps in the notebook:
1. Cleaning and modifying data
2. Checking the balance of the data
3. The train/test –split
4. Training the Linear Regression model
5. Error and performance metrics
6. Creating a tester row for metrics

--> Web scrapping
I made web srapping but i did not merge datasets because movies in a new datatset are very new that is why we lack a lot of scores and it results in N/a in many rows. If I had to merge these 2 datasets i would need to clean all Nan values and it could result in a very small new dataset.
