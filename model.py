from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pickle
import pandas as pd


data = pd.read_csv("C:/Users/kaush/Downloads/DS/data.csv")
y = data['label']
x = data.drop(['label'], axis = 1)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

knn_clf=KNeighborsClassifier()
knn_clf.fit(x_train,y_train)
y_pred=knn_clf.predict(x_test)

with open('C:/Users/kaush/Downloads/DS/knn_clf.pkl', 'wb') as model_file:
    pickle.dump(knn_clf, model_file)

