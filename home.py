import streamlit as st

def show():

    st.title("🏥 Health Care AI Smart Health Assistant")

    st.write("Welcome to the Health Care AI Smart Health Assistant!")

    name = st.text_input("Enter your name")

    age = st.number_input(
        "Enter your age",
        min_value=1,
        max_value=120
    )

    symptom = st.selectbox(
        "Select your symptom",
        ["Fever", "Cold", "Headache", "Cough", "Stomach Pain"]
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
            st.write("☕ Drink warm water and consult a doctor if it continues.")
        elif symptom == "Stomach Pain":
            st.write("🥣 Eat light food and drink plenty of water.")

        st.warning("⚠️ This is only a basic health suggestion. Please consult a doctor.")