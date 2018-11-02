# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 20:48:19 2018

@author: Seth
"""

import pandas as pd
import numpy as np
score = pd.read_csv('UWvMSU_1-22-13.txt', header=0, sep = '\t')
cumulative = (score.groupby(by=['team', 'time']).sum().groupby(level=[0]).cumsum())
cumulativeteam = cumulative.reset_index(level=['team', 'time'])
from plotnine import *
graph = ggplot(cumulativeteam, aes(x = "time", y = "score", color = "team"))
graph+geom_point()+geom_line()