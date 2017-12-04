#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np
import pandas as pd
#import scip
from scipy.io import wavfile as w
#from matplotlib.pyplot import specgram
import matplotlib.pyplot as plt
from scikits.talkbox.features import mfcc
import h5py

GENRE_DIR ='.'
ceps_dir="wav/"
genre_list = ["electro", "pop", "rock", "metal"]

with h5py.File('metal.h5', 'r') as h5f:
		for k in h5f.keys():
			print h5f[k][:]
