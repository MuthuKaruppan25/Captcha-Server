import numpy as np
import joblib
import math
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import warnings
from pydantic import BaseModel

# Suppress warnings
warnings.filterwarnings("ignore")

app = FastAPI()

# Allow CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, modify if needed
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Load the models from the files
logreg = joblib.load('logistic_regression_model_best10.pkl')
rf_model = joblib.load('random_forest_model_best10.pkl')
gb_model = joblib.load('gradient_boosting_model_best10.pkl')
svc_model = joblib.load('svm_model_best10.pkl')
knn_model = joblib.load('k-nearest_neighbors_model_best10.pkl')
nb_model = joblib.load('naive_bayes_model_best10.pkl')
dt_model = joblib.load('decision_tree_model_best10.pkl')
ada_model = joblib.load('adaboost_model_best10.pkl')
bagging_model = joblib.load('bagging_model_best10.pkl')
extra_trees_model = joblib.load('extra_trees_model_best10.pkl')
voting_trees = joblib.load('voting_classifier_model_best10.pkl')

lrlog = joblib.load('logistic_regression_model_mouse.pkl')
rflog = joblib.load('random_forest_model_mouse.pkl')
gblog = joblib.load('gradient_boosting_model_mouse.pkl')


class Features(BaseModel):
    features: list[float]


@app.post("/predict")
async def predict(features: Features):
    try:
        # Extract features from the request
        features = features.features
        print("Received Features:", features)

        # Replace NaN values with 0
        features = [0 if x is None or math.isnan(x) else x for x in features]

        if features[0] != 0:
            new_data = np.array([features])

            zero_count = 0
            total_conf_bot = 0  # To store the cumulative confidence for bot (0)
            total_conf_human = 0  # To store the cumulative confidence for human (1)
            model_count = 0  # To count the number of models used

            def make_prediction(model, model_name):
                nonlocal zero_count, total_conf_bot, total_conf_human, model_count
                pred = model.predict(new_data)[0]
                conf = model.predict_proba(new_data)[0]  # Probability for bot (0) and human (1)
                print(f"{model_name} Prediction: {int(pred)}")
                print(f"{model_name} Confidence: bot (0): {conf[0]}, human (1): {conf[1]}")

                total_conf_bot += conf[0]
                total_conf_human += conf[1]
                model_count += 1

                if pred == 0:
                    zero_count += 1

            # Make predictions with all models
            make_prediction(logreg, "Logistic Regression")
            make_prediction(rf_model, "Random Forest")
            make_prediction(gb_model, "Gradient Boosting")
            make_prediction(svc_model, "SVM")
            make_prediction(knn_model, "K-Nearest Neighbors")
            make_prediction(nb_model, "Naive Bayes")
            make_prediction(dt_model, "Decision Tree")
            make_prediction(ada_model, "AdaBoost")
            make_prediction(bagging_model, "Bagging")
            make_prediction(extra_trees_model, "Extra Trees")
            make_prediction(voting_trees, "Voting Trees")

            if zero_count >= 6:
                classification = 'bot'
            else:
                classification = 'human'

            avg_conf_bot = total_conf_bot / 11
            avg_conf_human = total_conf_human / 11

            print(f"\nFinal Classification: {classification}")
            print(f"Average Confidence for bot (0): {avg_conf_bot:.2f}")
            print(f"Average Confidence for human (1): {avg_conf_human:.2f}")

            response = {
                'classification': classification,
                'average_confidence_human': avg_conf_human,
                'average_confidence_bot': avg_conf_bot
            }
            return response

        else:
            data1 = [features[0], features[10], features[12], features[15]]
            new_data = np.array([data1])

            total_conf_bot = 0
            zero_count = 0
            total_conf_human = 0

            def make_prediction(model, model_name):
                nonlocal zero_count, total_conf_bot, total_conf_human
                pred = model.predict(new_data)[0]
                conf = model.predict_proba(new_data)[0]
                print(f"{model_name} Prediction: {int(pred)}")
                print(f"{model_name} Confidence: bot (0): {conf[0]}, human (1): {conf[1]}")

                total_conf_bot += conf[0]
                total_conf_human += conf[1]

                if pred == 0:
                    zero_count += 1

            make_prediction(lrlog, "Logistic Regression")
            make_prediction(rflog, "Random Forest")
            make_prediction(gblog, "Gradient Boosting")

            avg_human_conf = total_conf_human / 3

            if zero_count >= 2:
                classification = 'bot'
            else:
                classification = 'human'

            print(f"\nFinal Classification: {classification}")
            print(f"Average Human Confidence: {avg_human_conf}")

            return {"average_confidence_human": avg_human_conf}

    except Exception as e:
        print(f"Error: {str(e)}")
        return {"error": str(e)}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
