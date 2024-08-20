# README
This subfolder has the models regarding the statement of the problem. We find three different models, namely, a regressor, a classifier and a segmentor model.

## Regressor Model
We consider a set of different models and finally we obtained a acceptable performance:
```
Stacking Regressor Performance Metrics:
  Mean Absolute Error (MAE): 0.0712
  Mean Squared Error (MSE): 0.0123
  Root Mean Squared Error (RMSE): 0.1108
  R² Score: 0.7531
```

## Classifier Model
We consider a set of different models and finally we obtained a acceptable performance:
```
Stacking Classifier Metrics on Validation Set:
  Accuracy: 0.8469
  Precision: 0.8450
  Recall: 0.8469
  F1 Score: 0.8457
----------------------------------------
Classification Report:
              precision    recall  f1-score   support

           0       0.90      0.91      0.90      1085
           1       0.64      0.55      0.59       108
           2       0.77      0.78      0.78       492

    accuracy                           0.85      1685
   macro avg       0.77      0.75      0.76      1685
weighted avg       0.84      0.85      0.85      1685
```

# Segmentor model
We achive $4$ different groups:<br/>
***Cluster $0$:***<br/>
*Moderate Pollution Levels:* CO and NO2 levels are moderate, suggesting areas with average pollution.
<br/>
***Cluster $1$:***<br/>
*Moderately Low Pollution:* Slightly lower pollution levels compared to Cluster $0$, with moderate temperatures and humidity.<br/>
***Cluster $2$:***<br/>
*Low Pollution Levels:* Lowest levels of CO and NO2 among the clusters, indicating areas with better air quality.<br/>
***Cluster $3$:***<br/>
*High Pollution Levels:* Highest levels of CO and NO2, indicating significant pollution likely due to heavy traffic or industrial activities.
