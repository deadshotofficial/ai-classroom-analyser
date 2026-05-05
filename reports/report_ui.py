import streamlit as st
import pandas as pd
import sys

csv_path = sys.argv[1] if len(sys.argv) > 1 else "reports/engagement_states.csv"

def run_dashboard():
    st.set_page_config(
        page_title="Smart Classroom Report",
        layout="centered"
    )

    st.title("📊 Smart Classroom Engagement Report")

    df = pd.read_csv(csv_path)

    total = len(df)
    engaged = (df["state"] == "engaged").sum()
    distracted = (df["state"] == "distracted").sum()

    score = (engaged / total) * 100 if total > 0 else 0

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Frames", total)
    col2.metric("Engaged", engaged)
    col3.metric("Distracted", distracted)
    col4.metric("Score (%)", round(score, 2))

    st.divider()

    st.subheader("Engagement Distribution")
    st.bar_chart(df["state"].value_counts())

    st.subheader("Attention Timeline")
    st.line_chart((df["state"] == "engaged").astype(int))

run_dashboard()