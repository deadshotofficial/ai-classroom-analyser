import cv2
import time

class VideoCaptureManager:
    def __init__(self, source=0):
        self.source = source
        self.cap = cv2.VideoCapture(source)

        if not self.cap.isOpened():
            raise Exception("Error opening video source")

        self.frame_count = 0

    def get_frame(self):
        ret, frame = self.cap.read()

        if not ret:
            return None

        self.frame_count += 1
        return frame

    def release(self):
        self.cap.release()

    def show_frame(self, frame):
        cv2.imshow("Smart Classroom Analyzer", frame)

    def run_preview(self):
        while True:
            frame = self.get_frame()

            if frame is None:
                break

            self.show_frame(frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.release()
        cv2.destroyAllWindows()


def extract_frames(video_path, save_folder, interval=10):
    cap = cv2.VideoCapture(video_path)

    frame_id = 0
    saved_count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        if frame_id % interval == 0:
            filename = f"{save_folder}/frame_{saved_count}.jpg"
            cv2.imwrite(filename, frame)
            saved_count += 1

        frame_id += 1

    cap.release()
    print(f"Saved {saved_count} frames.")


if __name__ == "__main__":
    manager = VideoCaptureManager(0)
    manager.run_preview()