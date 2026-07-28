import streamlit as st

def show():

    st.title("💧 Water Reminder")

    st.write("Stay hydrated every day!")

    glasses = st.slider(
        "🥤 How many glasses of water did you drink today?",
        0,
        15,
        0
    )

    if st.button("Check Water Intake"):

        st.info(f"💧 You drank {glasses} glasses of water today.")

        if glasses >= 8:
            st.success("✅ Excellent! Your body is well hydrated.")
        elif glasses >= 5:
            st.warning("⚠️ Good, but try to drink a little more water.")
        else:
            st.error("❌ Drink at least 8 glasses of water every day.")