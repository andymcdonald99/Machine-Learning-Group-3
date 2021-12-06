#Andrew Mc Donald - 18318748

from os import read
import numpy as np
from numpy.lib.function_base import append
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

def read_file():
    global df, X, winrate, fav_card, trophies
    df = pd.read_csv(r"C:\Users\mcdon\Documents\College\4th Year\Machine Learning\Project\AllData.txt", sep=" ", header=None)
    fav_card = df.iloc[:, 0]
    trophies = df.iloc[:, 1]
    winrate = df.iloc[:, 2]




def winrate_card():
    global arr
    arr = [[] for _ in range(106)]
    for i in range(len(winrate)-1):
        v1 = fav_card[i]-1
        v2 = winrate[i]
        arr[v1].append(v2)
        

def avg_val():
    global arr2
    arr2 = [0]*106
    for i in range(106):
        if(len(arr[i]) != 0):
            arr2[i] = (sum(arr[i])) / (len(arr[i]))
        




read_file()
winrate_card()
avg_val()
card = (range(0, 106))


plt.scatter(card, arr2,  color="black",marker=".", s=35)
#plt.scatter(trophies, winrate, color = "blue",marker=".", s=2)
plt.xlabel('Favourite Card')

plt.ylabel('Win Rate')

plt.title("Win Rate vs Favourite Card")
plt.legend()

plt.show()
print()