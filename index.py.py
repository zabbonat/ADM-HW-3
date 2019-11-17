#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def Q_tf(word,text):
    tf = Counter(text)
    return(tf[word]/sum(tf.values()))
def Q_idf(query):
    count = Counter(query)
    sumsquare = 0
    for i in count.values():
        sumsquare+= np.square(i)
    return np.sqrt(sumsquare)

def query_length(query):    
    count = Counter(query)
    sumsquare = 0
    for i in count.values():
        sumsquare+= np.square(i)
    return np.sqrt(sumsquare)

def dot_product(q,doc):
    sumofproduct = 0
    for i in q:
            sumofproduct += Q_tf(i,q)*Q_idf(q)*doc[1]
    return(sumofproduct)
def document_length(doc):
    sumsquare = 0
    for i in doc:
        sumsquare+=i[1]**2
    return np.sqrt(sumsquare)


# In[ ]:


query = str(input().split())
qnorm = wordNorm(query)
inter = set() #set with the documents that contain all the words in the query
switch = True
tmp = set()
sumTfIDF = 0
for word in qnorm:
    if word in voc:
        file_score = invIndex[str(voc[word])]
        if (switch):
            for file in file_score:
                inter.add(file[0])
            switch = False
        if(len(inter) >0):
            for file in file_score:
                tmp.add(file[0])
            inter = inter.intersection(tmp)
        else:
            break
inter = intersection(qnorm,invIndex,voc,inter)
cosine_similarity = {}
for i in inter:
    cosine_similarity[i[0]] = dot_product(qnorm,i)/(query_length(qnorm)*document_length(inter))
sortedResult = sorted(cosine_similarity.items(), key=lambda kv: kv[1],reverse=True)

topFiveResult = sortedResult[:5]
topFiveSimilarityScore = []
for i in topFiveResult:
    topFiveSimilarityScore.append(round(i[1],2))
Similarity = pd.Series(topFiveSimilarityScore)

my_dataframe = pd.DataFrame()
for file in topFiveResult:
    table = pd.read_table(str(file[0]),sep='\t', header = None,index_col = None)
    my_dataframe = my_dataframe.append(pd.DataFrame(table))
df1 = my_dataframe.rename(columns={0: 'Title', 1:'Intro', 2:'Plot',14:'Wikipedia Url'})
df1["Similarity"] = Similarity.values
df2 = df1[['Title','Intro','Plot','Similarity','Wikipedia Url']]
df2[:5]

