# Reference: https://wikidocs.net/31698

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

df = pd.read_excel("논문검색리스트 정제 (1).xls", sheet_name="논문검색리스트")

df['abstract'].fillna('', inplace=True)

tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df['abstract'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(df.index, index=df['논문명']).drop_duplicates()


def get_recommendations(title, cosine_sim=cosine_sim):
    idx = indices[title]

    sim_scores = list(enumerate(cosine_sim[idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    for i in range(10):
        print(sim_scores[i])

    sim_scores = sim_scores[1:11]

    movie_indices = [i[0] for i in sim_scores]

    return df['논문명'].iloc[movie_indices]

print(get_recommendations('Working environments and clothing conditions in the construction industry'))
