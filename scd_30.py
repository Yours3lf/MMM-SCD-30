#!/usr/bin/python
import time
import datetime
import board
import busio
import adafruit_scd30

i2cAddress = 97

# set these for accurate measurement
ambient_pressure = 1015 # mBar
altitude = 36 # meters above sea level

# SCD-30 has tempremental I2C with clock stretching, datasheet recommends
# starting at 50KHz
i2c = busio.I2C(board.SCL, board.SDA, frequency=50000)
scd = adafruit_scd30.SCD30(i2c, ambient_pressure, i2cAddress)

scd.altitude = altitude

co2 = 0
temp = 0
hum = 0
gotData = False

while gotData == False:
	if scd.data_available:
		co2 = scd.CO2
		temp = scd.temperature
		hum = scd.relative_humidity

		if co2 > 1:
			gotData = True

	time.sleep(0.5)
	# print("Data unavailable, trying again...")

print("{'CO2': %d, 'temp': %0.2f, 'hum': %0.2f}" % (co2, temp, hum))