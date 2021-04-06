import utility as utl
import numpy as np
import csv
from user_module import TracUser
from user_module import Bid
from user_module import print_bid
from functools import cmp_to_key
from functools import reduce


#max bids accept
R = 3
tracUserList = []
bidList = []

def remove_from_list(L, bid):
    for l in L:
        if (l.cost == bid.cost and l.task == bid.task and l.user_idx == bid.user_idx):
            L.remove(l)


def overpayment_ratio(P, W):
    return (P-W)/W

def main():
    #users
    N = 100
    #Tasks
    T = 40
    res = [['users', 'tasks', 'opr']]
    for i in range(100,1000,50):
        opr = simulate(i,T)
        res.append([i,T,opr])
    with open('data_exp.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(res)



def simulate(N, T):
    print ("Simulating for {} Tasks for {} users".format(T, N))
    for i in range(N):
        tracUserList.append(TracUser(i+1, T))
    bidList = []
    for i in range(N):
        user = tracUserList[i]
        for bid in user.bid_list:
            bidList.append(bid)
    # for bid in bidList:
    #     print_bid(bid)
    temp = bidList[:]
    S,w = trac_algo(temp, T)
    # print(S)
    # print(w)
    P = 0
    for w_bid in S:
        print_bid(w_bid)
        temp = bidList[:]
        remove_from_list(temp, w_bid)
        pay, c_bid = trac_algo_payment(temp, w_bid, S, T)
        print (pay)
        P = P + pay
    opr = overpayment_ratio(P,w)
    print("User {} overpayment_ratio {}".format(N, opr))
    return opr



def comp_list(l1,l2):
    p1 = sorted(l1)
    p2 = sorted(l2)
    if (p1 == p2):
        return False
    return True
    # res = [x for x in l1 + l2 if x not in l1 or x not in l2]
    # print (res)
    # if not res:
    #     return True
    # else:
    #     return False

def trac_algo(bidList, T):
    # print (bidList)
    Tasks = [ i+1 for i in range(T)]
    w = 0
    Q = []
    r = []
    S = []
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
                    bid.r = bid.cost/(abs(1-len(Q)))
                else:
                    bid.r = bid.cost
                r.append(bid)
        print (len(r))
        r = sorted(r, key=cmp_to_key(Bid.comparator))
        w_bid = r[0]
        bidList.remove(w_bid)
        S.append(w_bid)
        w = w + w_bid.cost
        Q.append(w_bid.task)
        for bid in bidList:
            if (bid.task == w_bid.task):
                bidList.remove(bid)

    return S,w

def trac_algo_payment(bid_list, w_bid, winner_bids, T):
    # print (bidList)
    Tasks = [ i+1 for i in range(T)]
    w = 0
    Q = []
    r = []
    # print ("###bid list###")
    # for b in bid_list:
    #     print_bid(b)
    # print ("###winner_bids###")
    # for b in winner_bids:
    #     print_bid(b)
    while (comp_list(Tasks, Q)):
        # print (comp_list(Tasks, Q))
        # print ("Tasks {}".format(Tasks))
        # print ("Q {}".format(Q))
        r = []
        for bid in bid_list:
            # print (bid)
            task = bid.task
            if (task in Q):
                bid_list.remove(bid)
            else:
                if (abs(1-len(Q))):
                    bid.rpay = bid.cost/(abs(1-len(Q)))
                else:
                    bid.rpay = bid.cost
                r.append(bid)
        # print (r)
        # print ("###r###")
        # for b in r:
        #     print_bid(b)
        r = sorted(r, key=cmp_to_key(Bid.comparator_pay))
        c_bid = r[0]
        if (c_bid in winner_bids):
            bid_list.remove(c_bid)
            continue
        if (w_bid.task == c_bid.task):
            if (abs(1-len(Q))):
                pay = c_bid.rpay*(abs(1-len(Q)))
            else:
                pay = c_bid.rpay
            return pay,c_bid
        bid_list.remove(c_bid)
        Q.append(c_bid.task)



def print_trac_user(tracUser, idx):
    for i in range(tracUser.nBids):
        bid_obj = tracUser.bid_list[i]
        print( "User #{} Bid {} Cost {} Task {}".format(idx, bid_obj.bid, bid_obj.cost, bid_obj.task))

if __name__ == '__main__':
    main()
