About the project:

Linear Regression
Originally, I had a dataset containing top IMDB movies updated till December 15, 2023. This file is in CSV format and contains 11 columns, namely: Movie Name, Rating, Votes, Meta Score, Genre, PG Rating, Year, Duration, Cast, Director. The data has 1950 rows.

My linear regression model aims to answer the question: What factors contribute the most to a movie gaining more votes and fans?

Link to the original dataset: https://www.kaggle.com/datasets/kianindeed/imdb-movie-dataset-dec-2023

Steps in the notebook:
1. Cleaning and modifying data
2. Checking the balance of the data
3. The train/test –split
4. Training the Linear Regression model
5. Error and performance metrics
6. Creating a tester row for metrics
7. Emphasizing variables that should affect the prediction greatly

Web Scraping
I performed web scraping, but I did not merge datasets because movies in the new dataset are very recent, resulting in a lack of scores and many "N/a" values in rows. If I were to merge these two datasets, I would need to clean all NaN values, potentially resulting in a very small new dataset.