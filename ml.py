import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import warnings
import pickle
warnings.filterwarnings("ignore")

data = pd.read_csv("Iris.csv")
data = np.array(data)

X = data.drop(["Id", "Species"])
y = data.Species
y = y.astype('int')
X = X.astype('int')
# print(X,y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

clf= DecisionTreeClassifier()
clf.fit(Xtrain,ytrain)

pickle.dump(clf,open('model.pkl','wb'))

