import streamlit as st

def show():

    st.title("💡 Daily Health Tips")

    tips = [
        "🥗 Eat healthy and balanced food.",
        "💧 Drink at least 8 glasses of water every day.",
        "🏃 Exercise for 30 minutes daily.",
        "😴 Sleep for 7-8 hours every night.",
        "🍎 Eat fresh fruits and vegetables.",
        "🚭 Avoid smoking and alcohol.",
        "🧘 Practice yoga or meditation to reduce stress."
    ]

    for tip in tips:
        st.success(tip)