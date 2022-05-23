# Web interface for Raspberry Pi temperature monitor

Software: Flask + Chart.js + SQLite + systemd

Hardware: Raspberry Pi + BME280

Sample chart with temperature measured in the last 12 hours:

![Alt text](chart.png?raw=true "Optional Title")

## Software setup

Clone repository to your Raspberry:

    git clone https://github.com/KarolPWr/flask_sensor_display.git

For stable version, checkout the latest tag:

    git checkout tags/v1.0.0

Install required python packages:

    pip3 install -r requirements.txt

Run install.sh script:

    bash install.sh 

Run the web server (default on localhost:9999)

    python app.py

To uninstall running project files execute:

    bash uninstall.sh

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

Remember to enable i2c via `raspi-config`

To confirm what address your sensor has, connect it to Raspberry and run command:

    i2cscan -y <BUS>

Bus in my case was number 1, it could also be 0 or 2. Try different combinations 

## Development 

I normally develop application on desktop and deploy application to Raspberry remotely. To facilitate that, you can use helper script:

    bash deploy_to_rpi.sh -i <RASPBERRY_IP> -d <DESTINATION_PATH>

Which will copy project files to specified folder on Raspberry, kill running python app and run the webserver. 

### Using different sensor 

To use different sensor than I, you only need to re-implement sensor reading function `read_temperature()` in `sensor_getter.py` 
and test if data is correctly written do database (DATE:REAL)

*Note:* When using BMP280, I2C address will probably be 0x77

### Configuration

Constants are defined in `conf.py` file. If you want to change i.e. sensor's I2C address or database location, you change 
them in config file it will be automatically recognized by implicated files. 


