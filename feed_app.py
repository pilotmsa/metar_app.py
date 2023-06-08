import streamlit as st
import smtplib

def main():
    st.title("Space Weather Impacts on GNSS and Remote Sensing")

    # Collecting user input
    feedback = st.text_area("Provide your feedback on the lecture:")

    # Submit button
    if st.button("Submit"):
        # Process the feedback
        process_feedback(feedback)
        send_email(feedback)
        st.success("Thank you for your feedback! An email has been sent.")

def process_feedback(feedback):
    # In this function, you can write code to process and save the feedback
    # For example, you can store it in a database or write it to a file
    # You can also perform any analysis or computations on the feedback data

    # For demonstration purposes, let's simply print the feedback
    print(f"Feedback: {feedback}")

def send_email(feedback):
    # Configure your email settings
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "mahnoudsayed32@gmail.com"
    sender_password = "Msa-123456"
    recipient_email = "mahmoudsayed32@hotmail.com"

    # Create the email message
    subject = "Lecture Feedback"
    body = f"Feedback received:\n\n{feedback}"
    message = f"Subject: {subject}\n\n{body}"

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Log in to your email account
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, message)

    except Exception as e:
        print(f"An error occurred while sending the email: {str(e)}")

    finally:
        # Close the connection to the SMTP server
        server.quit()

if __name__ == "__main__":
    main()

