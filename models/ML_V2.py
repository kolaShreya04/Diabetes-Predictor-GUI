import pandas as pd
import xgboost as xgb  # Import XGBoost
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle

# Load the dataset
ds = pd.read_csv('framingham.csv')
print(ds['diabetes'].value_counts())

print("All the items in the data set.")
ds.dropna(axis=0, how='any', inplace=True)
print(ds.shape)

print(" ")
print(ds['diabetes'].value_counts())  
print("This is the average of the data set.")

# Prepare the data
X = ds.drop(columns=['diabetes'])
Y = ds['diabetes']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

# Create and train the XGBoost model
Model_XGB = xgb.XGBClassifier(n_estimators=200)  # Number of trees in the forest
Model_XGB.fit(X_train, Y_train)

# Make predictions
Predict_XGB = Model_XGB.predict(X_test)

# Calculate accuracy
Score_XGB = accuracy_score(Y_test, Predict_XGB)

# Save the trained model
with open('Diabetes_model', 'wb') as f:
    pickle.dump(Model_XGB, f)

print(Score_XGB)
print(" ")

# Print classification report and confusion matrix
print(classification_report(Y_test, Predict_XGB))
print(confusion_matrix(Y_test, Predict_XGB))
