import sqlite3
import math
import smbus2
import bme280


PORT = 1
I2C_ADDRESS = 0x76
bus = smbus2.SMBus(PORT)
DBDIR = '/home/pi/flask_chart_test/sensor_specific/'
DBNAME = 'temperature.db'


# store the temperature in the database
def log_temperature(temp):
    conn = sqlite3.connect(DBDIR + DBNAME)
    curs = conn.cursor()
    curs.execute("INSERT INTO temperature values(datetime('now', 'localtime'), (?))", (temp,))
    # commit the changes
    conn.commit()
    conn.close()


def read_temperature():
    calibration_params = bme280.load_calibration_params(bus, I2C_ADDRESS)

    # the sample method will take a single reading and return a
    # compensated_reading object
    data = bme280.sample(bus, I2C_ADDRESS, calibration_params)
    # the compensated_reading class has the following attributes
    print(data.id)
    print(data.timestamp)
    print(data.temperature)
    print(data.pressure)

    # there is a handy string representation too
    print(data)
    return math.floor(data.temperature*100)/100


if __name__ == '__main__':
    temperature = read_temperature()
    log_temperature(temperature)
