from User import User
import utility as utl
from Task import Task
import pandas as pd


def create_task_data ():
    df = pd.read_csv("./madrid.csv")
    l_place = df["place"]
    l_lon = df["longitude"]
    l_lat = df["latitude"]
    task_list = []
    size = len(l_place)
    for i in range(size):
        task = Task(i,l_place[i],l_lon[i], l_lat[i])
        task_list.append(task)

    for i in range(size):
        task = task_list[i]
        task.print_task()
    return task_list

def create_simul_data ():
    df = pd.read_csv("./simul.csv")
    l_date = df["date"]
    l_lon = df["lon"]
    l_lat = df["lat"]
    user_list = []
    size = len(l_date)
    for i in range(size):
        user = User(i, l_lon[i], l_lat[i], l_date[i])
        user_list.append(user)

    for i in range(size):
        user = user_list[i]
        user.print_user()

    return user_list
