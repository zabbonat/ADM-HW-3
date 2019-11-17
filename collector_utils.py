#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import bs4
from bs4 import BeautifulSoup, SoupStrainer
import requests
import pickle
import re
import pandas as pd
import matplotlib.pyplot as plt
import wikipediaapi
import requests
import time
import numpy as np
import pickle
import csv
import scipy as sp
from IPython.display import clear_output
import wptools
import wikipedia
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
from nltk.tokenize import RegexpTokenizer
from nltk.collocations import *
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
import string
import itertools as it
import json
# For a nice view of the output
from IPython.display import HTML, display
from tabulate import tabulate
import num2words


def collector(movies) :
    import datetime
    import json
    page=[]
    for i in range(7508,len(movies)):
        clear_output(wait=True)
        response= requests.get(movies[i])
        if response.status_code== 200:
            if response.status_code !=300:
                page=bs4.BeautifulSoup(response.text, 'html.parser')
                title.append(page.select("#firstHeading")[0].text) #from we keep the title
            if response.status_code == 429:
                time.sleep(20*10)
            with open('article_'+ str(i+1)+'.html', 'w', encoding="utf-8") as f_output:
                f_output.write(str(page))
        print("Current progress to download title and page",np.round(i/len(movies)*100,2),"%")

