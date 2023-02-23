import streamlit as st

# Define a function to calculate carbon footprint
def calculate_carbon_footprint(carbon_per_mile, miles_per_week, miles_per_gallon, price_per_gallon):
    # Calculate total carbon emissions in pounds per year
    carbon_emissions = carbon_per_mile * miles_per_week * 52
    # Calculate total fuel cost per year
    fuel_cost = miles_per_week * 52 / miles_per_gallon * price_per_gallon
    # Return results
    return carbon_emissions, fuel_cost

# Create a title and description for the app
st.title("Carbon Footprint Monitor")
st.write("This app helps you monitor your carbon footprint and fuel costs based on your weekly driving habits.")

# Create input fields for user data
carbon_per_mile = st.slider("Carbon emissions per mile (in pounds)", 0, 5, 1)
miles_per_week = st.slider("Miles driven per week", 0, 1000, 50)
miles_per_gallon = st.slider("Miles per gallon of your vehicle", 0, 50, 25)
price_per_gallon = st.slider("Price per gallon of fuel", 0.0, 5.0, 2.5)

# Calculate and display results
carbon_emissions, fuel_cost = calculate_carbon_footprint(carbon_per_mile, miles_per_week, miles_per_gallon, price_per_gallon)
st.write("Your estimated carbon footprint per year is", carbon_emissions, "pounds.")
st.write("Your estimated fuel cost per year is", fuel_cost, "dollars.")
