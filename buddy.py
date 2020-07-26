import os
import sqlite3
import pandas as pd 
from sqlalchemy import create_engine

# Read csv into pandas DataFrame
df = pd.read_csv('buddymove_holidayiq.csv')
print(df.shape)
print(df.head())
df.rename(columns={"User Id":"UserID"}, inplace=True)
print(df.head())

conn = sqlite3.connect("buddy.db")
c = conn.cursor()
query = """CREATE TABLE users (UserID text, Sports number, 
            Religious number, Nature number,
            Theatre number, Shopping number,
            Picnic number)"""
c.execute(query)
conn.commit()


df.to_sql('users', conn, if_exists='replace', index = False)

query = """
        SELECT
            count(distinct UserID)
        FROM
            users;"""
result = c.execute(query)
conn.commit()
print(result)