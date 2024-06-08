import glob
from datetime import datetime
from wiggle_sensors.write import write_to_csv

def read_DS18B20(decimals=1):
    """Reads the temperature from a 1-wire device"""

    device = glob.glob("/sys/bus/w1/devices/" + "28*")[0] + "/w1_slave"

    with open(device, "r") as f:
        lines = f.readlines()
    equals_pos = lines[1].find("t=")
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2 :]
        temp = round(float(temp_string) / 1000.0, decimals)

    print("Soil temperature: %0.1f C" % (temp))

    return temp

def write_DS18B20(decimals=1):
    """Write the temperature from a 1-wire device"""

    temp = read_DS18B20(decimals)
    sensor_data = {
        "time": datetime.now().isoformat(),
        "temperature": temp
    }
    field_names = ["time", "temperature"]
    write_to_csv(sensor_data, "soil-temperature", field_names)

if __name__ == "__main__":
    read_DS18B20()
