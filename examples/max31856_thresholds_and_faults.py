# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time

import board
import digitalio

import adafruit_max31856

# Create sensor object, communicating over the board's default SPI bus
spi = board.SPI()

# allocate a CS pin and set the direction
cs = digitalio.DigitalInOut(board.D0)
cs.direction = digitalio.Direction.OUTPUT

# create a thermocouple object with the above
thermocouple = adafruit_max31856.MAX31856(spi, cs)

# set the temperature thresholds for the thermocouple and cold junction
thermocouple.temperature_thresholds = (-1.5, 30.8)
thermocouple.reference_temperature_thresholds = (-1.0, 30.5)
current_faults = {}
current_cj_thresholds = (0, 0)
current_temp_thresholds = (0, 0)
print(thermocouple.reference_temperature_thresholds)
while True:
    current_temp_thresholds = thermocouple.temperature_thresholds
    current_cj_thresholds = thermocouple.reference_temperature_thresholds
    current_faults = thermocouple.fault
    print(
        f"Temps:    {thermocouple.temperature:.2f} :: cj: {thermocouple.reference_temperature:.2f}"
    )
    print("Thresholds:")
    print(f"Temp low: {current_temp_thresholds[0]:.2f} high: {current_temp_thresholds[1]:.2f}")
    print(f"CJ low:   {current_cj_thresholds[0]:.2f} high: {current_cj_thresholds[1]:.2f}")
    print("")
    print("Faults:")
    print(f"Temp Hi:    {current_faults['tc_high']} | CJ Hi:    {current_faults['cj_high']}")
    print(f"Temp Low:   {current_faults['tc_low']} | CJ Low:   {current_faults['cj_low']}")
    print(f"Temp Range: {current_faults['tc_range']} | CJ Range: {current_faults['cj_range']}")
    print("")
    print(
        f"Open Circuit: {current_faults['open_tc']} Voltage Over/Under: {current_faults['voltage']}"
    )
    print("")

    time.sleep(1.0)
