#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

    # Information as intro, plot, plot_s(when instead have just 'Plot' 
    # we have 'Plot summary', and 'story'{for now no value})


# In[ ]:


collector(movies)

