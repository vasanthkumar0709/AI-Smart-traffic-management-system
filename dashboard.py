import streamlit as st

st.set_page_config(
    page_title="AI Traffic Management",
    layout="wide"
)

st.title("🚦 AI-Powered Traffic Management System")

st.metric("🚗 Total Vehicles", 28)
st.metric("🚦 Traffic Density", "HIGH")
st.metric("⏱️ Green Signal Time", "45 sec")

st.success("System Running Successfully")