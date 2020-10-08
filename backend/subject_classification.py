import pandas as pd
import os
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing.text import Tokenizer
import tensorflow as tf 
from keras.preprocessing.sequence import pad_sequences
import sqlite3
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
import seaborn as sns

subjects = [
    "기타자연과학", "대기과학", "물리학", "생물학", "생활과학", 
    "수학", "자연과학", "자연과학일반", "지구과학", "지질학", "천문학", "통계학", 
    "해양학", "화학", "건축공학", "고분자공학", "공학", "공학일반", "교통공학", "금속공학", "기계공", 
    "기타공학", "농공학", "산림공학", "산업공학", "생물공학", "섬유공학", "안전공학", 
    "원자력공학", "의공학", "자동차공학", "자원공학", "재료공학", "전기공학", "전자/정보통신공학", 
    "제어계측공학", "조선공학", "컴퓨터학", "토목공학", "항공우주공학", "해양공학", "화학공학", "환경공학"
]

def data_preprocessing(abstract):
    # 특수 문자, 길이 짧은 단어, 소문자 변환
    pattern = "[^a-zA-Z]"
    abstract = re.sub(pattern=pattern, repl=" ", string=abstract)
    abstract = ' '.join([abstract for abstract in abstract.split() if len(abstract)>3])
    abstract = abstract.lower()

    # 불용어 제거
    stop_words = stopwords.words('english')
    tokenized_doc = abstract
    tokenized_doc = word_tokenize(tokenized_doc)
    tokenized_doc = [word for word in tokenized_doc if not word in stopwords.words()]
    
    return tokenized_doc

def vectorize_sequences(sequences, dimension=35000):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1.
    return results

def data_classification(abstract):
    tokenizer = Tokenizer(num_words=35000)
    tokenizer.fit_on_texts(abstract)
    abstract = tokenizer.texts_to_sequences(abstract)
    abstract = pad_sequences(abstract,maxlen=398)
    # print(abstract)
    vectorized_abstract = vectorize_sequences(abstract)
    # print(vectorized_abstract)
    
    model = tf.keras.models.load_model('./model_10epoch.h5')
    output = model.predict_classes(vectorized_abstract)

    count={}
    for i in output:
        try: count[i] += 1
        except: count[i]=1
    # print(count)
    
    classes = sorted(count.items(), reverse=True, key=lambda item:item[1])
    if len(classes) > 2:
        return classes[:2]
    else:
        return classes

def jaccard_similarity(doc1, doc2):
    if doc1 == "" or type(doc1) == type(1.0) or doc2 == "" or type(doc2) == type(1.0):
        return 0
    doc1 = set(doc1)
    doc2 = set(doc2)
    return len(doc1 & doc2) / len(doc1 | doc2)


def tf_idf_similarity(doc1, doc2):
    if doc1 == "" or type(doc1) == type(1.0) or doc2 == "" or type(doc2) == type(1.0):
        return 0

    tfidf_vectorizer = TfidfVectorizer(min_df=1)
    tfidf_matrix = tfidf_vectorizer.fit_transform([doc1, doc2])

    document_distance = (tfidf_matrix * tfidf_matrix.T)
    # print(document_distance)
    return document_distance.toarray()[0][1]

def get_similarity(tokenized_doc, papers):
    str_doc = ""
    for token in tokenized_doc:
        str_doc += token + ' '    

    similarity_list = []
    for row in papers.itertuples():
        similarity = []
        # print(row.abstract_clean)
        # similarity.append(tf_idf_similarity(papers["title_kor"][i], data["title_kor"]))
        similarity.append(tf_idf_similarity(row.abstract_clean, str_doc))
        similarity.append(tf_idf_similarity(row.keyword_clean, str_doc))
        score = (0.7*similarity[0] + 0.3*similarity[1])# + 0.05*similarity[2])
        similarity_list.append((row.id, score, similarity))
        # print(similarity)

    # print(similarity_list)
    similarity_list = sorted(similarity_list, key=lambda sim: sim[1], reverse=True)
    # # print(similarity)

    df = pd.DataFrame()
    for i in range(0, 10):
        print(similarity_list[i])
        similarity_paper = papers[papers['id']==similarity_list[i][0]]
        df = pd.concat([similarity_paper, df])
    #
    print(df)

def recommend(tokenized_doc, classes, keywords):
    results = []
    papers = pd.read_pickle("./keyword_space.pkl")
    print(len(classes))
    if len(classes) > 1:
        results.append(classes[0][0])
        results.append(classes[1][0])
    elif len(classes) == 1 and classes[0] != '':
        is_subject = papers['subject'] == classes[0]
        papers = papers[is_subject]
    else:
        print("%#")
        papers = papers
    
    papers_df = papers
    # print(papers_df)
    papers_df['keyword_clean'] = papers['keyword_clean'].str.split(' ')
    papers_df = papers.explode('keyword_clean')
    # print(papers_df)
    papers_df.dropna(subset=['keyword_clean'])

    contains = pd.DataFrame()
    for key in keywords:
        contains = pd.concat([contains, papers_df[papers_df['keyword_clean'].str.contains(key)]])
    contains = contains.drop_duplicates(['id'])
    contains_df = contains.head(5)
    # print(contains_df['id'].tolist())
    # print(contains_df['title_kor'].tolist())
    print(contains_df['keyword_kor'])
    print(contains_df['keyword_clean'])
    return contains_df['id'].tolist(), contains_df['title_kor'].tolist(),contains_df['keyword_kor'].tolist()


if __name__ == '__main__':
    keywords = ['Textile', 'Handloom', 'structure']   # 요약된 논문의 keyword
    abstract = "The effects of flow field upon the distribution of ionic concentration, electric potential, concentration boundary layer thickness, and electric current density were investigated. A modified numerical scheme is proposed to simulate the corresponding electrochemical system which is governed by nonlinear partial differential equations. Seven types of geometries and various flow fields with Reynolds numbers up to 2100 are considered. The obtained results indicate the current numerical method can successfully simulate the increase of current density on the cathode as the applied potential cell increases, and that rise will continue until the limiting current density is reached. To predict the effect of fluid flow, the proposed scheme is applied for various Peclet numbers. The increase of current density for Peclet numbers between 1 and 104 is quite evident. But for large Peclet numbers between 104 and 107 , the current density increases gradually. The results also show that as the anode size is doubled, the maximum current density occurs at the leading and trailing edges. However, if the cathode size is doubled, the maximum current density occurs at the center regions of it. Knowing the regions where current density is extremum helps electochemical system designers to control the parameters of the corresponding process."
    # abstract = data_preprocessing(abstract) # 요약된 논문의 abstract 데이터 전처리
    classes = []    # 요약된 논문의 분류
    # classes = data_classification(abstract) # 요약된 논문의 분류 구하기
    recommend(abstract, classes, keywords)

