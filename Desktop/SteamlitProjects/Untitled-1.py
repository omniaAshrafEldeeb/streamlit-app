import streamlit as st
import time
st.header("Shapes Calculation")
#st.select_slider("hello")
Shape = st.selectbox("Choose Calculate",["Circle", 
"Rectangle"])

print(Shape)

if Shape == "Circle":
    reduis = st.number_input("Redius", min_value=0.0, step=0.1)
    with st.spinner("Calculating......."):
        time.sleep(1)
        area = reduis*reduis*3.14

if Shape == 'Rectangle':
    width = st.number_input("Width",0.0,step=0.1)
    length = st.number_input("length", 0.0, step= 0.1)
    with st.spinner("Calculating......."):
        time.sleep(1)
        area = width * length

btn = st.button("Calculate Erea")
if btn :
    st.write("Result is " , area)
#print (width)
#print(length)