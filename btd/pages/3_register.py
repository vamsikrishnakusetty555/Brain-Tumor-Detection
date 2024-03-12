import streamlit as st
import re
import time
import Home
import pymysql

connection = pymysql.connect(
    host="sql6.freesqldatabase.com",
    user="sql6690767",
    password="HLW1BXqGQa",
    database="sql6690767"
)


def db(email,username,password):
    cursor=connection.cursor()
    query="INSERT INTO users (email, username, password) VALUES (%s, %s, %s)"
    data=(email,username,password)
    cursor.execute(query,data)
    connection.commit()
    cursor.close()
def css():
    st.markdown("""
    <style>
    .intro, .quote {
        text-align: justify;
    }
    </style>
    """, unsafe_allow_html=True)

def app1():
    css()
    st.title(":orange[Brain Tumor] Detection Portal")
    st.sidebar.empty()
    c1, c2 = st.columns([1.5, 2], gap="small")

    with c1:
        st.markdown("## Overview")
        st.markdown(
            "<p class='intro'>The Brain Tumor Detection Portal revolutionizes early diagnosis through MRI analysis. Leveraging advanced algorithms, our platform swiftly detects brain abnormalities with precision using MRI scan images as input.</p>",
            unsafe_allow_html=True)

    with c2:
        show_registration_page()

def show_registration_page():
    st.markdown("## Registration")

    # Registration form
    user_id_input = st.text_input("Email", key="user_id_input", value="", help="Enter your email address")
    name_input = st.text_input("Username", key="name_input", value="", help="Enter your name")
    password_input = st.text_input("Password", key="password_input", value="", type="password", help="Enter your password")
    confirm_password_input = st.text_input("Confirm Password", key="confirm_password_input", value="", type="password", help="Confirm your password")

    # Register button
    if st.button("Register"):
        # Validate form data
        if not (user_id_input and name_input and password_input and confirm_password_input):
            st.warning("Please fill in all fields.")
        elif not re.match(r"^\S+@\S+\.\S+$", user_id_input):
            st.warning("Please enter a valid email address.")
        elif password_input != confirm_password_input:
            st.warning("Passwords do not match.")
        else:
            # Store form data in session state or proceed with registration logic
            db(user_id_input,name_input,password_input)
            st.success("Registration Successful!")
            time.sleep(1)
            st.success("Go to Login Page!")

if __name__ == "__main__":
    Home.sidebar()
    app1()
