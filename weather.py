import json

print("yo", end = "\n")

def read_module(filename):
    try:  # As long as no FilenotFoundError
        with open(filename, r) as f:
            return json.load(f)
    except FilenotFoundError:
            return {}

def write_module(filename):
    # Assume filename will open correctly, etc.
    with open(filename, w) as f:
        json.dump(data, f)

def max_temperature(data, date):
    temp_max = date[0][t]
    for key in data:
        if date[key][t] > temp_max:
                temp_max = data[key][t]  # Key of data, temperature value
    return temp_max


def min_temperature(data, date):
    temp_min = date[0][t]
    for key in data:
        if date == key[0:8]:             # This is passing until 8th
            if date[key][t] < temp_min:
                temp_min = data[key][t]  # Key of data, temperature value
    return temp_min

def max_humidity(data, date):
    humid_max = date[0][h]
    for key in data:
        if date[key][h] > humid_max:
            humid_max = data[key][h]  # Key of data, temperature value
    return humid_max


def min_humidity(data, date):
    humid_min = date[0][h]
    for key in data:
        if date == key[0:8]:             # This is passing until 8th
            if date[key][h] < humid_min:
                humid_min = data[key][h]  # Key of data, temperature value
    return humid_min

