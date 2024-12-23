import streamlit as st
import pandas as pd
import pyodbc


def app():
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
    v1 ,v2=st.columns([3,8])

    with v2: st.title("Hospitals")
    v1 ,v2=st.columns([3,10])
    with v2 : st.header("")
    if conn2:
        st.sidebar.success("Connection successful!")
        #Hospital1 = st.button('Hospital list')

        #if Hospital1 :
        

        # Example query
        query2 ="SELECT  H_name, H_manager_name, H_address, H_email, rating FROM Hospital_info"
        try:
            df = pd.read_sql(query2, conn2)
            for i, row in df.iterrows():
                col1,col2 = st.columns([25,10])
                H_name = row['H_name']
                H_manager = row['H_manager_name']
                H_address = row['H_address']
                H_email = row['H_email']

                sentiment_mapping = ["one", "two", "three", "four", "five"]


                # Display the food details
                with col1:st.write(f" ***{H_name}***, Hospital manager: {H_manager}, Hospital address: {H_address}, Hospital name: {H_email}")
                                # Use st.slider to get the rating
                with col2:selected = st.feedback("stars",key = f"feedback_{i}")
                if selected is not None:
                    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")

                #with col2: rating = st.slider(f"Rate {D_name}", 0, 5, 0, key=f"slider_{i}")
                df.at[i, 'rating'] = selected  # Update the rating in the DataFrame

            # Show the DataFrame with the ratings
            on = st.toggle("Show Doctor Tables")

            if on:
                st.write("Hospital Ratings:")
                #st.dataframe(query2)
                st.write(df)
        except Exception as e:
            st.error(f"Query failed: {e}")
        finally:
            conn2.close()