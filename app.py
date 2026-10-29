import streamlit as st
import json
import os
import time

# Page settings
st.set_page_config(
    page_title="AI Traffic Management System",
    layout="wide"
)

st.title("🚦 AI-Powered Traffic Management System")

placeholder = st.empty()

while True:

    # Read JSON data
    if os.path.exists("data/traffic_data.json"):

        with open("data/traffic_data.json", "r") as file:
            data = json.load(file)

    else:

        data = {
            "total": 0,
            "cars": 0,
            "bikes": 0,
            "buses": 0,
            "trucks": 0,
            "density": "LOW",
            "green_time": 0,
            "emergency": False,
            "vehicle": "None"
        }

    # Dashboard
    with placeholder.container():

        col1, col2, col3 = st.columns(3)

        col1.metric("Vehicles", data["total"])
        col2.metric("Density", data["density"])
        col3.metric("Signal Time", f"{data['green_time']} sec")

        st.markdown("---")

        col4, col5 = st.columns(2)

        col4.metric("Cars", data["cars"])
        col5.metric("Bikes", data["bikes"])

        col6, col7 = st.columns(2)

        col6.metric("Buses", data["buses"])
        col7.metric("Trucks", data["trucks"])

        # Emergency alert
        if data["emergency"]:
            st.error(
                f"🚑 Emergency vehicle detected: {data['vehicle']}"
            )

    time.sleep(1)