import streamlit as st
import pickle

st.set_page_config(page_title='salary-predictor', page_icon="💸")
st.header("Salary-Predictor")

with open ("model.pkl", "rb") as file:
    model = pickle.load(file)


yoe = st.number_input('Years of Experience', min_value= 0.0, max_value= 10.0, step =0.5, value= 2.0)

if st.button("Predict"):
    prediction = model.predict([[yoe]])
    st.success(prediction)

