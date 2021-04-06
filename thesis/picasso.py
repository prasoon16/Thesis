import utility as utl
import numpy as np
from user_module import User
# Users
N = 100
# Number of Tasks
M = 30
# Users choice parameter
R = 5
# Data Point
NUM = 20

def main():
    print ("Simulating for {} Tasks for {} users".format(M, N))
    # print (utl.uniform(5, 15, 10))
    #
    # print (utl.normal(5, 15, 10))

    users = []
    for i in range(N):
        L = int(utl.uniform(1, R ,1))
        K = int(utl.uniform(1, 0.6*M, 1))
        mu_cost = utl.normal(20,40,1)
        sigma_cost = utl.normal(5,15,1)
        user = User(L, K, mu_cost, sigma_cost) # L -> no of or bids, K -> no of atomic bids, cost
        users.append(user)

    for user in users:
        user.print_user()

if __name__ == '__main__':
    main()
