# Preprocessing-boilerplate

This is a standard template for data preprocessing

 In general data preprocessing has 4 steps.

## 1 . Replacing / Removing blank entries (blanks.py)
  - Rows will blank entries can be removed. However, this isn't suggested as it can lead to the loss of important data.
  - Replacing can be done with the help of SimpleImputer in the sklearn.preprocessing module.
  - Functionality is provided to help replace the np.nan (blank) values with a statistical feature of choice. 
    - eg. the blank rows can be replaced by the mean of the column.

## 2 . Encoding categorical variables (categorical.py)
  - Columns that possess categorical variables with more than 2 values are generally tended to be One Hot Encoded.
  - If there are only two categorical variables, then the column is usually Label Encoded.

## 3 . Train and test (train_and_test.py)
  - The number of feature and result rows are divided into two parts for training and testing respectively.
  - The standard size for train:test is 4:1
  
## 4 . Feature scaling (feature_scaling.py)
  - Features are to be scaled so that none of them influence the model more than the other feature.
  - Two types of features exist, which include
    - Normalizing : Usually done when the data's plots are observed to be in the shape of a bell.
    - Standardizing : Usually done in any other situtation. 
  - Feature scaling can also be done on the dummy variables in order to achieve higher accuracies and make the model better.
  - Feature scaling should be done on the dependent variable as well, particularly during regression.
