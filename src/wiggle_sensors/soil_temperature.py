import os
import glob
from datetime import datetime
import csv
from pathlib import Path

BASE_FOLDER = Path.home() / "WiggleBin"
DATA_FOLDER = BASE_FOLDER / "sensor-data"
DATA_FILE = DATA_FOLDER / "soil-temperature.csv"

def create_directory():
    os.makedirs(DATA_FOLDER, exist_ok=True)

create_directory()

def write_DS18B20(decimals=1):
    """Reads the temperature from a 1-wire device"""

    device = glob.glob("/sys/bus/w1/devices/" + "28*")[0] + "/w1_slave"

    with open(device, "r") as f:
        lines = f.readlines()
    equals_pos = lines[1].find("t=")
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2 :]
        temp = round(float(temp_string) / 1000.0, decimals)

    print("Soil temperature: %0.1f C" % (temp))

    sensor_data = [{"time": datetime.now().isoformat(), "temperature": temp}]

    with open(DATA_FILE, "a", newline="") as csvfile:
        # Specify the field names
        fieldnames = ["time", "temperature"]

        # Create a CSV writer object
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header
        if os.stat(DATA_FILE).st_size == 0:
            writer.writeheader()

        # Write the sensor data
        for data in sensor_data:
            writer.writerow(data)


if __name__ == "__main__":
    write_DS18B20()
