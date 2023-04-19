# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


# Define Verify_otp() function
@app.route('/login' , methods=['POST'])
def verify_otp():
    username = request.form['username']
    password = request.form['password']
    mobile_number = request.form['number']

    if username == 'verify' and password == '12345':   
        account_sid = 'AC9982325d9ee7525b5b49067a22ff2bec'
        auth_token = '2f6a700eaffbc7fc1dbfc47d4a767478'
        client = Client(account_sid, auth_token)
        verification = client.verify \
            .services('VA04d5fe03d26fd85d6099c6a7e15b48a7') \
            .verifications \
            .create(to=mobile_number, channel='sms')

        print(verification.status)
        return render_template('otp_verify.html')
    else:
        return render_template('user_error.html')



@app.route('/otp' , methods=['POST'])
def get_otp():
    print("Processing")
    received_otp = request.form['received_otp']
    mobile_number = request.form['number']
    account_sid = "AC9982325d9ee7525b5b49067a22ff2bec"
    auth_token = "2f6a700eaffbc7fc1dbfc47d4a767478"
    client = Client(account_sid , auth_token)
    verification_check = client.verify \
        .services('VA04d5fe03d26fd85d6099c6a7e15b48a7') \
        .verification_checks \
        .create(to=mobile_number, code=received_otp)
    if verification_check.status == "pending":
        return "Entered OTP is wrong"
    else:
        return redirect("https://cdcoladocu.onrender.com/")

   

if __name__ == "__main__":
    app.run()

