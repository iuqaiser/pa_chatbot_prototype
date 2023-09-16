#based on https://www.techwithtim.net/tutorials/ai-chatbot
#goal: create program, build with streamlit, deploy with either streamlit community cloud or other web app deployment service

import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tensorflow
import tflearn
import random


import json
with open('intents.json') as file:
    data = json.load(file)
