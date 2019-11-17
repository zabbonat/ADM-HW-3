#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import wptools
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


# In[ ]:


#From each movie we have saved information as intro,plot and plot_s(this one represents plot in the case inside 
#Wikipedia Pages is not just Plot but Plot Summary)
def scraping(title,movies):    
    intro=[]
    plot=[]
    plot_s=[]
    story=[]
    import wikipedia
    for i in range(len(movies)):
        try:
            intro.append(wikipedia.WikipediaPage(title = title[i]).summary)
            plot.append(wikipedia.WikipediaPage(title[i]).section('Plot'))
            plot_s.append(wikipedia.WikipediaPage(title[i]).section('Plot summary'))
            print("Current progress",np.round(i/len(title)*100,2),"%")
            print(datetime.datetime.now().time())
        except wikipedia.DisambiguationError: 
            #in case it finds a DisambiguationPage he appenda to intro,plot,plot_s: ambiguos
              intro.append('ambiguos')
              plot.append('ambiguos')
              plot_s.append('ambiguos')


# In[ ]:


scraping(title,movies)


# In[ ]:


#a way to download all the infobox information for each movie 
def infoall(title):
    infobox=[] 
    for i in range(len(title)):
        page=wptools.page(title[i]).get_parse()
        infobox.append(page.data['infobox'])
    print("Current progress",np.round(i/len(title)*100,2),"%")
    return infobox


# In[ ]:


infoall(title)


# In[ ]:


#a method to insert all the information inside the dataframe
def built_dataframe(df,infobox):   
    df['title']=title
    df['intro']=intro
    df['plot']=plot
    df['plot_s']=plot_s

    #In the case plot is None we replace the value with plot_s, as previous, some movies don't have just 'plot' but 
    # 'plot summary'
    for l in range(len(df)):
        if df['plot'][l]==None:
            df['plot'][l]=df['plot_s'][l]
    for i in range(0,len(infobox)):
        try:
            if infobox[i]['name'] is not None:
                df['film_name'][i]=infobox[i]['name']
        except KeyError:         
              df['film_name'][i]='NA'

        try:
            if infobox[i]['director'] is not None:
                df['director'][i]=infobox[i]['director']     
        except KeyError: 
            df['director'][i]='NA'

        try:
            if infobox[i]['producer'] is not None:
                 df['producer'][i]=infobox[i]['producer']
        except KeyError:     
              df['producer'][i]='NA'

        try:
            if infobox[i]['writer'] is not None:
                df['writer'][i]=infobox[i]['writer']

        except KeyError: 
              df['writer'][i]='NA'

        try:
            if infobox[i]['starring'] is not None:
                 df['starring'][i]=infobox[i]['starring']
        except KeyError:     
              df['starring'][i]='NA'

        try:
            if infobox[i]['music'] is not None:
                 df['music'][i]=infobox[i]['music']
        except KeyError:     
              df['music'][i]='NA'  

        try:
            if infobox[i]['release_date'] is not None:
                 df['release_date'][i]=infobox[i]['release_date']
        except KeyError:    
              df['release_date'][i]='NA'

        try:
            if infobox[i]['runtime'] is not None:
                 df['runtime'][i]=infobox[i]['runtime']

        except KeyError:          
                df['runtime'][i]='NA'

        try:
            if infobox[i]['country'] is not None:
                 df['country'][i]=infobox[i]['country']

        except KeyError:         
               df['country'][i]='NA'

        try:
            if infobox[i]['language'] is not None:
                 df['language'][i]=infobox[i]['language']
        except KeyError:     
               df['language'][i]='NA'     
        try:
            if infobox[i]['budget'] is not None:
                  df['budget'][i]=infobox[i]['budget']
        except KeyError:   
              df['budget'][i]='NA'


# In[ ]:


build_dataframe(df,infobox)


# In[1]:


#A way to add in a correct way wikipedia links to each movie 
def wikipedia_url(df):
    for i in tqdm(range(len(df))):
        try:
            page= wikipedia.page(df['title'][i])
            df['wikipedia_url'][i]=page.url
        except:
            df['wikipedia_url'][i]='nolink'
            continue


# In[ ]:


wikipedia_url(df)


# In[ ]:


#CLEANING HTML DATA
def clean_html(df,col):
    from bs4 import BeautifulSoup
    for i in range(len(df)):
            df[col][i] = BeautifulSoup(str(df[col][i]), "lxml").text


# In[ ]:


clean_html(df,col)


# In[ ]:


#REMOVING THE PUNCTUATION FROM THE TEXT
def clear_punctuation(df,col):
    for i in tqdm(range(len(unique_file))):
        df[col][i]= str(df[col][i]).translate ({ord(c): " " for c in "!@#$%^&*()[]{};/<>?\|`~-=_+"})


# In[ ]:


clear_punctuation(df,col)


# In[ ]:


#SAVE TSV FILES WHERE EACH DOCUMENT REPRESENTS A SINGOL MOVIE 
for i in range(len(unique_file)):
    with open(r'C:\Users\Dilet\Desktop\Homework_3\data\Part_2\Doc\doc_'+str(i+1)+'.tsv','w', encoding="utf-8") as write_tsv:
        write_tsv.write(unique_file.iloc[[i]].to_csv(sep='\t', index=False, header=None))






