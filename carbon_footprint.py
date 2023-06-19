#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

def calculate_carbon_footprint(aircraft_type, distance):
    if aircraft_type == 'a320':
        fuel_consumption_per_mile = 50.625
    elif aircraft_type == 'a321':
        fuel_consumption_per_mile = 60
    elif aircraft_type == 'b738':
        fuel_consumption_per_mile = 52.5
    elif aircraft_type == 'b777':
        fuel_consumption_per_mile = 126.25
    elif aircraft_type == 'b744':
        fuel_consumption_per_mile = 245
    elif aircraft_type == 'b763':
        fuel_consumption_per_mile = 100
    elif aircraft_type == 'a333':
        fuel_consumption_per_mile = 118.75
    elif aircraft_type == 'a380':
        fuel_consumption_per_mile = 240
    elif aircraft_type == 'an225':
        fuel_consumption_per_mile = 320
    else:
        st.error('Invalid aircraft type!')
        return

    # Conversion factor: 1 liter of fuel = X metric tons of CO2 equivalent
    conversion_factor = 2.31  # Example conversion factor, adjust as per the specific fuel

    carbon_footprint_liters = fuel_consumption_per_mile * distance

    st.success(f'Carbon Footprint: {carbon_footprint_liters} metric tons')


# Create the web app using Streamlit
def main():
    st.title('Aircraft Carbon Footprint Calculator')

    aircraft_type = st.text_input('Enter Type of Aircraft:')
    distance = st.number_input('Enter Travel distance (in miles):')

    if st.button('Calculate'):
        calculate_carbon_footprint(aircraft_type, distance)


if __name__ == '__main__':
    main()


# In[ ]:




