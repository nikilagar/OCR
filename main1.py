import pandas as pd
import random

from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC, SVR, LinearSVR
from sklearn.model_selection import GridSearchCV, cross_val_score, KFold, cross_val_predict
from sklearn.ensemble import RandomForestClassifier, VotingClassifier, GradientBoostingClassifier, ExtraTreesClassifier
from sklearn.cross_validation import train_test_split
classification=[]
trainData=[]
for i in range(65,):
    df = pd.read_csv('data/trdata'+chr(i)+'.csv')
    trainData += df.values.tolist()
    df = pd.DataFrame()
    df = pd.read_csv('data/clasArr'+chr(i)+'.csv')
    classification += df.values.tolist()[0]

X_trainData, X_test, y_trainData, y_test = train_test_split(trainData,classification, random_state=int(random.random()*1000))

alg2 = LinearSVC(C = 5)
alg2 = alg2.fit(X_trainData, y_trainData)
scores = cross_val_score(alg2, X_test , y_test, cv = 10)
print("LinearSVC accuracy:", sum(scores)/len(scores))

alg = RandomForestClassifier(random_state=1, n_estimators=28, max_depth = 9, min_samples_split=10, min_samples_leaf=8)
alg.fit(X_trainData, y_trainData)
scores = cross_val_score(alg, X_test, y_test, cv = 15)
#print('Random Forest Scores list =', scores)
print('Random Forest average score = ', sum(scores)/len(scores))

alg1 = LogisticRegression(C=.9, max_iter=80)
alg1 = alg1.fit(X_trainData, y_trainData)
scores = cross_val_score(alg1, X_test , y_test, cv = 10)
print("LogisticRegression accuracy:", sum(scores)/len(scores))
