import streamlit as st

def show():

    st.title("🏥 Nearby Hospitals")

    st.write("Here are some popular hospitals:")

    st.success("🏥 Apollo Hospital\n📍 Hyderabad\n☎️ +91-40-2360-7777")

    st.success("🏥 Yashoda Hospital\n📍 Hyderabad\n☎️ +91-40-4567-4567")

    st.success("🏥 KIMS Hospital\n📍 Hyderabad\n☎️ +91-40-4488-5000")

    st.info("💡 In the future, you can connect this feature with Google Maps API to show nearby hospitals automatically.")