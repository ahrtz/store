import pandas as pd

from parse_kci import load_dataframes
from konlpy.tag import Hannanum
from konlpy.tag import Kkma
from konlpy.utils import pprint
from sklearn.feature_extraction.text import TfidfVectorizer


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


def hannanum_similarity(doc1, doc2):
    hannanum = Hannanum()
    str1 = "로봇 및 공작기계용 롤러기어 캠 감속기의 성능 비교 평가"
    str2 = "착용용 보행보조로봇의 일체형 족관절 토크센서 및 기구 설계"
    # doc1 = hannanum.nouns(str1)
    # doc2 = hannanum.nouns(str2)
    # print(set(doc1) & set(doc2))
    kkma = Kkma()
    pprint(kkma.sentences(str2))


def jaccard_similarity(doc1, doc2):
    doc1 = set(doc1)
    doc2 = set(doc2)
    return len(doc1 & doc2) / len(doc1 | doc2)


def tf_idf_similarity(doc1, doc2):
    tfidf_vectorizer = TfidfVectorizer(min_df=1)
    tfidf_matrix = tfidf_vectorizer.fit_transform([doc1, doc2])

    document_distance = (tfidf_matrix * tfidf_matrix.T)
    # print(document_distance)
    return document_distance.toarray()[0][1]


def get_similarity(dataframes):
    papers = dataframes["papers"]
    data = papers.iloc[251, :]  # "성능 인자를 활용한 7자유도 상지 외골격 로봇의 설계"
    # print(data)

    similarity_list = []
    for i in range(0, 900):
        similarity = []
        # similarity.append(tf_idf_similarity(papers["title_en"][i], data.title_en))
        similarity.append(jaccard_similarity(papers["title_ko"][i], data.title_ko))
        # similarity.append(jaccard_similarity(papers["author"][i], data.author))
        # similarity.append(jaccard_similarity(papers["abstract"][i], data.abstract))
        # similarity.append(jaccard_similarity(papers["subject"][i], data.subject))
        # score = (0.3*similarity[0] + 0.3*similarity[1] + 0.1*similarity[2] + 0.2*similarity[3] + 0.1*similarity[4])
        similarity_list.append((i, score, similarity))
        # print(similarity)

    # print(similarity_list)
    similarity_list = sorted(similarity_list, key=lambda sim: sim[1], reverse=True)
    # # print(similarity)

    similarity_paper = []
    for i in range(0, 10):
        print(similarity_list[i])
        similarity_paper.append(papers.loc[similarity_list[i][0], :])
    #
    print(similarity_paper)


def main():
    data = load_dataframes()
    # parse_keyword(data)
    get_similarity(data)
    # hannanum_similarity("", "")


if __name__ == "__main__":
    main()
