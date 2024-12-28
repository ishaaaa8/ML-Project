import os
import sys

import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)

def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}

        for model_name, model in models.items():
            # Skip models incompatible with GridSearchCV
            if model_name in ["CatBoosting Regressor", "XGBRegressor"]:
                print(f"Skipping {model_name} for GridSearchCV.")
                continue

            print(f"Evaluating {model_name} with GridSearchCV.")
            params = param.get(model_name, {})
            
            gs = GridSearchCV(model, params, cv=3, scoring="r2", n_jobs=-1)
            gs.fit(X_train, y_train)

            # Retrieve the best model from GridSearchCV
            best_model = gs.best_estimator_

            # Predictions for train and test data
            y_train_pred = best_model.predict(X_train)
            y_test_pred = best_model.predict(X_test)

            # Calculate R^2 scores
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            # Store the test score in the report
            report[model_name] = test_model_score

            print(f"{model_name} -> Train R^2: {train_model_score}, Test R^2: {test_model_score}")

        return report

    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)