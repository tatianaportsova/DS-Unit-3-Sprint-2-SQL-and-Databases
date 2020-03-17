# module1-introduction-to-sql/assignment/buddymove_holidayiq.py

import os
import sqlite3
import pandas
from sqlalchemy import create_engine

#engine = create_engine('sqlite://', echo=False)
df = pandas.read_csv("/Users/tt.sova/Desktop/buddymove_holidayiq.csv")
conn = sqlite3.connect("../buddymove_holidayiq.sqlite3")
curs = conn.cursor()
df.to_sql('users', conn, if_exists='replace',
           index=False)
#engine.execute("SELECT * FROM users").fetchall()