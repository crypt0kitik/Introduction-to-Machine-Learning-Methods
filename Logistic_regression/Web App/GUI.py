# ------------ PART 1 ------------

# PART 1: Imports, load and test of the model
# 1.1 imports

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

# ------------ PART 2 ------------

# PART 2: THE GUI
# create a window
customtkinter.set_appearance_mode("dark")
root = customtkinter.CTk()
root.geometry("700x400")


# PART 2.1: setting the background image
# I had a background image but it was too heavy for the app
# that is why now the whole code for this section is in comments

# open the image
# image = PIL.Image.open("bg_image.png")
# background_image = customtkinter.CTkImage(image, size=(1200, 900))

# Define a function to resize the background image
# def resize_image(event=None):
  #  new_width = root.winfo_width()
  #  new_height = root.winfo_height()
    # if you have issues with ANTIALIAS
    # you need Pillow==9.5.0 version
  #  resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
  #  photo = ImageTk.PhotoImage(resized_image)
  #  bg_lbl.configure(image=photo)
  #  bg_lbl.image = photo  # Keep a reference to avoid garbage collection

# Create a background label with the initial image
# bg_lbl = customtkinter.CTkLabel(root, text="", width=700, height=400)
# bg_lbl.place(x=0, y=0)

# Call the resize_image function when the window is resized
# root.bind("<Configure>", resize_image)

# Initialize the image size
# resize_image()

# PART 2.2: adding text about the goal of this GUI
# place the main text label
text_label = tk.Label(root, text="Let's check whether a customer takes deposit \n Please, fill in data below",
                      font=("Helvetica", 16), fg="black", bg="yellow")  # Set background to transparent
text_label.place(relx=0.5, rely=0.1, anchor="center")

# PART 2.3: question "How old is the client?"
# Create a new frame `age_form` to contain the Label and Entry widgets
age_form = tk.Frame(relief=tk.SUNKEN, borderwidth=2)
# Place the age_form frame in the window
age_form.place(relx=0.18, rely=0.25, anchor="center")

# Create the Label widget for asking the age question
lbl_age = tk.Label(master=age_form, text="How old is the client?")
# Create the Entry widget for entering the age
ent_age = tk.Entry(master=age_form, width=5)
# Position the label and entry widgets inside the frame using grid layout
lbl_age.grid(row=0, column=0, sticky="e")
ent_age.grid(row=0, column=1)

# Function to handle when Enter key is pressed
def handle_enter(event):
    age_value = ent_age.get()  # Get the value entered
    if not age_value:  # If the value is empty
        age_value = 0  # Set default value to 0
    else:
        try:
            age_value = int(age_value)  # Try converting to integer
        except ValueError:
            print("Error: Please enter a valid age (numeric value).")
            return  # Exit the function if value is not a number
    print("Age entered:", age_value)

# Bind the <Return> event to the ent_age Entry widget
ent_age.bind("<Return>", handle_enter)

# PART 2.4: Choose a client's marital status
# Dictionary mapping marital status strings to numeric values
marital_status_dict = {"divorced": 1, "married": 2, "single": 3}

# Set the initial value of marital status
marital_status = customtkinter.StringVar(value="divorced")

# Initializing a variable
numeric_marital_status = 0

# Callback function for when marital status is selected
def marital_status_callback(selected_status):
    # Retrieve the numeric value of the selected marital status from the dictionary
    numeric_marital_status = marital_status_dict[selected_status]
    # Print the numeric marital status
    print("Numeric marital status:", numeric_marital_status)

# Create a dropdown menu for selecting marital status
marital_combobox = customtkinter.CTkOptionMenu(master=root,
                                               fg_color=("black"),
                                               bg_color=("black"),
                                               values=["divorced", "married", "single"],
                                               command=marital_status_callback,
                                               variable=marital_status)

# Place the marital status dropdown menu on the window
marital_combobox.place(relx=0.44, rely=0.25, anchor="center")


# PART 2.5:Choose a client's education
# Dictionary to map words to numeric values for education levels
education_dict = {"primary": 1, "secondary": 2, "tertiary": 3, "unknown": 4}

# Set initial value for education level
education = customtkinter.StringVar(value="primary")

# Initializing a variable
numeric_education = 0
# Callback function for when an education level is selected
def education_callback(choice):
    # Retrieve the numeric value of the selected education level from the dictionary
    numeric_education = education_dict[choice]
    # Print the numeric education level
    print("Numeric education choice:", numeric_education)

# Create the education combobox
education_combobox = customtkinter.CTkOptionMenu(master=root,
                                                 fg_color=("black"),
                                                 bg_color=("black"),
                                                 values=["primary", "secondary", "tertiary", "unknown"],
                                                 command=education_callback,
                                                 variable=education)

# Place the education combobox on the window
education_combobox.place(relx=0.65, rely=0.25, anchor="center")

# PART 2.5: Choose a client's job
# Dictionary to map job titles to numeric values
job_dict = {"admin": 0, "blue-collar": 1, "entrepreneur": 2, "housemaid": 3, "management": 4,
            "retired": 5, "self-employed": 6, "services": 7, "student": 8, "technician": 9,
            "unemployed": 10, "unknown": 11}

# Set initial value for job
job = customtkinter.StringVar(value="entrepreneur")

# Initializing a variable
numeric_job = 0

# Callback function for when a job is selected
def job_callback(choice):
    # Retrieve the numeric value of the selected job from the dictionary
    numeric_job = job_dict[choice]
    # Print the numeric job value
    print("Numeric job choice:", numeric_job)

# Create the job combobox
job_combobox = customtkinter.CTkOptionMenu(master=root,
                                           fg_color=("black"),
                                           bg_color=("black"),
                                           values=["admin", "blue-collar", "entrepreneur", "housemaid",
                                                   "management", "retired", "self-employed", "services",
                                                   "student", "technician", "unemployed", "unknown"],
                                           command=job_callback,
                                           variable=job)

# Place the job combobox on the window
job_combobox.place(relx=0.86, rely=0.25, anchor="center")

# PART 2.6: Click "yes", if the client has deposit default
# Define a function to handle the default checkbox event
def default_checkbox_event():
    # Print the deposit default value when the checkbox state changes
    print("Deposit default value:", default_check.get())

# Set initial value for default checkbox (0 for off)
default_check = customtkinter.StringVar(value="0")

# Create the default checkbox widget
default_checkbox = customtkinter.CTkCheckBox(root,
                                             text="Client has deposit default",
                                             command=default_checkbox_event,
                                             variable=default_check,
                                             onvalue="1",  # Value when checkbox is checked
                                             offvalue="0")  # Value when checkbox is unchecked

# Place the default checkbox widget on the window
default_checkbox.place(relx=0.2, rely=0.35, anchor="center")

# PART 2.7: Click "yes", if the client has housing loan
# Define a function to handle the housing checkbox event
def housing_checkbox_event():
    # Print the housing loan value when the checkbox state changes
    print("Housing loan value:", housing_check.get())

# Set initial value for housing checkbox (0 for off)
housing_check = customtkinter.StringVar(value="0")

# Create the housing checkbox widget
housing_checkbox = customtkinter.CTkCheckBox(root,
                                             text="Client has housing loan",
                                             command=housing_checkbox_event,
                                             variable=housing_check,
                                             onvalue="1",  # Value when checkbox is checked
                                             offvalue="0")  # Value when checkbox is unchecked

# Place the housing checkbox widget on the window
housing_checkbox.place(relx=0.5, rely=0.35, anchor="center")

# PART 2.8: Question "What is the client's balance?"
# Create a new frame `balance_form` to contain the Label and Entry widgets
balance_form = tk.Frame(relief=tk.SUNKEN, borderwidth=2)
# Place the balance_form frame in the window
balance_form.place(relx=0.8, rely=0.35, anchor="center")

# Create the Label widget for asking the balance question
lbl_balance = tk.Label(master=balance_form, text="What is the balance?")
# Create the Entry widget for entering the balance
ent_balance = tk.Entry(master=balance_form, width=5)
# Position the label and entry widgets inside the frame using grid layout
lbl_balance.grid(row=0, column=0, sticky="e")
ent_balance.grid(row=0, column=1)

# Function to handle when Enter key is pressed
def handle_enter(event):
    balance_value = ent_balance.get()  # Get the value entered
    if not balance_value:  # If the value is empty
        balance_value = 0  # Set default value to 0
    else:
        try:
            balance_value = float(balance_value)  # Try converting to float
        except ValueError:
            print("Error: Please enter a valid balance (numeric value).")
            return  # Exit the function if value is not a number
    print("Balance entered:", balance_value)

# Bind the <Return> event to the ent_balance Entry widget
ent_balance.bind("<Return>", handle_enter)

# PART 2.9: Question "Does the client's have a personal loan?"
# Define a function to handle the personal loan checkbox event
def personal_loan_checkbox_event():
    # Print the personal loan value when the checkbox state changes
    print("Personal loan value:", personal_loan_check.get())

# Set initial value for personal loan checkbox (0 for off)
personal_loan_check = customtkinter.StringVar(value="0")

# Create the personal loan checkbox widget
personal_loan_checkbox = customtkinter.CTkCheckBox(root,
                                                    text="Client has personal loan",
                                                    command=personal_loan_checkbox_event,
                                                    variable=personal_loan_check,
                                                    onvalue="1",  # Value when checkbox is checked
                                                    offvalue="0")  # Value when checkbox is unchecked

# Place the personal loan checkbox widget on the window
personal_loan_checkbox.place(relx=0.19, rely=0.45, anchor="center")

# PART 2.10: Question "What was the contact method?"
# Dictionary to map contact methods to numeric values
contact_method_dict = {"cellular": 1, "telephone": 2, "unknown": 3}

# Set initial value for contact method
contact_method = customtkinter.StringVar(value="telephone")

# Initializing a variable
numeric_contact_method = 0
# Callback function for when a contact method is selected
def contact_method_callback(choice):
    # Retrieve the numeric value of the selected contact method from the dictionary
    numeric_contact_method = contact_method_dict[choice]
    # Print the numeric contact method value
    print("Numeric contact method choice:", numeric_contact_method)

# Create the contact method combobox
contact_method_combobox = customtkinter.CTkOptionMenu(master=root,
                                                     fg_color=("black"),
                                                     bg_color=("black"),
                                                     values=["cellular", "telephone", "unknown"],
                                                     command=contact_method_callback,
                                                     variable=contact_method)

# Place the contact method combobox on the window
contact_method_combobox.place(relx=0.5, rely=0.45, anchor="center")

# PART 2.11: Question "What a day it was?"
# Dictionary to map days of the week to numeric values
day_dict = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 7}

# Set initial value for day
day = customtkinter.StringVar(value="Monday")

# Initializing a variable
numeric_day = 0

# Callback function for when a day is selected
def day_callback(choice):
    # Retrieve the numeric value of the selected day from the dictionary
    numeric_day = day_dict[choice]
    # Print the numeric day value
    print("Numeric day:", numeric_day)

# Create the day combobox
day_combobox = customtkinter.CTkOptionMenu(master=root,
                                           fg_color=("black"),
                                           bg_color=("black"),
                                           values=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                                           command=day_callback,
                                           variable=day)

# Place the day combobox on the window
day_combobox.place(relx=0.8, rely=0.45, anchor="center")

# PART 2.12: Question "What a month it was?"
# Set initial value for month
month = customtkinter.StringVar(value="January")


# Function to convert month name to its numeric value
def convert_to_numeric(chosen_month):
    # List of months in order
    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    # Return the index of the chosen month plus 1 (to match numeric representation)
    return months.index(chosen_month) + 1

# Initializing a variable
numeric_month = 0

# Callback function for when a month is selected
def month_callback(choice):
    # Convert the chosen month to its numeric value
    numeric_month = convert_to_numeric(choice)
    # Print the numeric month value
    print("Numeric month:", numeric_month)

# Create the month combobox
month_combobox = customtkinter.CTkOptionMenu(master=root,
                                             fg_color=("black"),
                                             bg_color=("black"),
                                             values=["January", "February", "March", "April", "May", "June", "July",
                                                     "August", "September", "October", "November", "December"],
                                             command=month_callback,
                                             variable=month)

# Place the month combobox on the window
month_combobox.place(relx=0.19, rely=0.55, anchor="center")

# PART 2.13: Question "How long the contact was (in seconds)?"
# Create a new frame `contact_duration_form` to contain the Label and Entry widgets
contact_duration_form = tk.Frame(relief=tk.SUNKEN, borderwidth=2)
# Place the contact_duration_form frame in the window
contact_duration_form.place(relx=0.5, rely=0.55, anchor="center")

# Create the Label widget for asking the duration of contact question
lbl_contact_duration = tk.Label(master=contact_duration_form, text="Length of the contact (in sec):")
# Create the Entry widget for entering the duration of contact
ent_contact_duration = tk.Entry(master=contact_duration_form, width=5)
# Position the label and entry widgets inside the frame using grid layout
lbl_contact_duration.grid(row=0, column=0, sticky="e")
ent_contact_duration.grid(row=0, column=1)

# Function to handle when Enter key is pressed
def handle_enter(event):
    duration_value = ent_contact_duration.get()  # Get the value entered
    if not duration_value:  # If the value is empty
        duration_value = 0  # Set default value to 0
    else:
        try:
            duration_value = int(duration_value)  # Try converting to integer
        except ValueError:
            print("Error: Please enter a valid duration (numeric value).")
            return  # Exit the function if value is not a number
    print("Duration of contact entered:", duration_value)

# Bind the <Return> event to the ent_contact_duration Entry widget
ent_contact_duration.bind("<Return>", handle_enter)

# PART 2.14: Question "What is the previous outcome of the marketing campaign?"
# Dictionary to map outcomes of a previous marketing campaign to numeric values
poutcome_dict = {"Failure": 0, "Other": 1, "Success": 2, "Unknown": 3}

# Set initial value for poutcome
poutcome = customtkinter.StringVar(value="Failure")

# Initializing a variable
numeric_poutcome = 0

# Callback function for when an outcome is selected
def poutcome_callback(choice):
    # Retrieve the numeric value of the selected outcome from the dictionary
    numeric_poutcome = poutcome_dict[choice]
    # Print the numeric outcome value
    print("Numeric outcome:", numeric_poutcome)

# Create the outcome combobox
poutcome_combobox = customtkinter.CTkOptionMenu(master=root,
                                                fg_color=("black"),
                                                bg_color=("black"),
                                                values=["Failure", "Other", "Success", "Unknown"],
                                                command=poutcome_callback,
                                                variable=poutcome)

# Place the outcome combobox on the window
poutcome_combobox.place(relx=0.8, rely=0.55, anchor="center")

# PART 2.15: Question "How many number of contacts were done in this campaign?"
# Create a new frame `contact_number_form` to contain the Label and Entry widgets
contact_number_form = tk.Frame(relief=tk.SUNKEN, borderwidth=2)
# Place the contact_number_form frame in the window
contact_number_form.place(relx=0.23, rely=0.65, anchor="center")

# Create the Label widget for asking the question about the number of contact numbers done
lbl_contact_number = tk.Label(master=contact_number_form, text="Contact numbers were done now:")
# Create the Entry widget for entering the number of contact numbers done
ent_contact_number = tk.Entry(master=contact_number_form, width=5)
# Position the label and entry widgets inside the frame using grid layout
lbl_contact_number.grid(row=0, column=0, sticky="e")
ent_contact_number.grid(row=0, column=1)

# Function to handle when Enter key is pressed
def handle_enter(event):
    contact_number_value = ent_contact_number.get()  # Get the value entered
    if not contact_number_value:  # If the value is empty
        contact_number_value = 0  # Set default value to 0
    else:
        try:
            contact_number_value = int(contact_number_value)  # Try converting to integer
        except ValueError:
            print("Error: Please enter a valid number of contact numbers (numeric value).")
            return  # Exit the function if value is not a number
    print("Contact numbers were done now:", contact_number_value)

# Bind the <Return> event to the ent_contact_number Entry widget
ent_contact_number.bind("<Return>", handle_enter)

# PART 2.16: Question "How many number of contacts were done in the previous campaign?"
# Create a new frame `previous_contact_number_form` to contain the Label and Entry widgets
previous_contact_number_form = tk.Frame(relief=tk.SUNKEN, borderwidth=2)
# Place the previous_contact_number_form frame in the window
previous_contact_number_form.place(relx=0.73, rely=0.65, anchor="center")

# Create the Label widget for asking the question about the number of contact numbers done in the previous campaign
lbl_previous_contact_number = tk.Label(master=previous_contact_number_form, text="Contact numbers were done in p_campaign:")
# Create the Entry widget for entering the number of contact numbers done in the previous campaign
ent_previous_contact_number = tk.Entry(master=previous_contact_number_form, width=5)

# Position the label and entry widgets inside the frame using grid layout
lbl_previous_contact_number.grid(row=0, column=0, sticky="e")
ent_previous_contact_number.grid(row=0, column=1)

# Function to handle when Enter key is pressed
def handle_enter(event):
    previous_contact_number_value = ent_previous_contact_number.get()  # Get the value entered
    if not previous_contact_number_value:  # If the value is empty
        previous_contact_number_value = 0  # Set default value to 0
    else:
        try:
            previous_contact_number_value = int(previous_contact_number_value)  # Try converting to integer
        except ValueError:
            print("Error: Please enter a valid number of contact numbers (numeric value).")
            return  # Exit the function if value is not a number
    print("Contact numbers were done in p_campaign:", previous_contact_number_value)

# Bind the <Return> event to the ent_previous_contact_number Entry widget
ent_previous_contact_number.bind("<Return>", handle_enter)

# PART 2.17: Question "How many days that passed by after the client was last contacted?"
# Create a new frame `last_contact_days_form` to contain the Label and Entry widgets
last_contact_days_form = tk.Frame(relief=tk.SUNKEN, borderwidth=2)
# Place the last_contact_days_form frame in the window
last_contact_days_form.place(relx=0.5, rely=0.75, anchor="center")

# Create the Label widget for asking the question about the number of days since the last contact
lbl_last_contact_days = tk.Label(master=last_contact_days_form, text="How many days passed by after the client was last contacted?")
# Create the Entry widget for entering the number of days since the last contact
ent_last_contact_days = tk.Entry(master=last_contact_days_form, width=5)
# Position the label and entry widgets inside the frame using grid layout
lbl_last_contact_days.grid(row=0, column=0, sticky="e")
ent_last_contact_days.grid(row=0, column=1)

# Function to handle when Enter key is pressed
def handle_enter(event):
    last_contact_days_value = ent_last_contact_days.get()  # Get the value entered
    if not last_contact_days_value:  # If the value is empty
        last_contact_days_value = 0  # Set default value to 0
    else:
        try:
            last_contact_days_value = int(last_contact_days_value)  # Try converting to integer
        except ValueError:
            print("Error: Please enter a valid number of days (numeric value).")
            return  # Exit the function if value is not a number
    print("Number of days since last contact:", last_contact_days_value)

# Bind the <Return> event to the ent_last_contact_days Entry widget
ent_last_contact_days.bind("<Return>", handle_enter)

# PART 2.18: showing text that states "Waiting for user input..."
# make a label for just showing text (the result)
result_var = tkinter.StringVar()
label = tkinter.Label(root, textvariable=result_var)
result_var.set("Waiting for user input...")
label.place(relx=0.5, rely=0.84, anchor="center")


# ------------ PART 3 ------------

# PART 3: Collecting user responses and making predictions
# Function for collecting user responses and making predictions


# the function that is run when button is pressed
def set_text_by_button():
    # convert textbox value into integer if possible
    row_age = int(ent_age.get())
    row_job = numeric_job
    row_marital_status = numeric_marital_status
    row_education = numeric_education
    row_default_check = int(default_check.get())
    row_balance_form = int(ent_balance.get())
    row_housing_check = int(housing_check.get())
    row_personal_loan_check = int(personal_loan_check.get())
    row_contact_method = numeric_contact_method
    row_day = numeric_day
    row_month = numeric_month
    row_contact_duration_form = int(ent_contact_duration.get())
    row_contact_number_form = int(ent_contact_number.get())
    row_last_contact_days_form = int(ent_last_contact_days.get())
    row_previous_contact_number_form = int(ent_previous_contact_number.get())
    row_poutcome = numeric_poutcome

    # let's convert the user input into the
    # format that our model understands
    tester_row = {
        'age': row_age,
        'job': row_job,
        'marital': row_marital_status,
        'education': row_education,
        'failed_previous_credit': row_default_check,
        'balance': row_balance_form,
        'housing_loan': row_housing_check,
        'loan': row_personal_loan_check,
        'contact_type': row_contact_method,
        'day': row_day,
        'month': row_month,
        'contact_duration_sec': row_contact_duration_form,
        'number_of_contacts': row_contact_number_form,
        'days_since_last_contact': row_last_contact_days_form,
        'previous_number_of_contacts': row_previous_contact_number_form,
        'poutcome': row_poutcome
    }

    # convert to pandas-format
    tester_row = pd.DataFrame([tester_row])

    # Predict using logistic regression
    prediction = lm.predict(tester_row)[0]

    # Display the prediction result
    if prediction == 1:
        result_var.set("This client will take a deposit.")
    else:
        result_var.set("This client will not take a deposit.")

# helper function that allows us to press Enter to launch
# the button press function
def handle_enter(event):
    set_text_by_button()

# Define and configure the button to initiate prediction
set_up_button = tkinter.Button(root, height=1, width=16, text="Check the client", command=set_text_by_button)
set_up_button.pack(side="bottom", pady=20)

# Start the main event loop
root.mainloop()
