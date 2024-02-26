# PART

import tkinter
import pandas as pd
from joblib import load

lm = load("Movie_rating_model.pkl")

# PART 2: quickly test if the model file works correctly

# this code is copy-pasted from the linear regression code

# this is our separate test data candidate

# let's try with some new imaginary data
# let's try with some new imaginary data
tester_row = {
    'Votes': 20000,
    'Meta Score': 54.0,
    'Year': 2020,
    'Duration': 117,
    'Action': 1, 'Adventure': 1, 'Animation': 1, 'Biography': 0, 'Comedy': 0, 'Crime': 0, 'Documentary': 0,
    'Drama': 0, 'Family': 0, 'Fantasy': 0, 'History': 0, 'Horror': 0, 'Music': 0, 'Musical': 0,
    'Mystery': 0, 'Romance': 0, 'Sci-Fi': 0, 'Sport': 0, 'Thriller': 0, 'War': 0, 'Western': 0,

    'PG Rating_13+': 1, 'PG Rating_16+': 0, 'PG Rating_18+': 0, 'PG Rating_Approved': 0,
    'PG Rating_G': 0, 'PG Rating_GP': 0, 'PG Rating_NC-17': 0, 'PG Rating_PG': 0,
    'PG Rating_PG-13': 0, 'PG Rating_Passed': 0, 'PG Rating_R': 0, 'PG Rating_TV-14': 0,
    'PG Rating_TV-G': 0, 'PG Rating_TV-MA': 0, 'PG Rating_TV-PG': 0,
    'PG Rating_TV-Y7': 0
}

# convert to pandas-format
tester_row = pd.DataFrame([tester_row])

# use our model to predict our tester_row data
result = lm.predict(tester_row)[0]

print()
print(f"Predicted rating for this movie: {round(float(result), 2)}")