# Import Libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Import dataset

dataset = pd.read_csv(r"C:\Users\CHARAN\Downloads\Data (3).csv")

#Seperate features and dependent variables

x = dataset.iloc[:,:3].values
y = dataset.iloc[:,3].values

#Handling Missing values

from sklearn.impute import SimpleImputer
imputer=SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(x[:,1:3]) 
x[:,1:3]=imputer.transform(x[:,1:3])

#Encoding the categorical data

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[0])],remainder='passthrough')
x = np.array(ct.fit_transform(x)) 


#Encoding depending variable i.e., purchased column

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y=le.fit_transform(y)
