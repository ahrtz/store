from parse_kci import load_dataframes
import itertools
from collections import Counter
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import folium as fl


def parse_keyword(dataframes):
    papers = dataframes["papers"]

    keywords = papers.keyword.apply(lambda c: c.split(" , "))

    keywords_list = []
    for keyword in keywords:
        for word in keyword:
            keywords_list.append(word)

    print(keywords_list)
    keywords_set = set(keywords_list)
    print(keywords_set)

    df = pd.DataFrame()


def main():
    data = load_dataframes()
    parse_keyword(data)


if __name__ == "__main__":
    main()
