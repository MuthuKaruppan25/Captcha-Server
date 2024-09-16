import numpy as np
import joblib  # Import joblib to load the model

# Load the models from the files
logreg = joblib.load('logistic_regression_model.pkl')
rf_model = joblib.load('random_forest_model.pkl')
gb_model = joblib.load('gradient_boosting_model.pkl')

# Prepare new data for prediction
new_data = np.array([[0, 0, 10.6, 0.2, 0.008, 13.3, 10.2, 1.1]])  # Example new data with 8 features

# Make predictions using each model
logreg_pred = logreg.predict(new_data)
rf_pred = rf_model.predict(new_data)
gb_pred = gb_model.predict(new_data)

# Print predictions
print(f"Logistic Regression Prediction: {logreg_pred[0]}")
print(f"Random Forest Prediction: {rf_pred[0]}")
print(f"Gradient Boosting Prediction: {gb_pred[0]}")
