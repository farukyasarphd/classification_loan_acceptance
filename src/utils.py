import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import (
    classification_report, accuracy_score, recall_score,
    precision_score, f1_score, confusion_matrix, ConfusionMatrixDisplay
)
import matplotlib.pyplot as plt
from src.config import RANDOM_STATE

# Load Excel File
def load_excel(data_path, filename, sheet_name=None):
    """
    Load data from the specified sheet of an Excel file.

    Args:
        data_path (str): Path to the directory containing the Excel file.
        filename (str): Name of the Excel file.
        sheet_name (str or None): Name of the sheet to load. If None, loads the first sheet.

    Returns:
        pd.DataFrame: Loaded data as a pandas DataFrame.
    """
    file_path = f"{data_path}/{filename}"
    try:
        data = pd.read_excel(file_path, sheet_name=sheet_name)
        print(f"File '{filename}' loaded successfully!")
        return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None


# Train Model
def train_model(X_train, y_train, model_type, **kwargs):
    """
    Train a machine learning model with optional parameter arguments.

    Args:
        X_train (pd.DataFrame): Training features.
        y_train (pd.Series): Training target.
        model_type (str): The type of model to train. Supported models: 'xgboost', 'random_forest', 'gradient_boosting', 'logistic_regression'.
        **kwargs: Additional arguments for the model (e.g., n_estimators, learning_rate).

    Returns:
        Trained model.
    """
    
    # Default parameters
    default_params = {
        "random_state": RANDOM_STATE
    }

    # Merge default and explicitly provided parameters
    final_params = {**default_params, **kwargs}
    # Initialize model
    if model_type == "xgboost":
        model = XGBClassifier( **final_params)
    elif model_type == "random_forest":
        model = RandomForestClassifier( **final_params)
    elif model_type == "gradient_boosting":
        model = GradientBoostingClassifier( **final_params)
    elif model_type == "logistic_regression":
        model = LogisticRegression( **final_params)
    else:
        raise ValueError("Unsupported model type. Choose from 'xgboost', 'random_forest', 'gradient_boosting', 'logistic_regression'.")

    model.fit(X_train, y_train)
    return model

# Hyperparameter Tuning
def tune_hyperparameters(X_train, y_train, model, param_grid, scoring="recall"):
    """
    Perform hyperparameter tuning using GridSearchCV.

    Args:
        X_train (pd.DataFrame): Training features.
        y_train (pd.Series): Training target.
        model: A machine learning model (e.g., RandomForestClassifier()).
        param_grid (dict): Hyperparameter grid for tuning.
        scoring (str): Scoring metric for GridSearchCV.

    Returns:
        Best estimator after GridSearchCV.
    """
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, scoring=scoring, cv=5, n_jobs=-1)
    grid_search.fit(X_train, y_train)
    print(f"Best Parameters: {grid_search.best_params_}")
    return grid_search.best_estimator_

# Evaluate Model
def evaluate_model(model, X_test, y_test):
    """
    Evaluate a trained model on the test set and print key metrics.

    Args:
        model (sklearn or XGBoost model): Trained model.
        X_test (pd.DataFrame): Test features.
        y_test (pd.Series): Test target.

    Returns:
        dict: A dictionary of evaluation metrics.
    """
    y_pred = model.predict(X_test)
    metrics = {
        "Accuracy": accuracy_score(y_test, y_pred),
        "Recall": recall_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred),
        "F1-Score": f1_score(y_test, y_pred)
    }
    return metrics

# Plot Confusion Matrix
def plot_confusion_matrix(model, X_test, y_test):
    """
    Plot the confusion matrix for a trained model.

    Args:
        model (sklearn or XGBoost model): Trained model.
        X_test (pd.DataFrame): Test features.
        y_test (pd.Series): Test target.
    """
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(cmap="Blues", values_format="d")
    plt.title("Confusion Matrix")
    plt.show()