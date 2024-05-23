import streamlit as st
import re
import time
import Home
import pymysql

connection = pymysql.connect(
    host="sql12.freesqldatabase.com",
    user="sql12708566",
    password="bwQh8CzCRw",
    database="sql12708566"
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
    st.title(":orange[Brain Tumor] Detection using CNN")
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

    user_id_input = st.text_input("Email", key="user_id_input", value="", help="Enter your email address")
    name_input = st.text_input("Username", key="name_input", value="", help="Enter your name")
    password_input = st.text_input("Password", key="password_input", value="", type="password", help="Enter your password")
    confirm_password_input = st.text_input("Confirm Password", key="confirm_password_input", value="", type="password", help="Confirm your password")

    if st.button("Register"):
        if not (user_id_input and name_input and password_input and confirm_password_input):
            st.warning("Please fill in all fields.")
        elif not re.match(r"^\S+@(gmail\.com|yahoo\.com|outlook\.com)$", user_id_input):
            st.warning("Please enter a valid email address ending with @gmail.com, @yahoo.com, or @outlook.com.")
        elif len(password_input) < 8:
            st.warning("Password must be at least 8 characters long.")
        elif not re.search(r"[A-Z]", password_input):
            st.warning("Password must contain at least one uppercase letter.")
        elif not re.search(r"[a-z]", password_input):
            st.warning("Password must contain at least one lowercase letter.")
        elif not re.search(r"\d", password_input):
            st.warning("Password must contain at least one digit.")
        elif not re.search(r"[ !@#$%^&*()_+{}\[\]:;<>,.?/~\\-]", password_input):
            st.warning("Password must contain at least one special character.")
        elif password_input != confirm_password_input:
            st.warning("Passwords do not match.")
        else:
            db(user_id_input, name_input, password_input)
            st.success("Registration Successful!")
            time.sleep(1)
            st.success("Go to Login Page!")

if __name__ == "__main__":
    Home.sidebar()
    app1()
