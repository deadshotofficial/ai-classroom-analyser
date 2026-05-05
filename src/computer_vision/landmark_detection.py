import cv2
import mediapipe as mp

class LandmarkDetector:
    def __init__(self):
        self.mp_face_mesh = mp.solutions.face_mesh

        self.face_mesh = self.mp_face_mesh.FaceMesh(
            static_image_mode=False,
            max_num_faces=5,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

        self.drawer = mp.solutions.drawing_utils

    def get_landmarks(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb)

        landmarks_list = []

        if results.multi_face_landmarks:
            h, w, _ = frame.shape

            for face_landmarks in results.multi_face_landmarks:
                face_points = []

                for lm in face_landmarks.landmark:
                    x = int(lm.x * w)
                    y = int(lm.y * h)

                    face_points.append((x, y))

                landmarks_list.append(face_points)

        return landmarks_list

    def draw_landmarks(self, frame, landmarks_list):
        for face_landmarks in landmarks_list:
            for (x, y) in face_landmarks:
                cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

        return frame


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    detector = LandmarkDetector()

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        landmarks = detector.get_landmarks(frame)
        frame = detector.draw_landmarks(frame, landmarks)
        cv2.imshow("Landmarks", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()