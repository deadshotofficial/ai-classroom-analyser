import cmd
import sys

import pandas as pd
import os
import subprocess
import webbrowser
import time

class EngagementReport:
    def __init__(self):
        self.states = []

    def add_state(self, state):
        self.states.append(state)

    def generate_summary(self):
        total = len(self.states)
        engaged = self.states.count("engaged")
        distracted = self.states.count("distracted")

        score = (engaged / total) * 100 if total > 0 else 0

        return {
            "total": total,
            "engaged": engaged,
            "distracted": distracted,
            "score": round(score, 2)
        }

    def save_csv(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path = os.path.join(base_dir, "reports", "engagement_states.csv")

        os.makedirs(os.path.dirname(path), exist_ok=True)

        df = pd.DataFrame({"state": self.states})
        df.to_csv(path, index=False)

        return path

    def launch_dashboard(self, csv_path):
        print("Launching dashboard...")

        # Absolute path to report_ui.py
        base_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(base_dir, "report_ui.py")

        cmd = [
            sys.executable,
            "-m",
            "streamlit",
            "run",
            ui_path,
            "--",
            csv_path
        ]

        subprocess.Popen(cmd)

        time.sleep(3)

    def generate_and_show(self):
        summary = self.generate_summary()

        print("\n===== Engagement Summary =====")
        for k, v in summary.items():
            print(f"{k}: {v}")

        csv_path = self.save_csv()
        self.launch_dashboard(csv_path)