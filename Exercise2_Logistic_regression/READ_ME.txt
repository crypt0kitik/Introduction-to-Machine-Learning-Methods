This project is ongoing in real-time. I am currently working on it.


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

GUI (Graphical User Interface):
1. Imports, load and test of the model
