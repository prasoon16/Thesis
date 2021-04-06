import numpy as np

def uniform (low, high, size):
    return np.random.uniform(low, high, size)

def normal (mu, sigma, size):
    return np.random.normal(mu, sigma, size)
