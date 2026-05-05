import joblib
import os

class ModelUtils:
    @staticmethod
    def save_model(model, path):
        folder = os.path.dirname(path)

        if not os.path.exists(folder):
            os.makedirs(folder)

        joblib.dump(model, path)
        print("Model saved successfully:", path)

    @staticmethod
    def load_model(path):
        if not os.path.exists(path):
            raise FileNotFoundError("Model file not found")

        model = joblib.load(path)
        print("Model loaded successfully")
        return model

    @staticmethod
    def model_exists(path):
        return os.path.exists(path)

    @staticmethod
    def print_model_info(model): 
        print("Model Type:", type(model))

        if hasattr(model, "n_estimators"):
            print("Number of Trees:", model.n_estimators)

        if hasattr(model, "feature_importances_"):
            print("Feature Importance:", model.feature_importances_)


if __name__ == "__main__":
    path = "../../models/attention_model.pkl"

    if ModelUtils.model_exists(path):
        model = ModelUtils.load_model(path)
        ModelUtils.print_model_info(model)
    else:
        print("Model file not found.")