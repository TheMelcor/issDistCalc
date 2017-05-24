import urllib2
import json
from calc import calc_distance

localLat = 0
localLong = 0
iss = []


def get_iss_cords():
    req = urllib2.Request("http://api.open-notify.org/iss-now.json")
    response = urllib2.urlopen(req)

    obj = json.loads(response.read())

    return obj


# Use this function if you want a predefined long/lat
def run(latitude, longitude):
    iss = get_iss_cords()

    # print iss['timestamp']
    # print iss['iss_position']['latitude'], iss['iss_position']['longitude']

    print "Current ground distance to the ISS: " + str(calc_distance(latitude, iss['iss_position']['latitude'], longitude, iss['iss_position']['longitude'])) + "km"


def run2(localcords):
    global iss

    iss = get_iss_cords()

    distance = calc_distance(float(localcords[0]), iss['iss_position']['latitude'], float(localcords[1]), iss['iss_position']['longitude'])

    return round(distance,2)


def get_local_cords():
    response = urllib2.urlopen('http://ipinfo.io/json')
    data = json.load(response)
    _temp = str(data["loc"])
    return str.split(_temp, ",")