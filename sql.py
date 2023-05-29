import sqlite3 as sq

db=sq.connect("db.sqlite3")
print("Database connected")

db.execute("DROP DATABASE db.sqlite3")
print("Database dropped")