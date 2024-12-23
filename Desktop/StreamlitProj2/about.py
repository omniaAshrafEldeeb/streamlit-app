import streamlit as st
def app():
    #for col1,col2, col3 = st.
    v1 ,v2=st.columns([3,10])
    with v2 :st.header("information about us")
    v1 ,v2=st.columns([3,10])
    with v2 : st.title("")
    v1 ,v2,v3=st.columns([3,3,5])
    with v1 :st.markdown("made by : ***Omnia ElDeeb***")
    with v2 :st.markdown("Email: 0omniaeldeep0@gmail.com")
    with v3 : st.markdown("Github link : https://github.com/omniaAshrafEldeeb")