1. Logistic Regression --> SVC
2. Linear Regression --> SVR

I used these datasets for the linear and logistic regression, but I opted to try SVM as well on these datasets to see if I could achieve better metric results using different methods of optimization.



1. Logistic Regression --> SVC

Logistics regression results VS SVC results

Precision for class 0:  
83% VS 86%

Precision for class 1:  
79% VS 83%  
SVC achieves slightly higher precision for both classes compared to Logistic Regression, indicating that SVC produces fewer false positives.

Recall for class 0:  
86% VS 89%

Recall for class 1:  
75% VS 80%  
Logistic Regression has higher recall for class 0, while SVC has higher recall for class 1. This suggests that Logistic Regression is better at identifying true negatives, while SVC is better at identifying true positives.

F1-score for class 0:  
84% VS 88%

F1-score for class 1:  
77% VS 81%  
SVC outperforms Logistic Regression in terms of F1-score for both classes, indicating better overall performance in terms of balancing precision and recall.

Accuracy:  
81.44% VS 84.94%  
SVC achieves higher accuracy (84.94%) compared to Logistic Regression (81.44%), indicating that it makes fewer overall mistakes in classification.

In summary, based on the provided results, Support Vector Classifier (SVC) demonstrates superior performance compared to Logistic Regression across various evaluation metrics, including precision, recall, F1-score, and overall accuracy.



---------------------------------------------------------------------------------



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
