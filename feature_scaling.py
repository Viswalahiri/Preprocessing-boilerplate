## Feature Scaling
import sklearn

# we perform feature scaling since we must ensure that none of the dependant variables overlap on each other and thus are considered more important.
# For example, when we perform euclidean distance on two columns, then we see that one is very much larger than the other, in which case we normalize.

from sklearn.preprocessing import StandardScalar
sc_X = StandardScalar()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

# Two types of features scaling exist, which are normalizing and standardizing

# Should one go about feature scaling dummy variables?
# For easy implementation - no
# For higher accuracy - yes

# Feature scaling should generally be done for the dependent variable as well, particularly during regression.
