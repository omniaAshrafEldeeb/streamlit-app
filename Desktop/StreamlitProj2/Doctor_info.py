import streamlit as st
import pyodbc
import pandas as pd
from sqlalchemy import create_engine


def app():
    v1 ,v2=st.columns([3,12])
    with v2: st.title("information about Doctors")
    v1 ,v2=st.columns([3,10])
    with v2 : st.subheader("")

    def get_connection():
        try:
            conn2 = pyodbc.connect(
                "DRIVER={ODBC Driver 17 for SQL Server};"
                "SERVER=OMNO;"
                "DATABASE=NewHospital;"
                "Trusted_Connection=yes;"
            )
            return conn2
        except Exception as e:
            st.error(f"Error connecting to database: {e}")
            return None

    conn2 = get_connection()





    if conn2:
        st.sidebar.success("Connection successful!")
        #Doctor1 = st.button('Doctor list')

        #if Doctor1 :
    

        # Example query
        query = "SELECT TOP 10 * FROM Doctor;"  # Replace with your table name
        query2 = "SELECT D_id, D_name, De_id, rating FROM Doctor;"  # Replace with your table name
        query3 = "SELECT D_id, H_id FROM H_D;"  # Replace with your table name
        query6 = "SELECT H_name, H_id FROM Hospital_info;"  # Replace with your table name
        query4 = "SELECT D_id, phone_number FROM D_phone;"  # Replace with your table name
        query5 = "SELECT De_id, De_name FROM Department;"  # Replace with your table name
        print(type(query2))
        print(type(query5))




        try:
            Doc = pd.read_sql(query2, conn2)
            #st.write(Doc)
            H_D = pd.read_sql(query3, conn2)
            Hospital = pd.read_sql(query6, conn2)
            #st.write(df2)
            phone = pd.read_sql(query4, conn2)
            #st.write(phone)
            df4 = pd.read_sql(query5, conn2)
            result0 = pd.merge(df4, Doc, on='De_id', how='right')
            result1 = pd.merge (result0, phone, on = 'D_id', how = 'left')
            result2 = pd.merge(result1, H_D, on= 'D_id', how='left')
            result3 = pd.merge(result2,Hospital )

            #st.dataframe(result3)
            result4 = result3[['D_name','De_name','phone_number', "H_name","rating"]]
            #st.write(result4)

            
            for i, row in result4.iterrows():
                col1,col2 = st.columns([25,10])
                D_name = row['D_name']
                De_name = row['De_name']
                phone_number = row['phone_number']
                H_name = row['H_name']

                sentiment_mapping = ["one", "two", "three", "four", "five"]


                # Display the food details
                with col1:st.write(f" ***{D_name}***, Department: {De_name}, phone: {phone_number}, Hospital name: {H_name}")
                                # Use st.slider to get the rating
                with col2:selected = st.feedback("stars",key = f"feedback_{i}")
                if selected is not None:
                    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")

                #with col2: rating = st.slider(f"Rate {D_name}", 0, 5, 0, key=f"slider_{i}")
                result4.at[i, 'rating'] = selected  # Update the rating in the DataFrame

            # Show the DataFrame with the ratings
            on = st.toggle("Show Doctor Tables")

            if on:
                st.write("Doctor Ratings:")
                st.dataframe(result4)
        except Exception as e:
            st.error(f"Query failed: {e}")
        finally:
            conn2.close()