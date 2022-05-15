import sqlite3

connection = sqlite3.connect('temperature.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO temperature (date, temperature) VALUES (?, ?)",
            ('2022-05-13 12:12:13.000', 22.3)
            )

cur.execute("INSERT INTO pressure (date, pressure) VALUES (?, ?)",
            ('2022-05-13 12:12:13.000', 1013)
            )

connection.commit()
connection.close()
