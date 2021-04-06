import utility as utl
import numpy as np
# Data Point
NUM = 20
def get_cost (mu_cost, sigma_cost):
    cost = 0
    for i in range(NUM):
        cost = cost + abs(utl.uniform(mu_cost, sigma_cost, 1))
    cost  = int(cost/NUM)
    return cost


class User(object):
    """User class containing info about bids."""

    def __init__(self, L, K, mu_cost, sigma_cost):
        self.L = L
        self.K = K
        self.cost = []
        self.total_bids = L*K
        for i in range(self.total_bids):
            self.cost.append(get_cost(mu_cost, sigma_cost))

    def print_user(self):
        print ("OR Bids {} Atomic Bids {} Costs {} ".format(self.L, self.K, (self.cost)))


class Bid(object):
    """Bid for user"""
    def __init__(self, idx, T):
        self.cost = self.get_trac_cost_exp()
        self.bid = self.get_bid(self.cost)
        self.task = int(utl.uniform(1,T+1,1))
        self.user_idx = idx
        self.r = 1000
        self.rpay = 1000
        # print (self.cost,self.bid)
    def get_trac_cost(self):
        mu = int(utl.uniform(15,50,1))
        sigma = int(utl.uniform(2,3,1))
        return int(utl.normal(mu, sigma, 1))
    def get_trac_cost_uniform(self):
        return int(utl.uniform(12, 50, 1))
    def get_trac_cost_exp(self):
        cost = int(utl.uniform(12, 50, 1))
        x = np.log(cost)/(-0.2)
        return int((-1)*x)

    def get_bid(self, cost):
        return int(utl.uniform(3,10,1)+ cost)
    def comparator(b1, b2):
        if (b1.r == b2.r):
            return 0
        elif (b1.r<b2.r):
            return -1
        else:
            return 1
    def comparator_pay(b1, b2):
        if (b1.rpay == b2.rpay):
            return 0
        elif (b1.rpay<b2.rpay):
            return -1
        else:
            return 1


def print_bid(bid):
    print ("cost {} bid {} task {} user {} ".format(bid.cost, bid.bid, bid.task, bid.user_idx))

class TracUser(object):
    """User class for Trac Algo"""
    def __init__(self, idx, T):
        self.user_idx = idx
        self.nBids = int(utl.uniform(5,10,1))
        self.bid_list = []
        for i in range(self.nBids):
            self.bid_list.append(Bid(self.user_idx, T))
