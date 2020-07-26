import os
import sqlite3
from sqlalchemy import create_engine


conn = sqlite3.connect("buddy.db")
c = conn.cursor()
# Get row count from new sqlite3 table
t1 = "Table rows number: "
q1 = """
        SELECT
            count(distinct UserID)
        FROM
            users;"""
r1 = c.execute(q1).fetchall()
conn.commit()
print(t1, r1[0])

''' How many users who reviewed at least 100 Nature 
    in the category also reviewed at least 100 in the 
    Shopping category?'''

t2 = "Users that reviewed at least 100 Nature and Shopping: "
q2 = """
        SELECT
            count(distinct UserID)
        FROM
            users
        WHERE Nature > 99
        AND Shopping > 99;"""
r2 = c.execute(q2).fetchall()
conn.commit()
print(t2, r2[0])

t3 = "Genre averages are: "
q3 = """
        SELECT
            round(AVG(Sports),2)
            ,round(AVG(Religious),2)
            ,round(AVG(Nature),2)
            ,round(AVG(Theatre),2)
            ,round(AVG(Shopping),2)
            ,round(AVG(Picnic),2)
        FROM
            users;"""
r3 = c.execute(q3).fetchall()
conn.commit

r = r3[0]
print('Average number of Sports reviewed: ', r[0])
print('Average number of Religious reviewed: ', r[1])
print('Average number of Nature reviewed: ', r[2])
print('Average number of Theatre reviewed: ', r[3])
print('Average number of Shopping reviewed: ', r[4])
print('Average number of Picnic reviewed: ', r[5])

