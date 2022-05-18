import pathlib

DBNAME = 'temperature.db'
DBDIR = pathlib.Path(__file__).parent.resolve()
I2C_ADDRESS = 0x76
I2C_PORT = 1

DB_PATH = pathlib.Path.joinpath(DBDIR, DBNAME)
