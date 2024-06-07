from wiggle_sensors.environment import write_bme680
from wiggle_sensors.soil_temperature import write_DS18B20

def main():
    write_bme680()
    write_DS18B20()

if __name__ == "__main__":
    main()