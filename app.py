import streamlit as st
import joblib
import sklearn

st.write("pressure, dewpoint, humidity, cloud, rainfall, sunshine, winddirection, windspeed")
st.title("Rainfall Prediction")
a1=st.number_input("Enter pressure : ")
a2=st.number_input("Enter dewpoint : ")
a3=st.number_input("Enter humidity : ")
a4=st.number_input("Enter cloud : ")
a5=st.number_input("Enter sunshine : ")
a6=st.number_input("Enter win-direction : ")
a7=st.number_input("Enter wind-speed : ")

model=joblib.load("model.pkl")

if st.button("Predict"):
    op=st.write(model.predict([[a1,a2,a3,a4,a5,a6,a7]]))
    if op==1:
        st.write("Rainfall is likely to occur")
    else:
        st.write("Rainfall is not likely to occur") 