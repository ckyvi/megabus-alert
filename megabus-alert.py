"""
Date: 2024 06-10
Author: Vicky

This program is a Megabus tracker created with the purpose of sending alerts when 
the dates of certain routes are available. 

"""

import requests
import smtplib
import os

TARGET_DATE = "2026-10-14"

def get_dates():
    url = "https://ca.megabus.com/journey-planner/api/journeys/travel-dates"

    params = {
        "originCityId": 276,
        "destinationCityId": 145
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data["availableDates"]

def send_email():
    sender = "itzvickylin@gmail.com"
    app_password = os.environ["EMAIL_APP_PASSWORD"]
    receiver = "itzvicky@gmail.com"

    subject = "Megabus Alert"
    body = f"{TARGET_DATE} is now available!"

    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, app_password)
        server.sendmail(sender, receiver, message)

def main():
    dates = get_dates()

    if TARGET_DATE in dates:
        print("FOUND!")
        send_email()
    else:
        print("Not available yet")

if __name__ == "__main__":
    main()
    exit()
else:
    print("Not available yet")
