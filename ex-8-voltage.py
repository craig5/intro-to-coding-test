#!/usr/bin/env python3

# First, open the file.
fp = open("2024-04-19-voltages.csv", "r")
# The following will read each line and put it into a "list".
lines_list = fp.readlines()
# Don't forget to close the file when done.
fp.close()


def is_good_voltage(volt_str):
    """Helper function that returns True/False if the voltage is good/bad."""
    # FIXME The "volt" data is a string. Convert it to a float.
    #
    # If it is a voltage between 0 and 0.1, return True.
    if voltage > 0 and voltage < 0.1:
        return True
    # FIXME Also check if voltage between 4.9 and 5.1 and return True
    #
    # FIXME update this code to check for all bad voltages.
    #


bad_sensor = None
bad_voltages = list()
# Iterate through each line in the file.
for cur_line in lines_list:
    # When you read a file, it appends a "\n" to each line. We need to remove that.
    cur_line = cur_line.rstrip("\n")
    # Each line contains: "time=TIME_NUMBER, SENSOOR_NAME, VOLTAGE"
    # Where:
    #   TIME_NUMBER is an int,
    #   SENSOR_NAME is a string with a value of: back,front,left,right
    #   VOLTAGE is an floating point number
    parts = cur_line.split(",")
    cur_voltage_str = parts[2]
    if is_good_voltage(cur_voltage_str) is False:
        # FIXME Append the current voltage value to the "bad_voltages" variable.
        #
        # FIXME: update thev variable "bad_sensor" when you find bad voltages
        #


print("The bad sensor is: {}".format(bad_sensor))
# FIXME Add line tp print out the number of bad voltages.
# (Hint: use the "len()" built-in function.)
#
print("Bad voltages:")
for cur in bad_voltages:
    print("  - {}".format(cur))
