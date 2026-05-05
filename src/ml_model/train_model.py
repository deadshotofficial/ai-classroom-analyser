from importlib.resources import path

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
data_path = os.path.join(BASE_DIR, "data", "features", "attention_features.csv")
model_path = os.path.join(BASE_DIR, "models", "attention_model.pkl")

class AttentionModelTrainer:
    def __init__(self, data_path):
        self.data_path = data_path
        self.model = RandomForestClassifier(
            n_estimators=100,
            random_state=42,
            class_weight='balanced'
        )

    def load_dataset(self):
        df = pd.read_csv(self.data_path)

        if "label" not in df.columns:
            raise Exception("Dataset must contain 'label' column")

        X = df.drop("label", axis=1)
        y = df["label"]

        return X, y

    def split_data(self, X, y):
        return train_test_split(
            X, y,
            test_size=0.2,
            random_state=42
        )

    def train(self, X_train, y_train):
        print("Training model...")
        self.model.fit(X_train, y_train)
        print("Training complete.")

    def evaluate(self, X_test, y_test):
        predictions = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)

        print("\nModel Accuracy:", accuracy)
        print("\nClassification Report:")
        print(classification_report(y_test, predictions))

    def save_model(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        joblib.dump(self.model, path)

        print("Model saved to:", path)


if __name__ == "__main__":
    trainer = AttentionModelTrainer(data_path)

    X, y = trainer.load_dataset()
    X_train, X_test, y_train, y_test = trainer.split_data(X, y)

    trainer.train(X_train, y_train)
    trainer.evaluate(X_test, y_test)
    trainer.save_model(model_path)