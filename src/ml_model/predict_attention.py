import joblib
import numpy as np
import pandas as pd

class AttentionPredictor:
    def __init__(self, model_path):
        print("Loading model...")
        self.model = joblib.load(model_path)
        print("Model loaded.")

    def predict(self, feature_vector):
        """
        feature_vector example:
        [face_present, eye_closed, head_turn, yawn]
        """
        columns = ['face_present', 'eye_closed', 'head_turn', 'yawn']
        df = pd.DataFrame([feature_vector], columns=columns)
        return self.model.predict(df)[0]

    def predict_with_probability(self, feature_vector):
        feature_vector = np.array(feature_vector).reshape(1, -1)
        prediction = self.model.predict(feature_vector)
        probability = self.model.predict_proba(feature_vector)
        return prediction[0], probability

    def batch_predict(self, feature_list):
        feature_array = np.array(feature_list)
        predictions = self.model.predict(feature_array)
        return predictions


if __name__ == "__main__":
    predictor = AttentionPredictor(
        "../../models/attention_model.pkl"
    )

    sample = [1, 0, 0, 0]
    result = predictor.predict(sample)
    print("Prediction:", result)