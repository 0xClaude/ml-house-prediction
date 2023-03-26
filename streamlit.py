import streamlit as st
import joblib
import matplotlib.pyplot as plt
import pandas as pd
import locale

# Set up locale for displaying the price in euros
locale.setlocale(locale.LC_ALL, "de_DE")

# Load the model
model = joblib.load("regression.joblib")

# Set up the app
st.title("Predict house value")
st.write("Predict the value of your house:")

# Get user input
size = st.number_input("Size of the house in square meters:", step=1, value=100)
nb = st.number_input("Number of rooms: ", step=1, value=3)
garden = st.checkbox("Garden?")
orientation = st.selectbox("What is the orientation of the house?", ("Nord", "East", "South", "West"))

# Initial values
Orientation_Nord = 0
Orientation_Est = 0
Orientation_Sud = 0
Orientation_Ouest = 0

# Modify values according to user input
if (orientation == "Nord"):
    Orientation_Nord = 1
elif (orientation == "East"):
    Orientation_Est = 1
elif (orientation == "South"):
    Orientation_Sud = 1
else:
    Orientation_Ouest = 1

# Use model to predict price
price_prediction = float(model.predict([[size, nb, garden, Orientation_Est, Orientation_Nord, Orientation_Ouest, Orientation_Sud]]))

# Transform price
euro_price = locale.currency(price_prediction, grouping=True)

# Display the price
st.write("Your price should be", euro_price)
