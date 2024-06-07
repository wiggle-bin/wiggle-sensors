import time
from gpiozero import Button
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
    sensor = Button(SENSOR_PIN)

    try:
        while True:
            reading = not sensor.is_pressed
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
        print("Exiting...")


if __name__ == "__main__":
    main()
