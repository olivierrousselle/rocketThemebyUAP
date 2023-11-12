
from pytrends.request import TrendReq
import pandas as pd

""" https://pypi.org/project/pytrends/ 
    https://github.com/pat310/google-trends-api/wiki/Google-Trends-Categories """

thematics = ["bitcoin"]
timeframe = 'today 3-m' # date to start from
country = 'US' # two letter country abbreviation
gprop = '' # images, news, youtube or froogle (google shopping)
cat = '' # google trends categories (7: finance, 12: business, 16: news, 74: education)

while True:
    try:
        pytrends = TrendReq()
        if cat == '':
            pytrends.build_payload(thematics, timeframe=timeframe, geo=country, gprop=gprop)
        else:
            pytrends.build_payload(thematics, cat=cat, timeframe=timeframe, geo=country, gprop=gprop)
        for thematic in thematics:
            data = pytrends.related_queries()
            if data[thematic]['top'] is not None:
                keywords_top = data[thematic]['top'][['query']]
                keywords_top = keywords_top.rename(columns={'query': 'query top'})
            if data[thematic]['rising'] is not None:
                keywords_rising = data[thematic]['rising'][['query']]
                keywords_rising = keywords_rising.rename(columns={'query': 'query rising'})
            if len(keywords_top) > 0 and len(keywords_rising) > 0:
                keywords = pd.merge(keywords_top, keywords_rising, left_index=True, right_index=True)
                print(f"Requêtes populaires/en hausse pour '{thematic}':")
                print(keywords)
                keywords.to_csv(f"keywords_{thematic}.txt", sep=',')
        break
    except:
        pass
