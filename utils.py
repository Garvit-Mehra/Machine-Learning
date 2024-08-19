import numpy as np


def load_data():
    data = np.loadtxt("data.txt", delimiter=",")
    x = data[:,0]
    y = data[:,1]
    return x, y