import streamlit as st

def calculate_capacity(control_availability, duration_time_in_sector, number_of_communications, mean_duration_of_each_message):
    # Calculate sector capacity
    airspace_capacity = (control_availability / 100) * (duration_time_in_sector) / (number_of_communications * mean_duration_of_each_message)
    sector_capacity = airspace_capacity + (3600 * control_availability / 100) / (number_of_communications * mean_duration_of_each_message)
    return airspace_capacity, sector_capacity

# Create the Streamlit app
def main():
    st.title("Sector Capacity Calculator By NASMC")

    # Take input from the user
    control_availability = st.number_input('Enter the control availability (%): ')
    duration_time_in_sector = st.number_input('Enter duration time in sector (in seconds): ')
    number_of_communications = st.number_input('Enter number of communications (per second): ')
    mean_duration_of_each_message = st.number_input('Enter mean duration of each message (in seconds): ')

    # Calculate sector capacity
    if st.button("Calculate"):
        airspace_capacity, sector_capacity = calculate_capacity(control_availability, duration_time_in_sector, number_of_communications, mean_duration_of_each_message)

        # Print the results
        st.write("Airspace capacity:", airspace_capacity)
        st.write("Sector capacity:", sector_capacity)

if __name__ == '__main__':
    main()
