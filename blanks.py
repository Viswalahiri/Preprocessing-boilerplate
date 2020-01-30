## Getting rid of blank entries.
import pandas as pd
import numpy as np

dataset = pd.read_csv('Data.csv')

# Simple Imputer takes care of imputation transformation and completes missing values

from sklearn.impute import SimpleImputer 

# Take all features
X = dataset.iloc[:,:-1].values

# Take dependant variables
y = dataset.iloc[:,-1].values

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

# Fit for all columns that have a column that has an empty value
# Assuming allcolumns have a missing value
imputer.fit(X[:, 1:-1],y)

# Transform the dataset using imputer.transform.
X[:,1:-1] = imputer.transform(X[:,1:-1])
