#!/usr/bin/env python
# coding: utf-8

# In[12]:


import streamlit as st

def get_metar(icao_code, Date_Time, temperature, wind_speed, visibility):
    metar = f"METAR {icao_code} {Date_Time} {temperature} {wind_speed} {visibility}"
    return metar

# Streamlit UI
st.title("METAR Report Generator")

# User input
icao_code = st.text_input("Enter the ICAO code:")
Date_Time = st.text_input("Enter Date and Time (dhms)z:")
temperature = st.text_input("Enter the temperature:")
wind_direction = st.text_input("Enter wind direction:")
wind_speed = st.text_input("Enter the wind speed:")
visibility = st.text_input("Enter the visibility:")

# Generate and display the METAR
if st.button("Generate METAR Report"):
    metar_report = get_metar(icao_code, Date_Time, temperature, wind_speed, visibility)
    st.header("METAR Report:")
    st.write(metar_report)



# In[15]:


streamlit run metar_app.py


# In[6]:


import streamlit as st

def convert_celsius_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit.

    Args:
        celsius: Temperature in Celsius.

    Returns:
        Temperature in Fahrenheit.
    """
    return (celsius * 9/5) + 32

def convert_fahrenheit_to_celsius(fahrenheit):
    """Converts temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit: Temperature in Fahrenheit.

    Returns:
        Temperature in Celsius.
    """
    return (fahrenheit - 32) * 5/9

def main():
    st.title("Temperature Converter")

    conversion_type = st.selectbox(
        "Select conversion type:",
        ("Celsius to Fahrenheit", "Fahrenheit to Celsius")
    )

    if conversion_type == "Celsius to Fahrenheit":
        celsius = st.number_input("Enter temperature in Celsius:", value=0.0)
        fahrenheit = convert_celsius_to_fahrenheit(celsius)
        st.write(f"Temperature in Fahrenheit: {fahrenheit:.2f}°F")

    elif conversion_type == "Fahrenheit to Celsius":
        fahrenheit = st.number_input("Enter temperature in Fahrenheit:", value=0.0)
        celsius = convert_fahrenheit_to_celsius(fahrenheit)
        st.write(f"Temperature in Celsius: {celsius:.2f}°C")

if __name__ == "__main__":
    main()


# In[11]:


streamlit.run app.py


# In[ ]:


streamlit hello


# In[ ]:




