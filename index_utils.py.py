#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Build invertedIndex
#invertedIndex = {termID : doc}
def invertedIndex(vocabulary):
    invertedIndex= {}
    for key,value in vocabulary.items():
        for i in value:
            if (voc[i] in invertedIndex):
                invertedIndex[voc[i]] = invertedIndex[voc[i]] + [key]
            else:
                invertedIndex[voc[i]] = [key]
    return invertedIndex

def term_freq(term, text):
    termcountdic = Counter(text)
    return termcountdic[term] / len(text)

def idf(Allword,word):
    return math.log(N/int(wordDict[word]))

def invertedIndex(vocabulary,path):
    # invertedIndex = {termID : (doc, TF*IDF)}
    invertedIndex = {}
    counter = 0
    for file in tqdm(glob.glob(path)):
        df = pd.read_table(file,sep='\t',names=['title', 'intro', 'plot', 'film_name', 'language', 'runtime', 'budget',
       'country', 'music', 'writer', 'director', 'starring', 'producer',
       'release_date', 'wikipedia_url'])
       
        intro = preprocess(str(list(df['intro'])))
        plot = preprocess(str(list(df['plot'])))
        for word in vocabulary:
                tf = term_freq(word,intro+plot)
                if(tf>0):
                    if(vocabulary[word] in invertedIndex.keys()):
                        invertedIndex[vocabulary[word]] +=[(file,tf*idf(Allword,word))] #[(file,tfidf(word,file))]
                    else:
                        invertedIndex[vocabulary[word]] = [(file,tf*idf(Allword,word))]

    return invertedIndex

