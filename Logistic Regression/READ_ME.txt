This project contains 2 parts: Logistic Regression and GUI

---------- Data Analytics + ML ----------

The cleaning data part:
1. Check all NaN values --> delete if there are 
2. Check duplicates --> delete if there are 
3. Check the job column --> use clustering or other methods to modify it into numeric
4. marital column --> OneHotEncoder
5. education column --> OneHotEncoder
6. default column --> LabelEncoder
7. housing column --> LabelEncoder
8. loan column --> LabelEncoder
9. contact column --> OneHotEncoder 
10. month column --> use clustering or other methods to modify it into numeric
11. poutcome column --> OneHotEncoder 
12. deposit column --> LabelEncoder
13. Remove outliers by checking balance of these columns

Logistic regression part:
14. Converting data to X/y and checking multicollinearity by using VIF
15. Scaling the values
16. Creating the logistic regression and fitting the data
17. Classification error metrics
18. Testing the model with new data
19. Saving a trained scikit-learn model into a file
20. Analysis

---------- GUI ----------

GUI (Graphical User Interface):
PART 1: imports and load of the model
1.1 Imports
1.2 load and test of the model

PART 2: placing questions
2.1 Setting the background image
2.2 Adding text about the goal of this GUI
2.3: Question "How old is the client?"
2.4: Choose a client's marital status
2.5: Choose a client's job
2.6: Click "yes", if the client has deposit default
2.7: Click "yes", if the client has housing loan
2.8: Question "What is the client's balance?"
2.9: Question "Does the client's have a personal loan?"
2.10: Question "What was the contact method?"
2.11: Question "What a day it was?"
2.12: Question "What a month it was?"
2.13 Question "How long the contact was (in seconds)?"
2.14: Question "What is the previous outcome of the marketing campaign?"
2.15: Question "How many number of contacts were done in this campaign?"
2.16: Question "How many number of contacts were done in the previous campaign?"
2.17: Question "How many days that passed by after the client was last contacted?"
2.18: Showing text that states "Waiting for user input..."

PART 3: Collecting user responses and making predictions
3.1: Converting all values to int and name them
3.2: Converting the user input into the format that the model understands
3.3: Converting to pandas-format
3.4: Making prediction using logistic regression
3.5: Displaying the prediction result
3.6: Defining and configuring the button to initiate prediction