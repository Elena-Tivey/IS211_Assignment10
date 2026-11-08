import sqlite3

conn = sqlite3.connect("music.db")   # this creates the database
conn.executescript(open("music.sql").read())   # this creates the tables
conn.commit()
conn.close()