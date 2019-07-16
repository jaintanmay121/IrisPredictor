
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('Iris.csv')

x=df.drop(['Id','Species'],axis=1)
y=df['Species']


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

scores=[]
for k in range(1, 50):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    scores.append(accuracy_score(y_test, y_pred))


knn = KNeighborsClassifier(n_neighbors=np.argmax(scores)+1)
knn.fit(x, y)

'''
l=[]
for i in x.columns:
    p=float(input( f" Enter {i}:( {min(x[i])} - {max(x[i])} ) " ))
    l.append(p)

iris=knn.predict([[l[0],l[1],l[2],l[3]]])
print(f"It is an {iris[0] }")
'''

def irp(sl,sw,pl,pw):
    res=knn.predict([[float(sl),float(sw),float(pl),float(pw)]])
    return str(res[0])
