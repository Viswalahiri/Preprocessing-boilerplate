import sklearn
# Dividing our data into parts

# We divide our data into two parts, these are mainly, training and testing.

X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
