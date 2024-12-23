import streamlit as st
def app():
    st.header("information you")


    with st.form("my_form"):
        user_id_n = st.text_input("Enter your user id")
        password_n = st.text_input("Enter password")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            if user_id_n != "omnia" or password_n != 'o':
                st.write("Please enter correct user id and password")
            st.write(f"hello {user_id_n}")
            #st.page_link(r"C:\Users\MF\Desktop\StreamlitProj2\Home.py", label="Page 1", icon="1️⃣")

            #st.switch_page("pages/Home.py")
