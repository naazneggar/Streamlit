import streamlit as st
import joblib 
import pandas as pd

#data=pd.read_csv("C:\\Users\\acer\\house100.csv")
#st.dataframe(data)

model1=joblib.load("model1.pkl")
model2=joblib.load("Housing_Price.pkl")

st.sidebar.title("Pages")

#page=st.sidebar.selectbox("Select Model",["PCI","HOUSE"])
page=st.sidebar.radio("Select Model",options=["PerCapitaIncome","HOUSE"])

if page=="PerCapitaIncome":
    st.title('Per capita income of canada')
    st.write('This is a simple web_app to predict the per capita income of canada')
   

    year=st.number_input('Enter the year',min_value=100)
    prediction=model1.predict([[year]])
    prediction=pd.Series(prediction[0])
    if st.button('Predict'):
        st.error(f"The per capita income of canada in the year,{year} is {prediction[0]}")
else:
    st.title('House Price Prediction')
    st.write('This is a simple web_app to predict the House price')

    sqft=st.number_input("Enter the Square feet",min_value=100)
    room=st.number_input("Enter the number of rooms",min_value=1)
    age=st.number_input("Enter the Age of House",min_value=0)


    prediction=model2.predict([[sqft,room,age]])
    if st.button('Predict'):
        st.write('The Price of the house of',sqft,room,age,'is',prediction[0])



