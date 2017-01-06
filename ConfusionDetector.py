import pandas as pd
from sklearn import svm
import numpy as np

print("eeg data")

data = np.array(pd.read_csv("EEG data.csv", delimiter=","))
'''
[0]: Subject ID
[1]: Video ID
[2]: Attention (Proprietary measure of mental focus)
[3]: Mediation (Proprietary measure of calmness)
[4]: Raw (Raw EEG signal)
[5]: Delta (1-3 Hz of power spectrum)
[6]: Theta (4-7 Hz of power spectrum)
[7]: Alpha 1 (Lower 8-11 Hz of power spectrum)
[8]: Alpha 2 (Higher 8-11 Hz of power spectrum)
[9]: Beta 1 (Lower 12-29 Hz of power spectrum)
[10]: Beta 2 (Higher 12-29 Hz of power spectrum)
[11]: Gamma 1 (Lower 30-100 Hz of power spectrum)
[12]: Gamma 2 (Higher 30-100 Hz of power spectrum)
[13]: predefined label (whether the subject is expected to be confused)
[14]: user-defined label (whether the subject is actually confused)
'''
# stores each column in a variable
 
subjectID = data[:,0]
videoID = data[1,:]
attention = data[2,:]
mediation = data[3,:]
rawSignal = data[4,:]
delta = data[5,:]
theta = data[6,:]
alphaOne = data[7,:]
alphaTwo = data[8,:]
betaOne = data[9,:]
betaTwo = data[10,:]
gammaOne = data[11,:]
gammaTwo = data[12,:]
expectedConfused = data[13,:]
confusion = data[14,:]

print (confusion)
