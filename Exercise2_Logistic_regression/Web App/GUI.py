# PART 1: Imports, load and test of the model

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

lm = load("logmodel.joblib")

# tester_row = {
#     'age': 25,
#     'job': 2,
#     'marital': 1,
#     'education': 2,
#     'failed_previous_credit': 1,
#     'balance': 5000,
#     'housing_loan': 0,
#     'loan': 0,
#     'contact_type': 1,
#     'day': 5,
#     'month': 2,
#     'contact_duration_sec': 120,
#     'number_of_contacts': 1,
#     'days_since_last_contact': -1,
#     'previous_number_of_contacts': 0,
#     'poutcome': 3,
# }
#
# # create a pandas DataFrame and scale the values
# tester_row = pd.DataFrame([tester_row])
#
# print("All probabilities by category:")
# print(lm.predict_proba(tester_row))
# print()
#
# # change these based on your original data
# labels = ["No", "Yes"]
#
# print("Does this customer take a deposit (Yes/No):")
# result = labels[logmodel.predict(tester_row)[0]]
# print(result)
# print("-------------------")

# PART 2: THE GUI
# create a window
customtkinter.set_appearance_mode("dark")
root = customtkinter.CTk()
root.geometry("700x400")

# PART 2.1: setting the background image
# open the image
image = PIL.Image.open("bg_image.png")
background_image = customtkinter.CTkImage(image, size=(1200, 900))

# Define a function to resize the background image
def resize_image(event=None):
    new_width = root.winfo_width()
    new_height = root.winfo_height()
    # if you have issues with ANTIALIAS
    # you need Pillow==9.5.0 version
    resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(resized_image)
    bg_lbl.configure(image=photo)
    bg_lbl.image = photo  # Keep a reference to avoid garbage collection

# Create a background label with the initial image
bg_lbl = customtkinter.CTkLabel(root, text="", width=700, height=400)
bg_lbl.place(x=0, y=0)

# Call the resize_image function when the window is resized
root.bind("<Configure>", resize_image)

# Initialize the image size
resize_image()

# PART 2.2: adding text about the goal of this GUI
# place text label
# the main text
text_label = tk.Label(root, text="Let's check whether a customer takes deposit \n Please, fill in data below",
                      font=("Helvetica", 22), fg="white", bg="black")  # Set background to transparent
text_label.place(relx=0.5, rely=0.1, anchor="center")

# PART 2.3: question "How old is the client?"
# Create a new frame `age_form` to contain the Label and Entry widgets
age_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
age_form.place(relx=0.5, rely=0.25, anchor="center")

# Create the Label and Entry widgets for the first question
lbl_age = tk.Label(master=age_form, text="How old is the client?")
ent_age = tk.Entry(master=age_form)
lbl_age.grid(row=0, column=0, sticky="e")
ent_age.grid(row=0, column=1)

# Bind the <Return> event to the ent_age Entry widget
ent_age.bind("<Return>", lambda event: print("Age entered:", ent_age.get()))

# PART 2.3: Choose a client's marital status
# marital_label_text = tk.Label(root, text="Choose marital status", font=("Helvetica", 16), fg="white", bg="black")
# marital_label_text.place(relx=0.35, rely=0.35, anchor="center")

marital_status = customtkinter.StringVar(value="divorced")  # set initial value

# button to choose - combobox
def marital_status_callback(choice):
    print("Marital status choice:", choice)

marital_combobox = customtkinter.CTkOptionMenu(master=root,
                                       fg_color=("black"),
                                       bg_color=("black"),
                                       values=["divorced", "married", "single", "unknown"],
                                       command=marital_status_callback,
                                       variable=marital_status)

marital_combobox.place(relx=0.35, rely=0.35, anchor="center")

# PART 2.4:Choose a client's education
# edu_label_text = tk.Label(root, text="Choose education level", font=("Helvetica", 16), fg="white", bg="black")
# edu_label_text.place(relx=0.65, rely=0.35, anchor="center")
education = customtkinter.StringVar(value="primary")  # set initial value

# button to choose - combobox
def education_callback(choice):
    print("Education choice:", choice)

education_combobox = customtkinter.CTkOptionMenu(master=root,
                                       fg_color=("black"),
                                       bg_color=("black"),
                                       values=["primary", "secondary", "tertiary", "unknown"],
                                       command=education_callback,
                                       variable=education)

education_combobox.place(relx=0.65, rely=0.35, anchor="center")

# PART 2.4: Click "yes", if the client has deposit default
def default_checkbox_event():
    print("checkbox toggled, current value:", default_check_var.get())

default_check_var = customtkinter.StringVar(value="on")
default_checkbox = customtkinter.CTkCheckBox(root, text="Client has deposit default", command=default_checkbox_event,
                                     variable=default_check_var, onvalue="on", offvalue="off")

default_checkbox.place(relx=0.35, rely=0.45, anchor="center")

# PART 2.5: Click "yes", if the client has housing loan
def housing_checkbox_event():
    print("checkbox toggled, current value:", housing_check_var.get())

housing_check_var = customtkinter.StringVar(value="on")
housing_checkbox = customtkinter.CTkCheckBox(root, text="Client has housing loan", command=housing_checkbox_event,
                                     variable=housing_check_var, onvalue="on", offvalue="off")

housing_checkbox.place(relx=0.65, rely=0.45, anchor="center")

# PART 2.6: Question "What is the client's balance?"
# Create a new frame `age_form` to contain the Label and Entry widgets
balance_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
balance_form.place(relx=0.5, rely=0.55, anchor="center")

# Create the Label and Entry widgets for the first question
lbl_balance = tk.Label(master=balance_form, text="What is the client's balance?")
ent_balance = tk.Entry(master=balance_form)
lbl_balance.grid(row=0, column=0, sticky="e")
ent_balance.grid(row=0, column=1)

# Bind the <Return> event to the ent_age Entry widget
ent_balance.bind("<Return>", lambda event: print("Age entered:", ent_age.get()))

# PART 2.7: Question "Does the client's have a personal loan?"
def personal_loan_checkbox_event():
    print("checkbox toggled, current value:", personal_loan_check_var.get())

personal_loan_check_var = customtkinter.StringVar(value="on")
personal_loan_checkbox = customtkinter.CTkCheckBox(root, text="Client has housing loan", command=personal_loan_checkbox_event,
                                     variable=personal_loan_check_var, onvalue="on", offvalue="off")

personal_loan_checkbox.place(relx=0.35, rely=0.65, anchor="center")

# Function for collecting user responses and making predictions
def set_text_by_button():
    # Collect user data
    age = int(ent_age.get())
    marital_status = marital_status.get()
    education = education.get()
    # Other client characteristics to collect...

    # Create a DataFrame with user responses
    user_data = {
        'age': [age],
        'marital': [marital_status],
        'education': [education],
        # Other client characteristics...
    }
    user_df = pd.DataFrame(user_data)

    # Predict using logistic regression
    prediction = lm.predict(user_df)

    # Display the prediction result
    if prediction == 1:
        result_var.set("This client will take a deposit.")
    else:
        result_var.set("This client will not take a deposit.")

# Define and configure the button to initiate prediction
set_up_button = tkinter.Button(root, height=1, width=16, text="Check the client", command=set_text_by_button)
set_up_button.pack(side="bottom", pady=20)

# Start the main event loop
root.mainloop()