import pandas as pd
from sklearn import svm
import numpy as np

conf = pd.read_csv("EEG data.csv", delimiter=",")

X = conf[[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]
Y = conf[[14]]


