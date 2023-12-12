import requests
import sqlite3
import datetime
import asyncio
import pandas as pd
import matplotlib.pyplot as plt

async def wait_60_seconds():
    print("Waiting for 60 seconds...")
    await asyncio.sleep(60)
    print("60 seconds have passed. Now executing the code.")
    # Your code goes here



DATABASE = 'database.db'
API_URL = 'https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi'

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS data (
                    id INTEGER PRIMARY KEY,
                    factor INTEGER,
                    pi REAL,
                    time TEXT)''')
conn.commit()

def fetch_and_store():

    try:
        response = requests.get(API_URL)
        data = response.json()

        cursor.execute('INSERT INTO data (factor, pi, time) VALUES (?, ?, ?)',
                       (data['factor'], data['pi'], data['time']))
        print(data['factor'], data['pi'], data['time'])
        conn.commit()
        asyncio.run(wait_60_seconds())

    except Exception as e:
        print("Error:", e)

def main():
    iterations = 0
    while iterations < 60:
        fetch_and_store()
        iterations += 1

if __name__ == "__main__":
    main()

conn.close()
