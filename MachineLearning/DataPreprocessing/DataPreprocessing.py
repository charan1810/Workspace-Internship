# Importing the necessary libraries
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
# Load the dataset
dataset = pd.read_csv('pima-indians-diabetes.csv')
# Identify missing data (assumes that missing data is represented as NaN)
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values
# Print the number of missing entries in each column
np.sum(np.isnan(x),axis=1)
# Configure an instance of the SimpleImputer class
imputer=SimpleImputer()
# Fit the imputer on the DataFrame
imputer.fit(x)
# Apply the transform to the DataFrame
x = imputer.transform(x)
#Print your updated matrix of features
print(x)