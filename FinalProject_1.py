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



# Constants
DATABASE = 'data_project.db'
API_URL = 'https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi'

# Create/connect to a SQLite database
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS data (
                    id INTEGER PRIMARY KEY,
                    factor INTEGER,
                    pi REAL,
                    time TEXT)''')
conn.commit()

def fetch_and_store():

    try:
        # Fetch data from API
        response = requests.get(API_URL)
        data = response.json()

        # Insert data into the database
        cursor.execute('INSERT INTO data (factor, pi, time) VALUES (?, ?, ?)',
                       (data['factor'], data['pi'], data['time']))
        print(data['factor'], data['pi'], data['time'])
        conn.commit()
        asyncio.run(wait_60_seconds())

    except Exception as e:
        print("Error:", e)

def main():
    # iterations = 0
    # while iterations < 60:
    #     fetch_and_store()
    #     iterations += 1
    # For data analysis, you can add your code here or in a separate script
    df = pd.read_sql_query("SELECT * FROM data", conn)
    print(df)
    df.plot(x='factor', y='pi', kind='scatter')	
    plt.show()

if __name__ == "__main__":
    main()

# Close the database connection
conn.close()
