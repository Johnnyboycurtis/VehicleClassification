import sys
sys.path.append('/home/jonathan/Documents/ImageNASS')
import pynass.casesearch as cs
import pynass.xmlparser as xp
import pandas as pd
import numpy as np
import pickle
from tqdm import tqdm

## get Rear end accidents for 2014-2015
finder = cs.SearchNASS(chromedriver='/home/jonathan/Documents/ImageNASS/chromedriver')

results = []
for year in [2014, 2015]:
    tmp = finder.Search(PlaneOfImpact='All', Year = year, MinVeh=2, MaxVeh='All')
    ## tmp is a dictionary, but I only want/need the caseid not the links
    results += tmp


## save case ids
with open("Cases.txt", "w+") as myfile:
    for line in results:
        myfile.write(line + '\n')


