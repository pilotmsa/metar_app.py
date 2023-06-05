import streamlit as st

def get_metar(icao_code, Date_Time, temperature, wind_speed, visibility):
    metar = f"METAR {icao_code} {Date_Time} {temperature} {wind_speed} {visibility}"
    return metar

# Streamlit UI
st.title("METAR Report Generator")

# User input
icao_code = st.text_input("Enter the ICAO code:")
Date_Time = st.text_input("Enter Date and Time (dhms)z:")
temperature = st.text_input("Enter the temperature (c):")
wind_direction = st.text_input("Enter wind direction:")
wind_speed = st.text_input("Enter the wind speed (kt):")
visibility = st.text_input("Enter the visibility (km):")

# Generate and display the METAR
if st.button("Submit"):
    metar_report = get_metar(icao_code, Date_Time, temperature, wind_speed, visibility)
    st.header("METAR Report:")
    st.write(metar_report)
