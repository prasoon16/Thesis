import pandas as pd
import sys
import config
from User import User
from Bid import Bid
import utility as utl
from Task import Task
import data as dt
from functools import cmp_to_key
from functools import reduce
import copy


def update_quality(task, quality):
    task.expected_quality = task.expected_quality - quality
    if (task.expected_quality < 0 ):
         task.expected_quality = 0

def get_bid_list():
    bid_list = []
    for user in quser_list:
        dist = utl.get_distance(quser_list[user.index], qtask_list[user.task])
        # print ("distance {}".format(dist))
        bid_list.append(Bid(user.task, user.cost, user.index, utl.get_quality_from_distance(dist)))
    for bid in bid_list:
        bid.print_bid()
    return bid_list

def quality_algo(bid_list, T):
    tasks = [ i for i in range(T)]
    w = 0
    Q = []
    S = []
    qlty = 0
    while (utl.comp_list(tasks, Q)):
        # print ("Q {}".format(Q))
        # print ("lenght bid_list {}".format(len(bid_list)))
        r = []
        for bid in bid_list:
            task = bid.task
            if (task in Q):
                bid_list.remove(bid)
            else:
                if (abs(1-len(Q))):
                    bid.utility = bid.cost/(abs(1-len(Q)))
                else:
                    bid.utility = bid.cost
                r.append(bid)
        r = sorted(r, key=cmp_to_key(Bid.comparator_utility))
        if (len(r) == 0 ):
            # continue
            return S,w,qlty
        w_bid = r[0]
        w_bid.print_bid()
        # print ("w_bid.task {} ".format(w_bid.print_bid()))
        task = qtask_list[w_bid.task]
        qlty = qlty + w_bid.quality
        print ("qlty {}".format(qlty))
        update_quality(task, w_bid.quality)
        bid_list.remove(w_bid)
        S.append(w_bid)
        w = w + w_bid.cost
        if (task.expected_quality <= 0):
            Q.append(w_bid.task)
        for bid in bid_list:
            if (bid.task == w_bid.task):
                bid_list.remove(bid)
    return S,w,qlty

# def run_simulate(bid_list):
#     print ("Simulating for {} Tasks for {} users".format(config.T, config.N))
#     bid_list_copy = bid_list[:]
#     S, w,qlty = quality_algo(bid_list_copy, config.T)
#     print ("S {} w {} qlty {}".format(S, w, qlty))

def quality_based_algo(s_user_list, s_task_list):
    global qN, qT
    global quser_list, qtask_list
    qN = len(s_user_list)
    qT = len(s_task_list)
    quser_list = s_user_list
    qtask_list = s_task_list
    bid_list = get_bid_list()
    bid_list_copy = copy.deepcopy(bid_list)
    S,w,qlty = quality_algo(bid_list_copy, qT)
    return qlty
# def main ():
#     global user_list, task_list
#     user_list = dt.create_simul_data()
#     task_list = dt.create_task_data()
#     user_list = user_list[:config.N]
#     task_list = task_list[:config.T]
#     bid_list = get_bid_list()
#     run_simulate(bid_list)
#
# if __name__ == "__main__" :
#     main ()
