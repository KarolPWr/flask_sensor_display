from collections import OrderedDict
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

DBNAME = '/home/pi/flask_chart_test/sensor_specific/temperature.db'


def get_db_connection():
    conn = sqlite3.connect(DBNAME)
    conn.row_factory = sqlite3.Row
    return conn


def get_data_by_interval(interval_hours):
    conn = get_db_connection()

    if interval_hours is None:
        data = conn.execute("SELECT * FROM temperature").fetchall()
    else:
        data = conn.execute(
            "SELECT * FROM temperature WHERE date>datetime('now','localtime', '-%s hours')" % interval_hours).fetchall()

    conn.close()
    return data


@app.route('/debug')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM temperature').fetchall()
    conn.close()
    return OrderedDict(posts)  # not dict, because of underlying hash map


@app.route('/temperature')
def line():
    data = get_data_by_interval(12)
    db_data = OrderedDict(data)
    line_dates = db_data.keys()
    line_temperatures = db_data.values()
    last_temperature = next(reversed(db_data.values()))
    return render_template('line_chart.html', title='Temperature', labels=line_dates,
                           values=line_temperatures, last_temperature=last_temperature)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)
