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
    humid_max = 0
    for key in data:
        if date[key][h] > humid_max:
            humid_max = data[key][h]  # Key of data, temperature value
    return humid_max


def min_humidity(data, date):
    humid_min = 100
    for key in data:
        if date == key[0:8]:             # This is passing until 8th
            if date[key][h] < humid_min:
                humid_min = data[key][h]  # Key of data, temperature value
    return humid_min

def tot_rain(data, date):
    rain_sum = 0
    for key in data:
        if date == key[0:8]:
            rain_sum += date[key][r]
    return rain_sum

def report_daily(data, date):
    display = "========================= DAILY REPORT ========================\n"
    display += "Date                      Time  Temperature  Humidity  Rainfall\n"
    display += "====================  ========  ===========  ========  ========\n"
    
    
    for key in data:    
        if key[0,8]:  # 4-6 things in the string (doesn't check the very last one)
            # mdy is the Month DD, YYYY form of the date (ensure that the slice is a string, because
            # depending on the string it may try to return an integer instead)
            mdy = calendar.month_name(int(date[4:6])) + str(int(date[6:8])), "," + str(int(date[0:4]))
            # hms is the HH:MM:SS form of the time
            hms = key[8:10] + ":" + key[10:12] + ":" + key[12:14]

            t = data[key][t]
            h = data[key][h]
            r = data[key][r]

            # Number of spaces between
            display += f'{mdy:22}{hms:8}{t:13}{h:10}{r:10.2f}' + '\n'
    return display