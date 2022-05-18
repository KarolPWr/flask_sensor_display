# Web interface for Raspberry Pi temperature monitor

Software: Flask + Chart.js + SQLite + systemd

Hardware: Raspberry Pi + BME280

Sample chart with temperature measured in the last 6 hours:

![Alt text](chart.png?raw=true "Optional Title")

## Software setup

Clone repository to your Raspberry:

    git clone https://github.com/KarolPWr/flask_sensor_display.git

Install required python packages:

    pip3 install -r requirements.txt

Run install.sh script:

    bash install.sh 

Run the web server (default on localhost:9999)

    python app.py 

## Hardware setup 

I use Raspberry Pi Zero with Wifi and BME280 sensor. Since different versions of Raspberry are usually compatible when
it comes to GPIO and OS it should also work for other boards.

| RPi                  | BME280 |
|----------------------|--------|
| SCL (GPIO 3)         | SCL    |
| SDA (GPIO 2)         | SDA    |
| 3v3 (GPIO 1)         | VCC    |
| GND (any ground pin) | GND    |

If you have version of BME that has CSB and SDO pins, it is not necessary to connect them. However, sometimes due to
different board versions I2C addresses can get mixed up. 

To confirm what address your sensor has, connect it to Raspberry and run command:

    i2cscan -y <BUS>

Bus in my case was number 1, it could also be 0 or 2. Try different combinations 


