# ------------ PART 1 ------------

# PART 1: Imports, load and test of the model
# 1.1 imports

# in terminal
# pip install joblib
# pip install pandas
# pip install customtkinter
# brew install python-tk (for macOS)
# pip install Pillow
# pip install scikit-learn



# import libraries
from joblib import load
import pandas as pd
from tkinter import *
import customtkinter
import customtkinter, tkinter
import tkinter as tk
import PIL
from PIL import Image
from PIL import ImageTk

# 1.2 load and test of the model
lm = load("model.joblib")

tester_row = {
    'title': "Helsinki",
    'text': "cow cat dog true er of his party’s leadership",
}

# the variable is created to hold these
# input elements separately
# becuase the tester row is a dictionary
text_documents = [tester_row['title'], tester_row['text']]

# preprocess the text data in the 'title' and 'text' columns
# using TF-IDF vectorization
tfidf_vectorizer = TfidfVectorizer()
# fit the vectorizer on the training data
tfidf_vectorizer.fit(x_train)
# transform the test data
vectorized_documents = tfidf_vectorizer.transform(text_documents)

# make predictions using the trained model
predicted_probabilities = model.predict_proba(vectorized_documents)

# display the predicted probabilities for each class
print("Predicted Probabilities by Category:")
print(predicted_probabilities)

# define a dictionary to map class labels to their interpretations
label_interpretation = {
    1: "It is a fake news",
    0: "It is a true news"
}

# determine the predicted label based on the highest probability
predicted_label_index = np.argmax(predicted_probabilities)
predicted_label = label_interpretation[predicted_label_index]
print("\nResults:", predicted_label)