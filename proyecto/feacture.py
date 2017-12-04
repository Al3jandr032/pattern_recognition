#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
import os
import numpy as np
import scipy
from scipy.io import wavfile as w
#from matplotlib.pyplot import specgram
import matplotlib.pyplot as plt


def create_fft(fn):
	sample_rate, X = w.read(wave_filename)
	fft_features = abs(scipy.fft(X)[:1000])
	base_fn, ext = os.path.splitext(fn)
	data_fn = base_fn + ".fft"
	np.save(data_fn, fft_features)
"""
def read_fft(genre_list, base_dir=GENRE_DIR):
	X = []
	y = []
	for label, genre in enumerate(genre_list):
		genre_dir = os.path.join(base_dir, genre, "*.fft.npy")
		file_list = glob.glob(genre_dir)
		for fn in file_list:
			fft_features = np.load(fn)
			X.append(fft_features[:1000])
			y.append(label)
	return np.array(X), np.array(y)
"""

wave_filename = "01 - Frozen.wav"
"""

sample_rate, X = w.read(wave_filename)
print sample_rate, X.shape

#specgram(X, Fs=sample_rate, xextent=(0,30))
specgram(X[0], Fs=sample_rate)
"""

#create_fft(wave_filename)
sample_rate, X = w.read(wave_filename)
fft_features = abs(scipy.fft(X))
#fig, ax = plt.subplots()
#print fft_features

freq = np.fft.fftfreq(len(X), sample_rate)

plt.figure()
plt.plot( freq, np.abs(X) )
plt.figure()
plt.plot(freq, np.angle(X) )
plt.show()