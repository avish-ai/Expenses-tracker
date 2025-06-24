import pywhatkit

sender_email = "your_email@gmail.com"
sender_password = "your_app_password"  # Use app password if 2FA is on
receiver_email = "receiver_email@example.com"
subject = "Test Email from pywhatkit"
message = "Hello, this is a test email sent using pywhatkit!"

# Send the email
pywhatkit.send_mail(
    sender_email,
    sender_password,
    subject,
    message,
    receiver_email
)

print("Email sent successfully!")
