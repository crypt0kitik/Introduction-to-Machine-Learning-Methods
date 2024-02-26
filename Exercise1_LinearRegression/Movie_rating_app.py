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

# create window
window = tk.Tk()
window.title("Movie rating")
window.geometry("1200x900")
window.configure(bg="black")

# Function to update the positions of the pictures
def update_positions():
    # Update the position of each picture
    for label in picture_labels:
        x = random.randint(0, window_width - picture_width)
        y = random.randint(0, window_height - picture_height)
        label.place(x=x, y=y)

    # Schedule the next update
    window.after(2000, update_positions)  # Update positions every 2 seconds

# Load images and get their dimensions
image_files = ["image1.png", "image2.png", "image3.png"]  # List of image files
pictures = [tk.PhotoImage(file=file) for file in image_files]
picture_width = pictures[0].width()
picture_height = pictures[0].height()

# Create a list to store the Label widgets for pictures
picture_labels = []

# Create and place Label widgets for each picture
for picture in pictures:
    label = tk.Label(root, image=picture)
    label.place(x=random.randint(0, window_width - picture_width),
                y=random.randint(0, window_height - picture_height))
    picture_labels.append(label)

# Schedule the initial update
root.after(2000, update_positions)  # Update positions every 2 seconds






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
window.mainloop()