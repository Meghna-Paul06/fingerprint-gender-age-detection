import pandas as pd
import scipy
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from centroid import centroid
def knn(i):
    #directory= '/Users/Meghna/Desktop/project'
    fp=pd.read_table('fpdataset.txt','\t')
    prediction1=dict(zip(fp.gender_label.unique(),fp.gender.unique()))
    prediction2=dict(zip(fp.age_label.unique(),fp.age.unique()))
    X=fp[['centroidx','centroidy','inter_ridge','deg1','deg2']]
    y=fp['gender_label']
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=4)
    knn_gender=KNeighborsClassifier(n_neighbors=5)
    knn_gender.fit(X,y)
    KNeighborsClassifier(algorithm='auto', leaf_size=30,metric='minkowski', metric_params=None,n_jobs=1, n_neighbors=5, p=2,weights='uniform')
    X1=fp[['centroidx','centroidy','inter_ridge']]
    y1=fp['age_label']
    X1_train,X1_test,y1_train,y1_test=train_test_split(X1,y1,test_size=0.3,random_state=4)
    knn_age=KNeighborsClassifier(n_neighbors=5)
    knn_age.fit(X1,y1)
    KNeighborsClassifier(algorithm='auto', leaf_size=30,metric='minkowski', metric_params=None,n_jobs=1, n_neighbors=5, p=2,weights='uniform')
    centroidx,centroidy,inter_ridge,deg1,deg2=centroid(i)
    gender=knn_gender.predict([[centroidx,centroidy,inter_ridge,deg1,deg2]])
    age=knn_age.predict([[centroidx,centroidy,inter_ridge]])
    return(prediction1[gender[0]] , prediction2[age[0]])


