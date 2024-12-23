import streamlit as st
from streamlit_option_menu import option_menu
import pyodbc
import pandas as pd
from sqlalchemy import create_engine



def get_connection():
    try:
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=OMNO;"
            "DATABASE=NewHospital;"
            "Trusted_Connection=yes;"
        )
        return conn
    except Exception as e:
        st.error(f"Error connecting to database: {e}")
        return None

conn = get_connection()


def get_db_connection():
    server = 'OMNO'
    database = 'NewHospital'

    # SQLAlchemy connection string for Windows Authentication
    connection_string = f"mssql+pyodbc://@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes"

    # Create the SQLAlchemy engine
    engine = create_engine(connection_string)
    return engine

if "db_connection" not in st.session_state:
    st.session_state["db_connection"] = get_db_connection()

# Retrieve the shared connection
engine = st.session_state["db_connection"]


import Home, Hospital_info, about, My_info , Tests, Doctor_info

st.set_page_config(page_title = "Hospital App", page_icon= '🏥', layout="wide")
st.snow()



class MultiApp :
    
    def __init__ (self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append (
            {"title": title,
            "function" : func,
            })
        
    def run():
        with st.sidebar:
            app = option_menu(
                menu_title ='Hispotals app',
                menu_icon = 'options',
                options = ['Home', "Hospitals info","Doctors info","My info","Tests","About&contact"] ,
                icons = [] ,
                default_index = 0,
        
            )

        if app == "Home":
            Home.app()

        if app == "Hospitals info":
            Hospital_info.app()
        if app == "Doctors info":
            Doctor_info.app()
        if app == "My info":
            #
            # st.balloons()
            My_info.app()
        if app == "Tests":
            Tests.app()
        if app == "About&contact":
            about.app()

    run()    
    print("okay6")






# Inject the CSS into the app using st.markdown








