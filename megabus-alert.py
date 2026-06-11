"""
Date: 2026 06-10
Author: Vicky

This program is a Megabus tracker created with the purpose of sending alerts when 
the dates of certain routes are available. 
"""

import requests
import smtplib
import os

# My target date that I want tickets for
TARGET_DATE = "2026-09-08"  # CHANGED to a date that IS available

def get_dates():
    url = "https://ca.megabus.com/journey-planner/api/journeys/travel-dates"

    params = {
        "originCityId": 276, # Toronto 
        "destinationCityId": 145 # Kingston (or Montreal - we need to verify)
    }

    response = requests.get(url, params=params)
    data = response.json()
    return data["availableDates"]

def send_email():
    try:
        print("Sending email...")
        sender = "itzvickylin@gmail.com"
        app_password = os.environ.get("EMAIL_APP_PASSWORD")
        receiver = "itzvicky@gmail.com"
        
        if not app_password:
            print("ERROR: No password found!")
            return
            
        subject = "Megabus Alert"
        body = f"{TARGET_DATE} is now available!"
        message = f"Subject: {subject}\n\n{body}"
        
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender, app_password)
            server.sendmail(sender, receiver, message)
            
        print("Email sent successfully!")
    except Exception as e:
        print(f"Email error: {e}")

def main():
    dates = get_dates()
    
    if TARGET_DATE in dates:
        print("FOUND!")
        send_email()
    else:
        print(f"{TARGET_DATE} not available yet")

if __name__ == "__main__":
    main()
