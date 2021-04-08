import numpy as np
import config
from math import cos, asin, sqrt, pi, atan2,sin
import matplotlib.pyplot as plt
import pandas as pd

target_lat = 40.43
target_long = -3.7123
low_cost = 20
high_cost = 100

def uniform (low, high, size):
    return np.random.uniform(low, high, size)

def normal (mu, sigma, size):
    return np.random.normal(mu, sigma, size)

def comp_list(l1,l2):
    p1 = sorted(l1)
    p2 = sorted(l2)
    if (p1 == p2):
        return False
    return True

def deg2rad(deg):
    return deg * (pi/180)

def get_quality_from_distance(dist):
    quality = config.Task_Quality - config.Penalty * int(dist)
    if (quality < 0):
        quality = 0
    return quality

def get_distance(task, user):
    R = 6371;
    dLat = deg2rad(task.latitude-user.latitude);
    dLon = deg2rad(task.longitude-user.longitude);
    a = sin(dLat/2) * sin(dLat/2) +cos(deg2rad(user.latitude)) * cos(deg2rad(task.latitude  )) * sin(dLon/2) * sin(dLon/2);
    c = 2 *atan2(sqrt(a), sqrt(1-a));
    d = R * c;
    return d;

def get_expected_quality(task_list):
    sum = 0
    for task in task_list:
        sum = sum + task.expected_quality
    return sum

def plot_quality(q_data, trac_data, expected_quality):
    pq_data = pd.DataFrame(q_data, columns=['users', 'task', 'quality'])
    ptrac_data = pd.DataFrame(trac_data, columns=['users', 'task', 'quality'])
    plt.plot(pq_data['users'], pq_data['quality'], label="proposed algo")
    plt.plot(ptrac_data['users'], ptrac_data['quality'], label="trac algo")
    print (len(q_data))
    expected_quality_list = [expected_quality for i in range(len(q_data))]
    plt.plot(ptrac_data['users'], expected_quality_list, label = "expected quality")
    plt.xlabel("Users")
    plt.ylabel("Quality Metric")
    plt.legend()
    plt.show()
