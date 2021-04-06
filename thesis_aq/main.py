import pandas as pd
import sys
from User import User
import utility as utl
from Task import Task

user_list = []
task_list = []

def create_task_data (df):
    l_place = df["place"]
    l_lon = df["longitude"]
    l_lat = df["latitude"]

    size = len(l_place)
    for i in range(size):
        task = Task(i,l_place[i],l_lon[i], l_lat[i])
        task_list.append(task)

    for i in range(size):
        task = task_list[i]
        task.print_task()

def create_simul_data (df):
    l_date = df["date"]
    l_lon = df["lon"]
    l_lat = df["lat"]

    size = len(l_date)
    for i in range(size):
        user = User(i, l_lon[i], l_lat[i], l_date[i])
        user_list.append(user)

    for i in range(size):
        user = user_list[i]
        user.print_user()

def main ():
    df = pd.read_csv("./simul.csv")
    df_task = pd.read_csv("./madrid.csv")
    create_simul_data(df)
    create_task_data(df_task)

if __name__ == "__main__" :
    main ()
