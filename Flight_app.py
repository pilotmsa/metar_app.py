import streamlit as st
from dataclasses import dataclass

@dataclass
class FlightPlan:
    Massage_type: str
    aircraft_id: str
    flight_rules: str
    flight_type: str
    number_of_aircraft: int
    aircraft_type: str
    wake_turbulence: str
    Equipment: str
    departure_aerodrome: str
    departure_time: str
    speed: str
    Cruising_Level: str
    Route: str
    destination_aerodrome: str
    EET: str
    Alternate_aerodrome: str
    ITems_18: str

def app():
    st.title("Flight Plan By NASMC (National Air space Management Center)")

    Massage_type = st.text_input('Enter Message type (FPL/CNL/CHG/DEL): ')
    aircraft_id = st.text_input("Enter Aircraft ID: ")
    flight_rules = st.text_input("Enter Flight Rules (I/v/y/z): ")
    flight_type = st.text_input("Enter Type of Flight (S/N/M/G/X): ")
    number_of_aircraft = st.text_input("Enter Number of Aircraft: ")
    aircraft_type = st.text_input("Enter Aircraft Type (e.g., B738, A320): ")
    wake_turbulence = st.text_input('Enter Wake Turbulence Category of Aircraft:  ')
    Equipment = st.text_input('Enter Equipment: ')
    departure_aerodrome = st.text_input("Enter Departure Aerodrome: ")
    departure_time = st.text_input("Enter Departure Time (UTC): ")
    speed = st.text_input('Enter Aircraft Speed: ')
    Cruising_Level = st.text_input('Enter Cruising Level: ')
    Route = st.text_input("Enter Flight Route: ")
    destination_aerodrome = st.text_input("Enter Destination Aerodrome: ")
    EET = st.text_input("Enter Estimated Elapsed Time (EET): ")
    Alternate_aerodrome = st.text_input("Enter Alternate Aerodrome: ")
    ITems_18 = st.text_input('Enter Any Other Information: ')
    
    if st.button('Submit'):
        flight_plan = FlightPlan(Massage_type, aircraft_id, flight_rules, flight_type, number_of_aircraft, aircraft_type, wake_turbulence, Equipment, departure_aerodrome, departure_time, speed, Cruising_Level, Route, destination_aerodrome, EET, Alternate_aerodrome, ITems_18)
        st.write(flight_plan)

if __name__ == "__main__":
    app()



