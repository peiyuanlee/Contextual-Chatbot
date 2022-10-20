#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import string 
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def preprocessing(texts):
    # turn text to lower case
    texts = texts.lower()
    
    #remove punctuation, return words in a list
    remove_punc = [i for i in list(texts) if i not in string.punctuation]
    
    #join list to form string
    texts = "".join(remove_punc)
    
    #tokenization
    tokens = word_tokenize(texts)
    
    #lemmatize words
    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    
    #remove stopwords and return words in list
    return [i for i in lemmas if i not in stopwords.words('english')]

