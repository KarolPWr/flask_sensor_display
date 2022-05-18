import sqlite3
import math
import sys
import os
import smbus2
import bme280

sys.path.insert(1, os.path.join(sys.path[0], '..'))
import conf

bus = smbus2.SMBus(conf.I2C_PORT)


def log_temperature(temp):
    conn = sqlite3.connect(conf.DB_PATH)
    curs = conn.cursor()
    curs.execute("INSERT INTO temperature values(datetime('now', 'localtime'), (?))", (temp,))
    conn.commit()
    conn.close()


def read_temperature():
    calibration_params = bme280.load_calibration_params(bus, conf.I2C_ADDRESS)

    # the sample method will take a single reading and return a
    # compensated_reading object
    data = bme280.sample(bus, conf.I2C_ADDRESS, calibration_params)
    # the compensated_reading class has the following attributes
    print(data.id)
    print(data.timestamp)
    print(data.temperature)
    print(data.pressure)

    # there is a handy string representation too
    print(data)
    return math.floor(data.temperature * 100) / 100


if __name__ == '__main__':
    temperature = read_temperature()
    log_temperature(temperature)
