import numpy as np

target_lat = 40.43
target_long = -3.7123
low_cost = 20
high_cost = 100
def uniform (low, high, size):
    return np.random.uniform(low, high, size)

def normal (mu, sigma, size):
    return np.random.normal(mu, sigma, size)
