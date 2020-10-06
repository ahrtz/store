from sklearn.decomposition import TruncatedSVD
from scipy.sparse.linalg import svds

import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd
import numpy as np
import warnings
import sqlite3
from sklearn.metrics.pairwise import cosine_similarity

# 아이템 기반 협업 필터링(item based collaborative filtering)
def get_item_based_collabor(subject):  ## 이건 스크랩 별로 없어도
    ## scrap: 장고 dbsql 접근
    con = sqlite3.connect("./db.sqlite3")
    cur = con.cursor()
    query = cur.execute("SELECT * FROM reports_scraps")
    cols = [column[0] for column in query.description]
    result = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
    scrap_data = pd.DataFrame.from_records(data=result, columns=cols)
    paper_data = pd.read_pickle("all_data.pkl")
    # print(scrap_data)

    scrap_data['rating'] = [1 for _ in range(len(scrap_data))]
    paper_data['summary_id'] = paper_data['id']
    # print(scrap_data)
    # print(paper_data)

    user_scrap_paper = pd.merge(scrap_data, paper_data, on='summary_id')
    print("1",user_scrap_paper) 

    scrap_user_paper = user_scrap_paper.pivot_table('rating', index='title_kor', columns='user_id')
    user_scrap_paper = user_scrap_paper.pivot_table('rating', index='user_id', columns='title_kor')
    scrap_user_paper.fillna(0, inplace=True)
    print("2",user_scrap_paper)
    print("3",scrap_user_paper)

    item_based_collabor = cosine_similarity(scrap_user_paper, scrap_user_paper)

    item_based_collabor_df = pd.DataFrame(data=item_based_collabor, index=scrap_user_paper.index, columns=scrap_user_paper.index)
    print(item_based_collabor_df)
    
    return item_based_collabor_df['Bio-EPDM/tungsten oxide nanocomposite foam with improved thermal storage and sea water resistance'].sort_values(ascending=False)[:6]

# 잠재 요인(latent factor)기반 - 협업 필터링 Matrix Factorization
# 개인에게 맞춤형이 추천이 아닌, 특정 논문과 비슷한 논문 추천
def get_matrix_factorization(title): # 이거 사용하는걸로 대신 스크랩 많아야 된다
    ## scrap: 장고 dbsql 접근
    con = sqlite3.connect("./db.sqlite3")
    cur = con.cursor()
    query = cur.execute("SELECT * FROM reports_scraps")
    cols = [column[0] for column in query.description]
    result = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
    scrap_data = pd.DataFrame.from_records(data=result, columns=cols)
    paper_data = pd.read_pickle("all_data.pkl")

    scrap_data['rating'] = [1 for _ in range(len(scrap_data))]
    paper_data['summary_id'] = paper_data['id']

    user_scrap_paper = pd.merge(scrap_data, paper_data, on='summary_id')
    user_scrap_paper = user_scrap_paper.pivot_table('rating', index='user_id', columns='title_kor').fillna(0)
    print(user_scrap_paper.shape)
    
    scrap_user_paper = user_scrap_paper.values.T
    print(scrap_user_paper.shape)
    
    # latent값 => user data가 많이 쌓이면 다른것도 가능
    SVD = TruncatedSVD(n_components=2)
    matrix = SVD.fit_transform(scrap_user_paper)
    matrix.shape
    
    corr = np.corrcoef(matrix)
    print(corr.shape)
    corr2 = corr[:200, :200]
    print(corr2.shape)

    plt.figure(figsize=(16, 10))
    sns.heatmap(corr2)
    
    paper_title = user_scrap_paper.columns
    paper_title_list = list(paper_title)
    # title로 바껴야함
    coffey_hands = paper_title_list.index('Bio-EPDM/tungsten oxide nanocomposite foam with improved thermal storage and sea water resistance')
    corr_coffey_hands = corr[coffey_hands]
    print(list(paper_title[(corr_coffey_hands >= 0.9)])[:50])

# 개인 히스토리를 기반으로 논문 추천
def get_matrix_factorization_user_based():
    scrap_data = pd.read_pickle(".pkl")
    paper_data = pd.read_pickle(".pkl")
    
    df_user_scrap_paper = scrap_data.pivot(
        index='user_id',
        columns='subject',
        values='rating'
    ).fillna(0)
    df_user_scrap_paper.head()
    
    matrix = df_user_scrap_paper.as_matrix()
    user_papers_mean = np.mean(matrix, axis=1)
    matrix_user_mean = matrix - user_papers_mean.reshape(-1,1)
    
    U, sigma, Vt = svds(matrix_user_mean, k=12)
    sigma = np.diag(sigma)
    sigma.shape
    sigma[0]
    
    svd_user_predicted_papers = np.dot(np.dot(U, sigma), Vt) + user_papers_mean.reshape(-1, 1)
    df_svd_preds = pd.DataFrame(svd_user_predicted_ratings, columns = df_user_movie_ratings.columns)
    df_svd_preds.head()
    
    already_rated, predictions = recommend_paper_using_matrix_factorization(df_svd_preds, 330, paper_data, scrap_data, 10)
    
def recommend_paper_using_matrix_factorization(df_svd_preds, user_id, org_paper_data, org_scrap_data, num_recommned=5):
    user_row_number = user_id-1
    sorted_user_predictions = df_svd_preds.iloc[user_row_number].sort_values(ascending=False)
    user_data = org_scrap_data[org_scrap_data.user_id == user_id]
    user_history = user_data.merge(org_paper_data, on='summary_id').sort_values(['rating'], ascending=False)
    
    recommendations = org_paper_data[~org_paper_data['summary_id'].isin(user_history['summary_id'])]
    recommendations = recommendations.merge(pd.DataFrame(sorted_user_predictions).reset_index(), on='summary_id')
    recommendations = recommendations.rename(columns={user_row_number: 'Predictions'}).sort_values('Predictions', ascending = False).iloc[:num_recommendations, :]
    
    return user_history, recommendations

if __name__ == '__main__':
    # print(get_item_based_collabor('subject'))
    get_matrix_factorization("  ")



# 1. scrap확인해서 해당 id의 값이 없으면 