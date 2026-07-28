import streamlit as st

def show():

    st.title("🤖 AI Health Chat")

    question = st.text_input("💬 Ask your health question")

    if st.button("Ask AI"):

        if question == "":
            st.warning("⚠️ Please enter your question.")

        else:
            st.success("🤖 AI Response")

            st.write("Thank you for your question.")

            st.write("This is a basic AI Health Assistant.")

            st.info("💡 For serious health problems, always consult a qualified doctor.")