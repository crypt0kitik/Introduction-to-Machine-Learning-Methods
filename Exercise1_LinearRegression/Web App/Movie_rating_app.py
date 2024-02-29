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

################

# PART 3: development of the web application

# import moduls
import tkinter as tk
import tkinter.ttk as ttk
import os
import random
from tkinter import *
from PIL import ImageTk, Image



# create window
root = tk.Tk()
root.title("Movie rating")
root.geometry("1200x900")
#root.configure(bg="black")

# A widget used to display text on the screen
#text = tk.Label(
   # text="Imagine that you want to make a famous movie \n but beforehand you want to see whether this movie will be famous",
    #foreground="white",  # Set the text color to white
   # font= ('Aerial', 17)
    #background="black",  # Set the background color to black
    #width = 10,
    #height = 10
#)
#text.pack()


# Load images for frames
image_paths = ["image1.png", "image2.png", "image3.png"]
photos = [None] * len(image_paths)

# loop all images
for i, image_path in enumerate(image_paths):
    image = Image.open(image_path)
    # Resize the image to fit the dimensions of the corresponding frame
    if i == 0:
        image = image.resize((200, 100), Image.ANTIALIAS)
    elif i == 1:
        image = image.resize((100, 100), Image.ANTIALIAS)
    elif i == 2:
        image = image.resize((50, 100), Image.ANTIALIAS)
    photos[i] = ImageTk.PhotoImage(image)

# Create frames with image backgrounds
frames = []
for i, photo in enumerate(photos):
    frame = tk.Frame(master=root, width=(i+1)*50+150, height=100)
    frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    background_label = tk.Label(frame, image=photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    frames.append(frame)

def change_images():
    global photos
    for i, frame in enumerate(frames):
        new_photo_index = (i + 1) % len(image_paths)
        new_photo = photos[new_photo_index]
        frame_background_label = frame.winfo_children()[0]  # Get the background label of the frame
        frame_background_label.configure(image=new_photo)
        frame_background_label.image = new_photo  # Keep a reference to avoid garbage collection
    root.after(2000, change_images)

root.after(2000, change_images)  # Start changing images after 2 seconds

##########################


# to run the Tkinter event loop. This method
# listens for events, such as button clicks or keypresses,
# and blocks any code that comes after it from running
# until you close the window where you called the method.
root.mainloop()
