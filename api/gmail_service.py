from flask import Blueprint, request
from flask_praetorian import auth_required
import smtplib

# Gmail service module
gmail_service = Blueprint('gmail_service', __name__)


@gmail_service.route("/api/send_email", methods=['POST'])
@auth_required
def send_email():
    """Send mails from surfbetter account with user email and user password"""
    try:
        req = request.get_json(force=True)
        email = "surffbetter@gmail.com"
        password = "pestillo01"
        admin_email = "antoniojoselojoojeda@gmail.com"
        subject = req['subject']
        message = f"Subject: {subject}\n\nEmail from: {req['user_email']}\nMessage:\n{req['message']}"

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, admin_email, message)
        return {"message": "mail send success"}, 200

    except Exception as e:
        return {"Error": str(e)}, 500

    finally:
        server.quit()
