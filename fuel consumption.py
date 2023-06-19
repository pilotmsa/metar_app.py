#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

def calculate_fuel_consumption(aircraft, distance):
    """Calculates the fuel consumption of an aircraft for a given distance.

    Args:
        aircraft: The type of aircraft.
        distance: The distance in nautical miles.

    Returns:
        The fuel consumption in liters.
    """

    fuel_consumption = {
        "A320": 2.5,
        "B738": 3.0,
        "B739": 3.0,
        "A380": 4.0,
        "A321": 2.7,
        "B777": 3.5,
        "B789": 3.2,
    }

    if aircraft not in fuel_consumption:
        raise ValueError("Invalid aircraft model.")

    return fuel_consumption[aircraft] * distance


def convert_liters_to_price(liters, fuel_price):
    """Converts liters of fuel to a price.

    Args:
        liters: The number of liters of fuel.
        fuel_price: The price per liter of fuel.

    Returns:
        The price of the fuel in dollars.
    """

    return liters * fuel_price


# Create the web app using Streamlit
def main():
    st.title('Aircraft Fuel Consumption and Cost Calculator')

    aircraft_model = st.selectbox('Select aircraft model:', [
        "A320",
        "B738",
        "B739",
        "A380",
        "A321",
        "B777",
        "B789"
    ])

    distance = st.number_input('Enter distance (in nautical miles):')

    fuel_price = st.number_input('Enter fuel price (per liter):')

    if st.button('Calculate'):
        try:
            fuel = calculate_fuel_consumption(aircraft_model, distance)
            cost = convert_liters_to_price(fuel, fuel_price)
            st.success(f"Fuel consumption: {fuel} liters")
            st.success(f"Fuel cost: {cost} $")
        except ValueError as e:
            st.error(str(e))


if __name__ == '__main__':
    main()

