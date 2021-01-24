import numpy as np
import pandas as pd
from time import time
import os
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

data = pd.read_csv("Crops.csv")
crop_pred = data['Crop']
crop_input = data.drop('Crop', axis =1)
crop_transform = pd.DataFrame(data =crop_input)
additional_info = pd.read_csv('Prediction.csv')

crop_transformed = crop_transform.drop('States', axis=1)
features_final = pd.get_dummies(crop_transformed)

factor = pd.factorize(data['Crop'])
data.Crop = factor[0]
definitions = factor[1]

X =features_final.iloc[:].values
y = data.iloc[:,6].values

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state= 21 )
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(max_depth =35, max_features =10 , random_state = 42 , ccp_alpha = 0.0022 , criterion="gini" )
classifier.fit(X_train, y_train)
# classifier.save("final_model.h5")
y_pred = classifier.predict(X_test)
reversefactor = dict(zip(range(77),definitions))
y_test = np.vectorize(reversefactor.get)(y_test)
y_pred = np.vectorize(reversefactor.get)(y_pred)
print(y_pred)
import joblib 
  
# Save the model as a pickle in a file 
joblib.dump(classifier, 'crop_pred.pkl') 
joblib.dump(reversefactor, 'reversefactor.pkl') 

