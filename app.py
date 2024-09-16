from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import joblib
import math

app = Flask(__name__)
CORS(app)

# Load the models from the files
logreg = joblib.load('logistic_regression_modelnew.pkl')
rf_model = joblib.load('random_forest_modelnew.pkl')
gb_model = joblib.load('gradient_boosting_modelnew.pkl')

@app.route('/predict', methods=['POST', 'OPTIONS'])
def predict():
    try:
        if request.method == 'OPTIONS':
            return jsonify({'status': 'OK'}), 200

        # Get the JSON data from the request
        data = request.get_json()

        # Extract features from the JSON data
        features = data.get('features')
        print(features)

        # Replace NaN values with 0
        for i in range(len(features)):
            if features[i] is None:
                features[i] = 0
            if math.isnan(features[i]):
                features[i] = 0

        # Convert features to a numpy array
        new_data = np.array([features])

        # Make predictions and get confidence scores using each model
        logreg_pred = logreg.predict(new_data)
        rf_pred = rf_model.predict(new_data)
        gb_pred = gb_model.predict(new_data)

        logreg_conf = logreg.predict_proba(new_data)[0]  # Confidence for both classes
        rf_conf = rf_model.predict_proba(new_data)[0]
        gb_conf = gb_model.predict_proba(new_data)[0]

        zero_count = sum([int(logreg_pred[0]) == 0, int(rf_pred[0]) == 0, int(gb_pred[0]) == 0])

        # Determine if it's a bot or a human based on the count of 0s
        if zero_count >= 2:
            classification = 'bot'
        else:
            classification = 'human'

        # Prepare the response with predictions and confidence scores
        response = {
            'Logistic Regression Prediction': int(logreg_pred[0]),
            'Logistic Regression Confidence': {
                'bot (0)': logreg_conf[0],
                'human (1)': logreg_conf[1]
            },
            'Random Forest Prediction': int(rf_pred[0]),
            'Random Forest Confidence': {
                'bot (0)': rf_conf[0],
                'human (1)': rf_conf[1]
            },
            'Gradient Boosting Prediction': int(gb_pred[0]),
            'Gradient Boosting Confidence': {
                'bot (0)': gb_conf[0],
                'human (1)': gb_conf[1]
            },
            'Classification': classification
        }

        print(response)  # Optional: Print the response to the console
        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
