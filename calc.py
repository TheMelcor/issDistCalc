from math import sin, cos, sqrt, atan2, radians


def calc_distance(lat1, lat2, lon1, lon2):
    # approximate radius of earth in km
    R = 6373.0

    rlat1 = radians(lat1)
    rlon1 = radians(lon1)
    rlat2 = radians(float(lat2))
    rlon2 = radians(float(lon2))

    dlon = rlon2 - rlon1
    dlat = rlat2 - rlat1

    a = sin(dlat / 2)**2 + cos(rlat1) * cos(rlat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance