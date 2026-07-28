import streamlit as st
def show():
    
    st.title("💊 Medicine Reminder")
    medicine = st.text_input("💊 Enter Medicine Name")

    time = st.time_input("⏰ Select Reminder Time")

    if st.button("Save Reminder"):

        st.success("✅ Reminder Saved!")

        st.info(f"💊 Medicine: {medicine}")

        st.info(f"⏰ Time: {time}")

        st.warning("📌 Please take your medicine on time.")