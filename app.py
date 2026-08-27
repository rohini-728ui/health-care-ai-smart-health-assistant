import streamlit as st
import sqlite3

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Health Care AI Smart Health Assistant",
    page_icon="🏥",
    layout="wide"
)

# ---------------- IMPORT MODULES ----------------
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

# ---------------- DATABASE ----------------
conn = sqlite3.connect("health.db", check_same_thread=False)
cursor = conn.cursor()

# ---------------- LOGIN STATUS ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- LOGIN PAGE ----------------
if not st.session_state.logged_in:

    st.title("🏥 Health Care AI Smart Health Assistant")
    st.subheader("🔐 Login")

    st.write(
        "Welcome to the Health Care AI Smart Health Assistant!"
    )

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


# ---------------- HOME INPUTS ----------------
st.title("🏥 Health Care AI Smart Health Assistant")

name = st.text_input("Enter your name")

age = st.number_input(
    "Enter your age",
    min_value=1,
    max_value=120
)

symptom = st.selectbox(
    "Select your symptom",
    [
        "Fever",
        "Cold",
        "Headache",
        "Cough",
        "Stomach Pain"
    ]
)

if st.button("Get Suggestion"):

    st.success(f"Hello {name}!")

    if symptom == "Fever":
        st.write("💊 Drink plenty of water and take proper rest.")

    elif symptom == "Cold":
        st.write("🤧 Drink warm fluids and take enough rest.")

    elif symptom == "Headache":
        st.write("😴 Rest well and stay hydrated.")

    elif symptom == "Cough":
        st.write(
            "🍯 Drink warm water and consult a doctor if it continues."
        )

    elif symptom == "Stomach Pain":
        st.write(
            "🥣 Eat light food and drink plenty of water."
        )

    st.warning(
        "⚠️ This is only a basic health suggestion. "
        "Please consult a doctor for medical advice."
    )


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
    health.show()

elif menu == "🚑 Emergency Contacts":
    emergency.show()

elif menu == "🤖 AI Health Chat":
    chatbot.show()

elif menu == "📊 Dashboard":
    dashboard.show()

elif menu == "ℹ️ About":
    about.show()