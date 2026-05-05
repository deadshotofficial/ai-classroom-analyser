import os

class Config:
    # Video settings
    VIDEO_SOURCE = 0  # Use webcam
    FRAME_WIDTH = 640
    FRAME_HEIGHT = 480

    # Feature thresholds
    EAR_THRESHOLD = 0.25
    YAWN_THRESHOLD = 0.6
    HEAD_POSE_THRESHOLD = 2.95

    # Paths
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

    DATA_DIR = os.path.join(BASE_DIR, "data")
    FEATURE_DATASET = os.path.join(DATA_DIR, "features", "attention_features.csv")

    MODEL_DIR = os.path.join(BASE_DIR, "models")
    MODEL_PATH = os.path.join(BASE_DIR, "models", "attention_model.pkl")

    REPORT_DIR = os.path.join(BASE_DIR, "reports")

    # Engagement scoring
    ENGAGED_WEIGHT = 1
    DISTRACTED_WEIGHT = 0

    # Dashboard
    DASHBOARD_PORT = 8501

    @staticmethod
    def create_folders():
        folders = [
            Config.DATA_DIR,
            os.path.join(Config.DATA_DIR, "features"),
            Config.MODEL_DIR,
            Config.REPORT_DIR
        ]

        for folder in folders:
            os.makedirs(folder, exist_ok=True)