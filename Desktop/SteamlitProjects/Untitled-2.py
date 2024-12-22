import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
file =st.file_uploader("Upload file", type = ['csv'])
if file is not None:
    df = pd.read_csv(file)
    n_rows = st.slider("choose number of rows", 1,len(df),step =1)
    n_columns = st.multiselect("choose columns you want to appear", df.columns.tolist(),df.columns.tolist())
    r = st.write(df[:n_rows][n_columns])
    #columns_to_chart = st.multiselect("choose columns you want to make chart", df.columns.tolist(),max_selections= 2)
    #if len(columns_to_chart) == 2:
    #x,y = columns_to_chart
    numberical_columns = df.select_dtypes(include = np.number).columns.tolist()
    
    print('okay')
    
    tab1, tab2 = st.tabs(["Scatter plot", "Histogram"])
    with tab1 :
        col1, col2, col3 = st.columns(3)
        with col1:
            selct1 = st.selectbox('Select column in x axis', numberical_columns)
        with col2 :
            selct2 = st.selectbox('Select column in y axis', df.columns)
        with col3:
            select_color = st.selectbox('Select column to be color ', df.columns)
    
        fig_scater = px.scatter(df, selct1 , selct2 , color =select_color)
        st.plotly_chart(fig_scater)
    with tab2:
        col_to_histo = st.selectbox("choose column to make Histogram for it", df.columns)
        fig_hist = px.histogram(df,col_to_histo)
        st.plotly_chart(fig_hist)
print(df.columns)
