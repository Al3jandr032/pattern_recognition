#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np
import scipy
from scipy.io import wavfile as w
#from matplotlib.pyplot import specgram
import matplotlib.pyplot as plt

wave_filename = "03 - Porcelain.wav"

import os
for file in os.listdir("."):
    if file.endswith(".wav"):
        sample_rate, X = w.read(file)
        fft_features_channel1 = abs(scipy.fft(X)[10000:1324800][:][0])
        fft_features_channel2 = abs(scipy.fft(X)[10000:1324800][:][1])
        print fft_features_channel1," : ",fft_features_channel2

#plt.specgram(X[100000:150000][:][0], Fs=sample_rate,xextent=(0,30))
#plt.specgram(X[100000:900000][:][0], Fs=sample_rate)
#plt.show()
