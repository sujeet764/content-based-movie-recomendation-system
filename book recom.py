#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel

books = pd.read_csv("books.csv")

books.Title = books.Title.str.lower()

tfv = TfidfVectorizer(stop_words="english")

books['Genre'] = books['Genre'].fillna(" ")

tfv_matrix = tfv.fit_transform(books["Genre"])

sig = sigmoid_kernel(tfv_matrix,tfv_matrix)

import pickle
with open("book_sig.pickle","wb") as f:
    pickle.dump(sig,f)

indices = pd.Series(books.index,index = books['Title']).drop_duplicates()

with open("book_indices.pickle","wb") as f:
    pickle.dump(indices,f)

with open("book_title.pickle","wb") as f:
    pickle.dump(books,f)

#sorted(list(enumerate(sig[indices['Fundamentals of Wavelets']])), key = lambda x:x[1], reverse=True)

def book_rec(title,sig=sig):
    try:
        title= title.lower()
        idx = indices[title]
        sig_score = list(enumerate(sig[idx]))
        sig_score = sorted(sig_score,key=lambda x : x[1], reverse=True)
        sig_score = sig_score[1:11]
        book_indices = [i[0] for i in sig_score]
        return books['Title'].iloc[book_indices]
    except:
        return


# In[63]:


indices


# In[ ]:




