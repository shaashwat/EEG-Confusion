import pandas as pd
from sklearn import svm
import numpy as np

conf = pd.read_csv("EEG data.csv", delimiter=",")

X = conf[[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]
Y = conf[[14]]

clf = svm.SVC()
clf.fit(X, Y)
prediction = clf.predict([20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
print(prediction)

if(prediction < 0) { 
	print("error!")
}
