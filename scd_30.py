#!/usr/bin/python
import time
import datetime
import board
import busio
import adafruit_scd30

i2cAddress = 0x61 # 97 in decimal

# set these for accurate measurement
ambient_pressure = 1015 # mBar
altitude = 36 # meters above sea level

# SCD-30 has tempremental I2C with clock stretching, datasheet recommends
# starting at 50KHz
i2c = busio.I2C(board.SCL, board.SDA)
scd = adafruit_scd30.SCD30(i2c, ambient_pressure, i2cAddress)

scd.altitude = altitude

co2 = None
temp = None
hum = None
attempts = 10

while attempts > 0:
	try:
		if scd.data_available:
			co2 = scd.CO2
			temp = scd.temperature
			hum = scd.relative_humidity

		if co2 is not None and co2 > 1:
				break  # Exit loop if valid data is read

	except RuntimeError as e:
		print(f"Error reading SCD-30: {e}")

	time.sleep(0.5)
	attempts -= 1

if co2 is not None and not (co2 != co2):
	print('{"co2": %d, "temp": %0.2f, "hum": %0.2f}' % (co2, temp, hum))
else:
	print('{"co2": %d, "temp": %0.2f, "hum": %0.2f}' % (0, 0, 0))