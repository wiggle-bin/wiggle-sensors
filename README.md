# WiggleSensors

## Preparing Raspberry Pi

### For soil temperature - ds18b20

You will need to enable the Raspberry PI to gather ds18b20 data

https://raspberrytips.nl/ds18b20-raspberry-pi/

## Via CLI

Run `wiggle-sensors -h` to see options for viewing sensor data such as temperature, gas, pressure and humidity from bme680 and DS18B20 sensor.

```
wiggle-sensors -h
```

## Installation for development

Installing package
```
pip3 install .
```

For installation without dev dependencies
```
pip install --no-dev -r requirements.txt
```