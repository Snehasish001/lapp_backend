import pandas as pd
import requests
from datetime import datetime

# -------- CONFIG --------
API_URL = "http://127.0.0.1:8000//api/singapore/last-digit/"
EXCEL_FILE = "single_digit.xlsx"
# ------------------------

headers = {
    "Content-Type": "application/json",
}

df = pd.read_excel(EXCEL_FILE)

for _, row in df.iterrows():
    payload = {
        "date": row["DATE"].date().isoformat(),
        "mor": str(row["MOR"]),
        "day": str(row["DAY"]),
        "evn": str(row["EVN"]),
    }

    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code in (200, 201):
        print(f"✔ Sent {payload['date']}")
    else:
        print(f"✖ Failed {payload['date']} → {response.status_code}")
        print(response.text)
