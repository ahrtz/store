import pandas as pd

from parse_kci import load_dataframes
# from konlpy.tag import Hannanum
# from konlpy.tag import Kkma
# from konlpy.utils import pprint
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models.keyedvectors import KeyedVectors
w2vec = KeyedVectors.load_word2vec_format(\
        './model/GoogleNews-vectors-negative300.bin.gz', binary=True, limit=900000)


def recommand(dataframe):
    w2vec.most_similar(positive=['king', 'woman'], negative=['man'], topn=3)


def main():
    data = load_dataframes()
    # parse_keyword(data)
    recommand(data)
    # hannanum_similarity("", "")


if __name__ == "__main__":
    main()