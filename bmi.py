import streamlit as st
def show():

    st.title("🩺 BMI Calculator")

    weight = st.number_input(
        "Enter your Weight (kg)",
        min_value=1.0
    )

    height = st.number_input(
        "Enter your Height (m)",
        min_value=0.5
    )

    if st.button("Calculate BMI"):

        bmi = weight / (height * height)

        st.success(f"Your BMI is {bmi:.2f}")

        if bmi < 18.5:
            st.warning("⚠️ Underweight")
        elif bmi < 25:
            st.success("✅ Normal Weight")
        elif bmi < 30:
            st.warning("⚠️ Overweight")
        else:
            st.error("❌ Obese")