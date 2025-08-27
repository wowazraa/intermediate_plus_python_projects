import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import EMAIL_ADDRESS, EMAIL_PASSWORD, SMTP_SERVER, SMTP_PORT

def send_emails(emails, subject, message, is_html=True):
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for email in emails:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = email
        msg['Subject'] = subject

        if is_html:
            html_content = f"""
            <html>
                <body style="font-family: Arial, sans-serif; line-height: 1.6;">
                    <h2 style="color: #2E86C1;">New Flight Deal!</h2>
                    <p>{message}</p>
                    <hr>
                    <p style="font-size: 0.9em; color: #555;">This is an automated notification from Flight Club.</p>
                </body>
            </html>
            """
            msg.attach(MIMEText(html_content, 'html'))
        else:
            msg.attach(MIMEText(message, 'plain'))

        server.sendmail(EMAIL_ADDRESS, email, msg.as_string())

    server.quit()
