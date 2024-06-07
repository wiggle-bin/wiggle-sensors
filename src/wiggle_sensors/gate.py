import time
import RPi.GPIO as GPIO
import csv
from datetime import datetime
from pathlib import Path
import os

BASE_FOLDER = Path.home() / "WiggleBin"
DATA_FOLDER = BASE_FOLDER / "sensor-data"
DATA_FILE = DATA_FOLDER / "wiggle-gate.csv"

SENSOR_PIN = 17

def create_directory():
    os.makedirs(DATA_FOLDER, exist_ok=True)

create_directory()

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SENSOR_PIN, GPIO.IN)

    try:
        while True:
            reading = GPIO.input(SENSOR_PIN)
            now = datetime.now().isoformat()

            sensor_data = [
                {
                    "time": datetime.now().isoformat(),
                    "status": reading,
                }
            ]

            if reading:
                print(f"Wiggle detected! {now}")

                with open(DATA_FILE, "a", newline="") as csvfile:
                    # Specify the field names
                    fieldnames = ["time", "status"]

                    # Create a CSV writer object
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                    # Write the header
                    if os.stat(DATA_FILE).st_size == 0:
                        writer.writeheader()

                    # Write the sensor data
                    for data in sensor_data:
                        writer.writerow(data)

            time.sleep(0.5)
    except KeyboardInterrupt:
        GPIO.cleanup()  # clean up GPIO on CTRL+C exit


if __name__ == "__main__":
    main()
