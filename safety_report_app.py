#!/usr/bin/env python
# coding: utf-8

import smtplib
import streamlit as st

# Function to generate safety report based on user input
def generate_safety_report(user_input):
    # Perform safety analysis based on user input
    # ...
    # Your code for safety analysis goes here
    # ...

    # Generate safety report
    safety_report = "Safety Report\n\n"
    safety_report += "==================================\n"
    safety_report += "Summary of Safety Analysis:\n"
    safety_report += "==================================\n"
    # Include relevant information from the safety analysis results
    # ...

    # Add recommendations or actions to be taken
    safety_report += "\nRecommendations:\n"
    # ...

    # Add conclusion or final remarks
    safety_report += "\nConclusion:\n"
    # ...

    return safety_report

# Function to send email
def send_email(subject, body, recipient):
    # Set up SMTP server
    # Set up SMTP server and port for Gmail
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    sender_email = "mahnoudsayed32@gmail.com"
    sender_password = "Msa-123456"

    # Create email message
    message = f"Subject: {subject}\n\n{body}"

    try:
        # Connect to SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Log in to sender email account
        server.login(sender_email, sender_password)

        # Send email
        server.sendmail(sender_email, recipient, message)

        st.success("Safety report sent successfully.")

    except Exception as e:
        st.error(f"Failed to send safety report. Error: {str(e)}")

    finally:
        # Close the SMTP server connection
        server.quit()

# Streamlit web app
def main():
    # Set page title
    st.title("Aviation Safety Report Generator (NASMC) National Air Space Management Center")

    # Get user input
    position = st.text_input("Enter your position")
    user_input = st.text_area("Enter details for safety analysis:")
    recipient = st.text_input("Enter recipient email address")

    # Generate safety report based on user input
    if st.button("Submit Report"):
        report = generate_safety_report(user_input)

        # Display the safety report
        st.text(report)

        # Save the safety report to a file
        with open("safety_report.txt", "w") as file:
            file.write(report)

        # Send safety report via email
        if recipient:
            send_email("Aviation Safety Report", report, recipient)
        else:
            st.warning("Please enter a recipient email address.")

# Run the app
if __name__ == "__main__":
    main()
