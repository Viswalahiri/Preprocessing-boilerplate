## Encoding Catergorical Variables.
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer 

ct = ColumnTransformer(
    [('onehotencoder', OneHotEncoder(), [0])],    # The column numbers to be transformed (here is [0] but can be [0, 1, 3])
    remainder='passthrough'                         # Leave the rest of the columns untouched
)

X = np.array(ct.fit_transform(X), dtype=np.float)

#Encode target labels with value between 0 and n_classes-1.
labelencoder = LabelEncoder()

y = labelencoder.fit_transform(y)
