# WiggleBME680

## Via CLI

Run `wiggle-bme680` to gather sensor data such as temperature, gas, pressure and humidity from bme680 sensor.

```
wiggle-bme680
```

## Install WiggleBME680 service

In the terminal run `wiggle-bme680-install`. This will install and start a service which runs `wiggle-bme680` on boot.

```
wiggle-bme680-install
```


You can check the status with:

```
systemctl --user status wiggle-bme680.service
```

To stop the service run:

```
systemctl --user stop wiggle-bme680.service
```

To start the service run:

```
systemctl --user start wiggle-bme680.service
```

## Installation for development

Updating packages on Raspberry Pi
```
pip install --upgrade pip setuptools wheel
python -m pip install --upgrade pip
apt-get install libjpeg-dev zlib1g-dev
```

Installing package
```
pip3 install -e .
```

For installation without dev dependencies
```
pip install --no-dev -r requirements.txt
```