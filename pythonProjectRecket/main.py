import pandas as pd
from pytrends.request import TrendReq

# j'initialise l'objet PyTrends
pytrends = TrendReq(hl='fr-FR', tz=360)

# ma thématique ou mon mot clé
mots_cles = ["blockchain"]

# obtention des données de tendance & timeframe / pays
pytrends.build_payload(mots_cles, timeframe='today 3-m', geo='FR')

# obtention des données de tendance
data = pytrends.related_queries()

# données dans dictionnaire
# boucle et print
for mot_cle in mots_cles:
    if data[mot_cle]['top'] is not None:
        print(f"Requêtes populaires pour '{mot_cle}':")
        print(data[mot_cle]['top'])
    if data[mot_cle]['rising'] is not None:
        print(f"Requêtes en hausse pour '{mot_cle}':")
        print(data[mot_cle]['rising'])
