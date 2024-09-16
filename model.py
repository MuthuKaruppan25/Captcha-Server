import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib  # Import joblib to save the model

# Load the dataset from a CSV file
df = pd.read_csv('datak1.csv')

# Fill NaN values with 0
df = df.fillna(0)

# Use iloc to select features and label
# Features are in columns 0 to 7, and label is in column 8
X = df.iloc[:, :-1]  # Select all rows and columns except the last one for features
y = df.iloc[:, -1]   # Select all rows and only the last column for label

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the Logistic Regression model
logreg = LogisticRegression(max_iter=1000)  # Increased max_iter to ensure convergence

# Train the model
logreg.fit(X_train, y_train)

# Save the trained model to a file
joblib.dump(logreg, 'logistic_regression_model_mouse.pkl')  # Save the model as 'logistic_regression_model.pkl'

# Make predictions on the test set
y_pred = logreg.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Logistic Regression Accuracy: {accuracy:.2f}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))



# Initialize the Random Forest model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
rf_model.fit(X_train, y_train)

# Save the trained model to a file
joblib.dump(rf_model, 'random_forest_model_mouse.pkl')

# Evaluate the model (optional)
y_pred_rf = rf_model.predict(X_test)
accuracy_rf = accuracy_score(y_test, y_pred_rf)
print(f"Random Forest Model Accuracy: {accuracy_rf:.2f}")

# Initialize the Gradient Boosting model
gb_model = GradientBoostingClassifier(random_state=42)

# Train the model
gb_model.fit(X_train, y_train)

# Save the trained model to a file
joblib.dump(gb_model, 'gradient_boosting_model_mouse.pkl')

# Evaluate the model (optional)
y_pred_gb = gb_model.predict(X_test)
accuracy_gb = accuracy_score(y_test, y_pred_gb)
print(f"Gradient Boosting Model Accuracy: {accuracy_gb:.2f}")
