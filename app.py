from flask import Flask, Markup, render_template
import sqlite3
from collections import OrderedDict

app = Flask(__name__)

DBNAME = 'temperature.db'


def get_db_connection():
    conn = sqlite3.connect(DBNAME)
    conn.row_factory = sqlite3.Row
    return conn


def get_data_by_interval(interval):
    conn = get_db_connection()

    if interval is None:
        data = conn.execute("SELECT * FROM temperature").fetchall()
    else:
        data = conn.execute("SELECT * FROM temperature WHERE date>datetime('now','-%s hours')" % interval).fetchall()

    conn.close()
    return data


@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM temperature').fetchall()
    conn.close()
    return OrderedDict(posts)  # not dict, because of underlying hash map


@app.route('/line')
def line():
    data = get_data_by_interval(99999)
    db_data = OrderedDict(data)
    line_dates = db_data.keys()
    line_temperatures = db_data.values()
    return render_template('line_chart.html', title='Temperature', labels=line_dates,
                           values=line_temperatures)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)
