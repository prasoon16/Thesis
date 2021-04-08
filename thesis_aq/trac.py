import utility as utl
import numpy as np
import csv
import config
import data as dt
from Bid import Bid
from functools import cmp_to_key
from functools import reduce
import copy

def get_bid_list(user_list):
    bid_list = []
    for user in user_list:
        dist = utl.get_distance(user_list[user.index], ttask_list[user.task])
        bid_list.append(Bid(user.task, user.cost, user.index, utl.get_quality_from_distance(dist)))
    for bid in bid_list:
        bid.print_bid()
    return bid_list

def comp_list(l1,l2):
    p1 = sorted(l1)
    p2 = sorted(l2)
    if (p1 == p2):
        return False
    return True

def overpayment_ratio(P, W):
    return (P-W)/W

def trac_algo(bidList, T):
    # print (bidList)
    Tasks = [ i for i in range(T)]
    w = 0
    Q = []
    r = []
    S = []
    qlty = 0
    while (comp_list(Tasks, Q)):
        print (comp_list(Tasks, Q))
        print ("S {}".format(Tasks))
        print ("Q {}".format(Q))
        r = []
        for bid in bidList:
            # print (bid)
            task = bid.task
            if (task in Q):
                bidList.remove(bid)
            else:
                if (abs(1-len(Q))):
                    bid.utility = bid.cost/(abs(1-len(Q)))
                else:
                    bid.utility = bid.cost
                r.append(bid)
        print (len(r))
        r = sorted(r, key=cmp_to_key(Bid.comparator_utility))
        w_bid = r[0]
        task = ttask_list[w_bid.task]
        qlty = qlty + w_bid.quality
        bidList.remove(w_bid)
        S.append(w_bid)
        w = w + w_bid.cost
        Q.append(w_bid.task)
        for bid in bidList:
            if (bid.task == w_bid.task):
                bidList.remove(bid)

    return S,w,qlty

def remove_from_list(L, bid):
    for l in L:
        if (l.cost == bid.cost and l.task == bid.task and l.user == bid.user):
            L.remove(l)

def trac_algo_payment(bid_list, w_bid, winner_bids, T):
    # print (bidList)
    Tasks = [ i for i in range(T)]
    w = 0
    Q = []
    r = []
    while (comp_list(Tasks, Q)):
        r = []
        for bid in bid_list:
            # print (bid)
            task = bid.task
            if (task in Q):
                bid_list.remove(bid)
            else:
                if (abs(1-len(Q))):
                    bid.payment = bid.cost/(abs(1-len(Q)))
                else:
                    bid.payment = bid.cost
                r.append(bid)
        r = sorted(r, key=cmp_to_key(Bid.comparator_payment))
        c_bid = r[0]
        if (c_bid in winner_bids):
            bid_list.remove(c_bid)
            continue
        if (w_bid.task == c_bid.task):
            if (abs(1-len(Q))):
                pay = c_bid.payment*(abs(1-len(Q)))
            else:
                pay = c_bid.payment
            return pay,c_bid
        bid_list.remove(c_bid)
        Q.append(c_bid.task)

# def main():
#     user_list = dt.create_simul_data()
#     user_list = user_list[:config.N]
#     task_list = dt.create_task_data()
#     task_list = task_list[:config.T]
#     # run_simulate(config.N, config.T, user_list, task_list)
#     bid_list = get_bid_list(user_list)
#     run_simulate(bid_list)

def run_simulate(bid_list):
    print ("Simulating for {} Tasks for {} users".format(config.T, config.N))
    bid_list_copy = bid_list[:]
    S,w = trac_algo(bid_list_copy, config.T)
    print ("S {} w {}".format(S, w))
    P = 0
    for w_bid in S:
        w_bid.print_bid()
        temp = bid_list[:]
        remove_from_list(temp, w_bid)
        pay, c_bid = trac_algo_payment(temp, w_bid, S, config.T)
        print (pay)
        P = P + pay
    opr = overpayment_ratio(P,w)
    print (opr)


def trac_based_algo(t_user_list, t_task_list):
    global tN, tT
    global tuser_list, ttask_list
    tN = len(t_user_list)
    tT = len(t_task_list)
    tuser_list = t_user_list
    ttask_list = t_task_list
    bid_list = get_bid_list(tuser_list)
    bid_list_copy = copy.deepcopy(bid_list)
    S,w,quality = trac_algo(bid_list_copy, tT)
    return quality
# if __name__ == '__main__':
#     main()
