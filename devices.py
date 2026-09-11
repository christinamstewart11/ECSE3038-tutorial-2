readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]

#task 1
def list_devices(readings):
    for reading in readings:
        print(f"The device is: {reading['name']}, The temp is: {reading['temp']}")
        
list_devices(readings)

#tak 2
def average_temp(readings):
    total = 0
    for reading in readings:
        total += reading["temp"]
    avg_t = total / len(readings)
    print(f"\nThe average temp is: {avg_t}")
    return avg_t

average_temp(readings)

#task 3
def hottest(readings):
    hottest_device = readings[0]
    for reading in readings:
        if reading["temp"] > hottest_device["temp"]:
            hottest_device = reading
    print(f"\nThe hottest device is: {hottest_device}")
    return hottest_device

hottest(readings)

#task 4
def to_status(reading):
    if reading["online"]:
        status = "ok"
    else:
        status = "offline"
    return {
        "device": reading["name"],
        "status": status,
        "celsius": reading["temp"]
    }

print(f"\nThe new dictionary is: {to_status(readings[1])}")  # hall-lamp is index 1

#task 5
def by_room(readings):
    rooms = {}
    for reading in readings:
        room = reading["room"]
        if room not in rooms:
            rooms[room] = []
        rooms[room].append(reading["name"])
    print(f"\nThe device(s) under each room is/are: {rooms}")
    return rooms

by_room(readings)