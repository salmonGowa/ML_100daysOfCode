import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from mlxtend.feature_selection import SequentialFeatureSelector

#defining an array

data=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
#converting the array into a datafram
df=pd.DataFrame(data)

#selecting the features and the target
X=df.iloc[:,:-1]
y=df.iloc[:,-1]

#performing stepwise regression 
sfs=SequentialFeatureSelector(linear_model.LogisticRegression(),k_feature=3,forward=True,scoring='accuracy',cv=None) 
selected_features=sfs.fit(X,y)
