import data as dt
import config
from quality_algo import quality_based_algo
import copy
import utility as utl
from trac import trac_based_algo

def main():
    global user_list, task_list
    user_list = dt.create_simul_data()
    task_list = dt.create_task_data()
    N = config.N
    T = config.T
    # res_i = [['users', 'tasks', 'quality']]
    # res_t = [['users', 'tasks', 'quality']]
    res_i = [[]]
    res_t = [[]]
    for i in range(100,N,50):
        sim_user_list = copy.deepcopy(user_list)
        sim_user_list = sim_user_list[:i]
        task_list_cpy = copy.deepcopy(task_list)
        tsim_user_list = copy.deepcopy(user_list)
        tsim_user_list = sim_user_list[:i]
        ttask_list_cpy = copy.deepcopy(task_list)
        print ("#### simulating for {} users {} ####".format(i, utl.get_expected_quality(task_list_cpy)))
        print ("len(sim_user_list) {} len(task_list_cpy) {} ".format(len(sim_user_list), len(task_list_cpy)))
        for task in task_list_cpy:
            task.print_task()
        qi = quality_based_algo(sim_user_list, task_list_cpy)
        # print ("qi {}".format(qi))
        qt = trac_based_algo(tsim_user_list, ttask_list_cpy)
        res_i.append([i,len(task_list), qi])
        print ("#### simulating for {} users ####".format(i))
        res_t.append([i,len(task_list), qt])
    print (res_i)
    print (res_t)
    utl.plot_quality(res_i, res_t, utl.get_expected_quality(task_list))
    # user_list = user_list[:config.N]
    # task_list = task_list[:config.T]


if __name__ == "__main__" :
    main ()
