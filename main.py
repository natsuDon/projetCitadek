"""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import spacy
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import dill as pickle
import nltk
from nltk.corpus import stopwords
from vaderSentiment_fr.vaderSentiment import SentimentIntensityAnalyzer

#test de l'analyse des sentiment
from analyser_entiment import AnalyserSentiment
monAnalyser=AnalyserSentiment()

documents=["je t'aime", "je danse", "nous voulons quitter la France", "nous dansons", "c'est toujours un problème d'incompétence",
"le problème, je vous le dis, c'est les peuhles"]
i=0;




#test avec le fichier csv
import csv
from data_cleaner import DataCleaner
fil=pd.read_csv("scrappingDataHachathon.csv", sep="#")
tab=fil["paragraphe"]
dc=DataCleaner()
dataClean=dc.clean_data(tab)
my_score=monAnalyser.analyzeSentiment(dataClean)
print(my_score)
df = pd.DataFrame( {"Commentaire":dataClean,'Score': my_score})
df.to_csv("dataAnalyse2.csv")
"""

from facebook_scraper import get_posts

for post in get_posts(credentials=("kafando.donald@gmail.com", "Kafandonalnaruto19"),
        post_url="https://lefaso.net/spip.php?article116135&fbclid=IwAR2HCjpcrNa4SYsHCnJHhe0oNe_AgsBtw4GROpFaeG74g3oRv42zXXP6nFA",  pages=3):
    print(post['text'])







