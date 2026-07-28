import streamlit as st

def show():

    st.title("📊 Health Dashboard")

    st.write("Welcome to your Health Dashboard")

    st.metric("💧 Water Goal", "8 Glasses")

    st.metric("🏃 Exercise", "30 Minutes")

    st.metric("😴 Sleep", "8 Hours")

    st.success("✅ Keep following a healthy lifestyle every day!")