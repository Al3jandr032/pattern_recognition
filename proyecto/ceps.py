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
#genre_list = ["electro"]
def write_ceps(ceps, fn):
  base_fn, ext = os.path.splitext(fn)
  data_fn = base_fn + ".ceps"
  np.save(data_fn, ceps)
  print("Written %s" % data_fn)
def create_ceps(fn):
  print "creating :",fn
  sample_rate, X = scipy.io.wavfile.read(fn)
  ceps, mspec, spec = mfcc(X)
  write_ceps(ceps, fn)

def read_ceps(genre_list, base_dir=GENRE_DIR):
    data= {}

    for label, genre in enumerate(genre_list):
      print "genero", label,":",genre
      for file in os.listdir(os.path.join(base_dir, genre,ceps_dir)): 
          if file.endswith(".ceps.npy"):
              ceps = np.load(os.path.join(base_dir, genre,ceps_dir)+file)
              num_ceps = len(ceps)
              """
              print file," -> ",ceps.shape," : ",ceps[0]
              tmp = np.empty([1])
              for i in xrange(ceps.shape[0]):
                tmp = np.append(tmp,ceps[i][0])
              """
              if genre not in data:
                data[genre] = [np.mean(ceps[int(num_ceps*1/10):int(num_ceps*9/10)], axis=0)]
              else:
                data[genre].append(np.mean(ceps[int(num_ceps*1/10):int(num_ceps*9/10)], axis=0))
              
              
            #X.append(np.mean(ceps[int(num_ceps*1/10):int(num_ceps*9/10)], axis=0))
            #y.append(1)
      print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4"
    #return np.array(X), np.array(y)
    return data

cl =read_ceps(genre_list)
#panda_pop = pd.DataFrame(data)

for key in cl:
  print len(cl[key])
  with h5py.File(str(key)+'.h5', 'w') as h5f:
    cont =0
    for elem in cl[key]:
      aux =str(key)+str(cont)
      print aux
      h5f.create_dataset(aux, data=elem)
      cont += 1

"""
for file in os.listdir("./rock/wav"):
    if file.endswith(".wav"):
        create_ceps("./rock/wav/"+file)

for file in os.listdir("./metal/wav"):
    if file.endswith(".wav"):
        create_ceps("./metal/wav/"+file)

for file in os.listdir("./electro/wav"):
    if file.endswith(".wav"):
        create_ceps("./electro/wav/"+file)
"""
#print read_ceps(genre_list)
