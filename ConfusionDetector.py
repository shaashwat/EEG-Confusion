import pandas as pd
from sklearn import svm
import numpy as np

data = np.array(pd.read_csv("EEG data.csv", delimiter=","))

subjectID = data[0, :]
videoID = data[1, :]
attention = data[2, :]
mediation = data[3, :]
rawSignal = data[4, :]
delta = data[5, :]
theta = data[6, :]
alphaOne = data[7, :]
alphaTwo = data[8, :]
betaOne = data[9, :]
betaTwo = data[10, :]
gammaOne = data[11, :]
gammaTwo = data[12, :]
expectedConfused = data[13, :]
confusion = data[14, :]

# print (subjectID)
