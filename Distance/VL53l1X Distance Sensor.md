# VL53l1X Distance Sensor

Python library for the VL53L1X Laser Ranger

## Install

```
$ sudo pip install smbus2
$ sudo pip install vl53l1x
```

## Usage

```python
import VL53L1X

tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
tof.open() # Initialise the i2c bus and configure the sensor
tof.start_ranging(1) # Start ranging, 1 = Short Range, 2 = Medium Range, 3 = Long Range
distance_in_mm = tof.get_distance() # Grab the range in mm
tof.stop_ranging() # Stop ranging
```



## GPIO

![raspberry pi gpio에 대한 이미지 검색결과](https://t1.daumcdn.net/cfile/tistory/225B534E569F830607)

![vl53l1x](C:\Users\WOOHYON\Pictures\vl53l1x.jpg)

Pin 연결은 다음과 같다.

VIN (2.6~5.5V) - Pin# **01**

GND - Pin# **06**

SDA - Pin# **03**

SCL - Pin# **05**

GPIO1(<u>SD</u>) - (Green Pin ex. Pin# 16, 20, 21 etc)

