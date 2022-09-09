import pandas as pd
import numpy as np
import math
from collections import defaultdict

train=pd.read_csv("./data/a_base.csv")
test=pd.read_csv("./data/a_test.csv")

totaluser=train['user'].unique()
list_user=[]
list_item=[]
list_rate=[]

#vec1=u1[u1.item.isin()]

def recommend(user,num=10):
    #find similarity between user and other uesr.
    user_similarity = [] 
    for other_user in train['user'].unique():
        if (other_user == user):
        	continue
        common_movies = find_common_movie(user,other_user)
        common_len=len(common_movies)
        if(common_len>=5):
        	sim = cal_user_similarity_with_movie_rating(user,other_user,common_movies)
        elif(common_len==0):
        	sim=0
        else:
        	sim = cal_user_similarity_with_movie_rating(user,other_user,common_movies)*(common_len/5.0)
        user_similarity.append([other_user,sim])
    
    #find top 10 similar user
    user_similarity = np.array(user_similarity)
    sorted_index = np.argsort(user_similarity, axis=0)[:,1][::-1][:10]
    similar_users = user_similarity[:,0][sorted_index]
    print(similar_users)
    
    
    
    #find the movie the user haven't seen
    seen_movies = train.loc[train["user"]==user,"item"].values
    not_seen_movies = defaultdict(list) 
    for similar_user in similar_users:
        movies = train.loc[train.user==similar_user,["item","rate"]].values.tolist()
        if isinstance(movies[0], list):
            for movie in movies:
                if movie[0] in seen_movies:
                    continue
                not_seen_movies[movie[0]].append(movie[1]) 
        elif movies[0] not in seen_movies:
        	not_seen_movies[movies[0]].append(movies[1])
    creattable(user,not_seen_movies)

                
    
def creattable(user,not_seen_movies):
	for item,rate in not_seen_movies.items():
		list_user.append(user)
		list_rate.append(round(sum(rate)/len(rate)))
		list_item.append(item)


def find_common_movie(user1,user2):
    """找尋兩個uesr共同觀看過電影"""
    s1 = set((train.loc[train["user"]==user1,"item"].values))
    s2 = set((train.loc[train["user"]==user2,"item"].values))
    return s1.intersection(s2)


def cosine_similarity(vec1, vec2):
    """
    計算兩個向量之間的餘弦相似性
    :param vec1: 向量 a 
    :param vec2: 向量 b
    :return: sim
    """
    vec1 = np.mat(vec1)
    vec2 = np.mat(vec2)
    num = float(vec1 * vec2.T)
    denom = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    cos = num / denom
    return cos

def cal_user_similarity_with_movie_rating(user1,user2,movies_id):
    """計算兩個user對於特定電影評分的相似度"""
    u1 = train[train["user"]==user1]
    u2 = train[train["user"]==user2]
    vec1 = u1[u1.item.isin(movies_id)].sort_values(by="item")["rate"].values
    vec2 = u2[u2.item.isin(movies_id)].sort_values(by="item")["rate"].values
    return cosine_similarity(vec1, vec2)


for i in totaluser:
	recommend(i,num=10)
table={"user":list_user,"item":list_item,"rate":list_rate}
output=pd.DataFrame.from_dict(table)
output.to_csv("./predict.csv")