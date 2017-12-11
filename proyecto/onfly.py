#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np
from scipy.io import wavfile as w
from scikits.talkbox.features import mfcc



def create_ceps(fn):
  print "creating :",fn
  sample_rate, X = x.read(fn)
  ceps, mspec, spec = mfcc(X)
  print ceps 


create_ceps()
