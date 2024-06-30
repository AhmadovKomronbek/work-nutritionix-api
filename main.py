from dotenv import load_dotenv
import requests
import os
import datetime

load_dotenv()

APP_ID = os.environ.get("ID")
API_KEY = os.environ.get("KEY")
TOKEN = os.environ.get("TOKEN")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
GENDER = "male"
WEIGHT_KG = 55
HEIGHT_CM = 160
AGE = 15

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

user_query = input("Nimani qancha qilding : ")

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

data = {
    "query": user_query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=data, headers=header)
exercise_list = response.json()["exercises"]

for data in exercise_list:
    sheety_data = {
        "sheet1": {
            "time": datetime.datetime.now().strftime("%d/%m/%Y"),
            "date": datetime.datetime.now().strftime("%M:%M:%S"),
            "exercise": data["name"].capitalize(),
            "duration": data["duration_min"],
            "calories": data["nf_calories"]
        }
    }

    sheety_headers = {
        "Authorization": f"Bearer {TOKEN}"
    }
    sheet_response = requests.post(url=f"{SHEETY_ENDPOINT}", json=sheety_data, headers=sheety_headers)
    print(sheet_response)
