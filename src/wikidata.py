#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Aleksander Brynjulf Hubert
# Created Date: May 2020
# =============================================================================
"""
Extraction of Wikipedia Text Dump and Tokenization on a distributed
system using pyspark on the GCP.
"""
# =============================================================================
# Imports
# =============================================================================
import numpy as np
import re
import pyspark
from pyspark import SparkContext
from pyspark import SparkConf
import itertools
import collections
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import string

stop_words = set(stopwords.words('english'))
table = str.maketrans('', '', string.punctuation)

## Tokenizer Function
def get_tokens(line):
    ## Tokenizes to lowercase words
    tokens = word_tokenize(line)
    tokens = [w.lower() for w in tokens]
    stripped = [w.translate(table) for w in tokens]
    words = [word for word in stripped if word.isalpha()]
    return (words)

## Function for tokenizing the pages
def get_page(content):
    page = []
    try:
        if(content != [] and content != None):
            ## the first line is the doc info
            ## the second line is the title
            ## the third line is the page text
            page = content.split("\n", 2)
            #tokenizes the text data
            page[2] = get_tokens(page[2])
    except:
        ## if the page is empty returns a dummy array
        ## to be removed later
        page = [1,2,3]
    return page

def tokenize_data(filepath):
    ## reads in the file
    ## my path "gs://{BUCKET_NAME}/data/*/*"
    data = sc.wholeTextFiles(filepath)
    ## flatmaps the files into a sinlge RDD where
    ## each row is seperated by the <doc tag
    ## which is how the xml splits the data
    pages = data.flatMap(lambda x :(x[1].split('<doc')))

    ## Tokenizes the page text and saves it as an RDD with each
    ## row representing an array of tokenized text
    ## for each page
    tokenized_text = pages.map(lambda x : get_page(x)[2]).filter(lambda x: x != 3)
    return tokenized_text
