from flask import Flask, Markup, render_template
import sqlite3
from collections import OrderedDict

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('temperature.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM temperature').fetchall()
    conn.close()
    return OrderedDict(posts)  # not dict, because of underlying hash map


@app.route('/line')
def line():
    conn = get_db_connection()
    db_data = conn.execute('SELECT * FROM temperature').fetchall()
    conn.close()
    db_data = OrderedDict(db_data)
    line_dates = db_data.keys()
    line_temperatures = db_data.values()
    return render_template('line_chart.html', title='Temperature', labels=line_dates,
                           values=line_temperatures)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)
