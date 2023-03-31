#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install gensim')
get_ipython().system('pip install nltk')
get_ipython().system('pip install PyPDF2')
get_ipython().system('pip install pytesseract')
import os.path
import pathlib
import re
import requests
import PyPDF2
import pytesseract
from bs4 import BeautifulSoup as bs
from difflib import SequenceMatcher
from flask import *
from gensim import corpora, models, similarities
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.metrics import edit_distance

app = Flask("Plagiarism Checker")
app.secret_key = "SIH2022AI"

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

GOOGLE_CLIENT_ID = "824135687740-s7siaanvlm13t1ak8ko50dsg0nf1eijq.apps.googleusercontent.com"
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = re.sub(r'[^\w\s]', '', text)
    tokens = word_tokenize(text.lower())
    filtered_tokens = [token for token in tokens if token not in stop_words]
    return filtered_tokens

def get_input_text(f):
    if '.txt' in str(f):
        with open(f, 'r') as file:
            text = file.read()
    elif '.pdf' in str(f):
        with open(f, 'rb') as file:
            pdfReader = PyPDF2.PdfFileReader(file)
            pages = []
            for i in range(pdfReader.numPages):
                page = pdfReader.getPage(i)
                text = page.extractText()
                pages.append(text)
            text = ' '.join(pages)
    elif '.doc' in str(f) or '.docx' in str(f):
        text = textract.process(f)
        text = text.decode('utf-8')
    return text

def cosine_similarity(text1, text2):
    texts = [text1, text2]
    tokenized_texts = [preprocess(text)


# In[ ]:





# In[ ]:




