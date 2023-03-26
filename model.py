import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Loading the data
df = pd.read_csv("houses.csv")

# Rescale the data, but make sure to not have an imbalance
df = pd.get_dummies(df, columns=["orientation"])

# Initiating the linear regression model
model = LinearRegression()

# Splitting data into train and test
train, test = train_test_split(df)

# define X and y for the training data
X_train = train.drop(columns=["price"])
y_train = train["price"]

# define X and y for the testing data
X_test = test.drop(columns=["price"])
y_test = test["price"]

# train model
model.fit(X_train, y_train)

# predict on training data
y_predict = model.predict(X_train)

# Save the model
joblib.dump(model, "regression.joblib")

# TODO: Add test for the model