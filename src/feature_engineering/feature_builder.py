import pandas as pd

class FeatureBuilder:
    def __init__(self):
        self.rows = []

    def build_feature_vector(self, face_present, eye_closed, head_turn, yawn):
        vector = {
            "face_present": face_present,
            "eye_closed": eye_closed,
            "head_turn": head_turn,
            "yawn": yawn
        }

        return vector

    def add_row(self, vector):
        self.rows.append(vector)

    def save_dataset(self, filepath):
        df = pd.DataFrame(self.rows)
        df.to_csv(filepath, index=False)
        print("Dataset saved:", filepath)

    def calculate_label(self, vector):
        if vector["eye_closed"] == 1:
            return "distracted"

        if vector["head_turn"] == 1:
            return "distracted"

        if vector["yawn"] == 1:
            return "distracted"

        return "engaged"


if __name__ == "__main__":
    builder = FeatureBuilder()

    sample = builder.build_feature_vector(
        face_present=1,
        eye_closed=0,
        head_turn=0,
        yawn=0
    )

    builder.add_row(sample)
    builder.save_dataset("attention_features.csv")