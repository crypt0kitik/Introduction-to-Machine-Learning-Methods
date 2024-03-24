1. Logistic Regression --> SVC
2. Linear Regression --> SVR

I used these datasets for the linear and logistic regression, but I opted to try SVM as well on these datasets to see if I could achieve better metric results using different methods of optimization.




1. Logistic Regression --> SVC

---------------------------

2. Linear Regression --> SVR
Comparing the results between linear regression and support vector regression (SVR), we observe the following:

Linear regression results VS SVR results:
MAE 0.3 VS MAE 0.13 $  
This indicates that SVR provides more accurate predictions on average.

MSE 0.15 ^2 VS MSE 0.03 $^2  
SVR demonstrates superior performance in minimizing squared errors.

RMSE 0.38 VS RMSE 0.17  
SVR provides more precise predictions with smaller root mean squared errors.

R-squared 0.44 VS R-squared 0.48  
SVR outperforms linear regression with an R-squared value of 0.48, suggesting a better fit to the data.

Overall, SVR consistently outperforms linear regression across all metrics in this comparison.
