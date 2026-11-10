import streamlit as st
import sqlite3

import home
import bmi
import medicine
import water
import nearby
import chatbot
import dashboard
import emergency
import about
import health

st.set_page_config(
    page_title="Health Care AI Smart Health Assistant",
    page_icon="🏥",
    layout="wide"
)

# ---------------- DATABASE ----------------
conn = sqlite3.connect("health.db", check_same_thread=False)
cursor = conn.cursor()

# ---------------- LOGIN ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.title("🏥 Health Care AI Smart Health Assistant")
    st.subheader("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
            st.success("✅ Login Successful!")
            st.rerun()
        else:
            st.error("❌ Invalid Username or Password")

    st.stop()

# ---------------- SIDEBAR ----------------
st.sidebar.title("🏥 Health Care AI")

menu = st.sidebar.radio(
    "📋 Select Menu",
    [
        "🏠 Home",
        "🩺 BMI Calculator",
        "💊 Medicine Reminder",
        "💧 Water Reminder",
        "🏥 Nearby Hospitals",
        "💡 Health Tips",
        "🚑 Emergency Contacts",
        "🤖 AI Health Chat",
        "📊 Dashboard",
        "ℹ️ About"
    ]
)

# ---------------- PAGES ----------------

if menu == "🏠 Home":
    home.show()

elif menu == "🩺 BMI Calculator":
    bmi.show()

elif menu == "💊 Medicine Reminder":
    medicine.show()

elif menu == "💧 Water Reminder":
    water.show()

elif menu == "🏥 Nearby Hospitals":
    nearby.show()

elif menu == "💡 Health Tips":
    tips.show()

elif menu == "🚑 Emergency Contacts":
    emergency.show()

elif menu == "🤖 AI Health Chat":
    chatbot.show()

elif menu == "📊 Dashboard":
    dashboard.show()

elif menu == "ℹ️ About":
    about.show()