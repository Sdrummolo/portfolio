from flask import Flask, render_template, request
from flask_mail import Mail, Message
from os import environ

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = environ.get('MAIL_USERNAME')
app.config['MAIL_MAX_EMAILS'] = None
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Extract data from form
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # Send formatted email
        msg = Message("New message from portfolio submission!",
                      recipients=[environ.get('MAIL_USERNAME')])
        msg.html = f"<b>Name:</b> {name}<br><b>Email:</b> {email}<br><br>{message}"
        mail.send(msg)

    return render_template("index.html")
