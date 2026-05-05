import numpy as np

class EyeAspectRatio:
    def __init__(self, threshold=0.25):
        self.threshold = threshold

    def compute_distance(self, p1, p2):
        return np.linalg.norm(np.array(p1) - np.array(p2))

    def calculate_ear(self, eye_points):
        A = self.compute_distance(eye_points[1], eye_points[5])
        B = self.compute_distance(eye_points[2], eye_points[4])
        C = self.compute_distance(eye_points[0], eye_points[3])

        ear = (A + B) / (2.0 * C)
        return ear

    def is_eye_closed(self, ear):
        return ear < self.threshold

    def analyze_eye(self, eye_points):
        ear = self.calculate_ear(eye_points)
        closed = self.is_eye_closed(ear)

        return {
            "ear": ear,
            "eye_closed": int(closed)
        }


if __name__ == "__main__":
    # Example test
    eye = [(10,10),(12,8),(14,8),(16,10),(14,12),(12,12)]

    ear_system = EyeAspectRatio()
    result = ear_system.analyze_eye(eye)

    print("EAR:", result["ear"])
    print("Eye Closed:", result["eye_closed"])