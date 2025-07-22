from flask import Flask, render_template, request, flash, redirect, url_for
import os
from dotenv import load_dotenv
import traceback
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-here')

# Email Configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'ranjan1497chaurasiya@gmail.com'
SENDER_PASSWORD = 'utqy slfn stnm cnxh'

SENDGRID_API_KEY = "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"
TO_EMAIL = "ranjan1497chaurasiya@gmail.com"  # Your verified sender email

def send_email(subject, body, to_email):
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = to_email
        msg['Subject'] = subject

        # Add body
        msg.attach(MIMEText(body, 'plain'))

        # Create SMTP session
        print("\nConnecting to SMTP server...")
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        
        print("Logging in...")
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        
        print("Sending email...")
        text = msg.as_string()
        server.sendmail(SENDER_EMAIL, to_email, text)
        
        print("Closing connection...")
        server.quit()
        
        print("Email sent successfully!")
        return True
        
    except Exception as e:
        print(f"\nError sending email: {str(e)}")
        print("\nFull traceback:")
        print(traceback.format_exc())
        return False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/certifications')
def certifications():
    return render_template('certifications.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        print("Contact form POST received")
        print("Form data:", request.form)
        name = request.form.get('name', '')
        email = request.form.get('email', '')
        subject = request.form.get('subject', '')
        message = request.form.get('message', '')

        # Compose the email
        email_subject = f"Portfolio Contact: {subject} (from {name}, {email})"
        email_body = f"""
You have received a new message from your portfolio contact form.

Name: {name}
Email: {email}

Message:
{message}
"""

        print("SENDGRID_API_KEY:", SENDGRID_API_KEY)
        print("Email subject:", email_subject)
        print("Email body:", email_body)

        try:
            sg = SendGridAPIClient(SENDGRID_API_KEY)
            mail = Mail(
                from_email=TO_EMAIL,
                to_emails=TO_EMAIL,
                subject=email_subject,
                plain_text_content=email_body
            )
            response = sg.send(mail)
            print(f"SendGrid response: {response.status_code}")
            flash('Thank you for your message! I will get back to you soon.', 'success')
        except Exception as e:
            print(f"SendGrid error: {e}")
            flash('Sorry, there was an error sending your message. Please try again later.', 'danger')

        return redirect(url_for('contact'))

    return render_template('contact.html')

@app.route('/test_email')
def test_email():
    subject = "Test Email from Portfolio"
    body = "This is a test email to verify the email configuration is working."
    
    if send_email(subject, body, SENDER_EMAIL):
        return "Test email sent successfully! Please check your inbox and spam folder."
    else:
        return "Error sending test email. Check the console for details."

@app.route('/sendgridtest')
def sendgridtest():
    print("SENDGRID_API_KEY:", SENDGRID_API_KEY)
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    mail = Mail(
        from_email=TO_EMAIL,
        to_emails=TO_EMAIL,
        subject="SendGrid Flask Route Test",
        plain_text_content="This is a test from the /sendgridtest route."
    )
    response = sg.send(mail)
    print(f"SendGrid response: {response.status_code}")
    return "Test email sent from /sendgridtest"

if __name__ == '__main__':
    app.run(debug=True, port=5500) 