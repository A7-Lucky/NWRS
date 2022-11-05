import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
# from webtoon.models import Webtoon

ratings = pd.read_csv('webtoon/ratings.csv')
webtoons = pd.read_csv('webtoon/naver_webtoon.csv')

# 데이터프레임을 출력했을때 더 많은 열이 보이도록 함
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 300)
# id를 기준으로 ratings 와 movies 를 결합함
webtoon_ratings = pd.merge(ratings, webtoons, on='id')

user_title = webtoon_ratings.pivot_table('rating', index='title', columns='userId')
user_title = user_title.fillna(0)

item_based_collab = cosine_similarity(user_title, user_title)
item_based_collab = pd.DataFrame(item_based_collab, index=user_title.index, columns=user_title.index)

def item_based_filtering(webtoon):
    webtoon_list = item_based_collab[webtoon].sort_values(ascending=False)[1:21]
    return webtoon_list.index