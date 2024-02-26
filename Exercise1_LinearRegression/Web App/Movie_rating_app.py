# PART 1: needed imports and load the model

import tkinter
import pandas as pd
from joblib import load

lm = load("Movie_rating_model.pkl")

# PART 2: quickly test if the model file works correctly
# let's try with some new imaginary data
#tester_row = {
#    'Votes': 20000,
#    'Meta Score': 54.0,
#    'Year': 2020,
#    'Duration': 117,
#    'Action': 1, 'Adventure': 1, 'Animation': 1, 'Biography': 0, 'Comedy': 0, 'Crime': 0, 'Documentary': 0,
#    'Drama': 0, 'Family': 0, 'Fantasy': 0, 'History': 0, 'Horror': 0, 'Music': 0, 'Musical': 0,
#    'Mystery': 0, 'Romance': 0, 'Sci-Fi': 0, 'Sport': 0, 'Thriller': 0, 'War': 0, 'Western': 0,

#   'PG Rating_13+': 1, 'PG Rating_16+': 0, 'PG Rating_18+': 0, 'PG Rating_Approved': 0,
#    'PG Rating_G': 0, 'PG Rating_GP': 0, 'PG Rating_NC-17': 0, 'PG Rating_PG': 0,
#    'PG Rating_PG-13': 0, 'PG Rating_Passed': 0, 'PG Rating_R': 0, 'PG Rating_TV-14': 0,
#    'PG Rating_TV-G': 0, 'PG Rating_TV-MA': 0, 'PG Rating_TV-PG': 0,
#   'PG Rating_TV-Y7': 0
#}

# convert to pandas-format
#tester_row = pd.DataFrame([tester_row])

# use our model to predict our tester_row data
#result = lm.predict(tester_row)[0]

#print(f"Predicted rating for this movie: {round(float(result), 2)}")

# the model works correctly!

# PART 3: development of the web application

# import moduls
import tkinter as tk
import tkinter.ttk as ttk
import os
import random

# create window
root = tk.Tk()
root.title("Movie rating")
#root.geometry("1200x900")
#root.configure(bg="black")

############################

# Load images and get their dimensions
# Assuming the images are in the same directory as your script
script_dir = os.path.dirname(os.path.realpath(__file__))
image_files = [os.path.join(script_dir, "image1.png"), os.path.join(script_dir, "image2.png")]

# Define a Canvas widget
canvas = canvas(win, width=600, height=400, bg="white")
canvas.pack(pady=20)

# Add Images to Canvas widget
image = ImageTk.PhotoImage(Image.open('favicon.ico'))
img = canvas.create_image(250, 120, anchor=NW, image=image)

def left(e):
   x = -20
   y = 0
   canvas.move(img, x, y)

def right(e):
   x = 20
   y = 0
   canvas.move(img, x, y)

def up(e):
   x = 0
   y = -20
   canvas.move(img, x, y)

def down(e):
   x = 0
   y = 20
   canvas.move(img, x, y)

# Bind the move function
win.bind("<Left>", left)
win.bind("<Right>", right)
win.bind("<Up>", up)
win.bind("<Down>", down)










##########################

# A widget used to display text on the screen
text = tk.Label(
    text="Imagine that you want to make a famous movie \n but beforehand you want to see whether this movie will be famous",
    foreground="white",  # Set the text color to white
    font= ('Aerial', 17)
    #background="black",  # Set the background color to black
    #width = 10,
    #height = 10
)
text.pack()

entry = tk.Entry(fg="yellow", bg="white", width=50)
entry.pack()

# to run the Tkinter event loop. This method
# listens for events, such as button clicks or keypresses,
# and blocks any code that comes after it from running
# until you close the window where you called the method.
root.mainloop()