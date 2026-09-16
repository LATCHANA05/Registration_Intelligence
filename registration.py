import streamlit as st
from database import add_attendee

def show_registration():

    st.header("📝 Attendee Registration")

    name = st.text_input("Full Name")

    email = st.text_input("Email")

    phone = st.text_input("Phone Number")

    college = st.text_input("College")

    department = st.selectbox(
        "Department",
        ["ECE", "EEE", "CSE", "IT", "AIDS", "Mechanical", "Civil"]
    )

    event = st.selectbox(
        "Event",
        ["AI Workshop", "Python Workshop", "Hackathon", "Seminar"]
    )

    city = st.text_input("City")

    age = st.number_input(
        "Age",
        min_value=16,
        max_value=100,
        step=1
    )

    gender = st.radio(
        "Gender",
        ["Male", "Female", "Other"]
    )

    if st.button("🚀 Register"):

        if name == "" or email == "" or phone == "" or college == "" or city == "":
            st.error("Please fill all required fields.")

        else:

            add_attendee(
                name,
                email,
                phone,
                college,
                department,
                event,
                city,
                age,
                gender
            )

            st.success("🎉 Registration Successful!")