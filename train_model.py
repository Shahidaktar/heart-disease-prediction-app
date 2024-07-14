import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

data = pd.read_csv('heart.csv')

data['trestbps']=np.log(data['trestbps'])
data['chol']=np.log(data['chol'])
data['thalach']=np.log(data['thalach'])

X=data.drop(columns='target', axis=1)
y=data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

rand_clf = RandomForestClassifier(criterion = 'entropy', max_depth = 10, max_features = 0.5, min_samples_leaf = 2, min_samples_split = 3, n_estimators = 130)
rand_clf.fit(X_train, y_train)

pickle.dump(rand_clf, open("heart.pkl",'wb'))

print("Model trained and saved as heart.pkl")