# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
dataset = pd.read_csv(r"Cyour_datafile_path")

# Separate features and target variable
X = dataset.drop(['application_id', 'gender', 'international', 'race', 'admission'], axis=1).values
y = dataset['admission'].values  # Assuming 'admission' is the target variable

# Check and fill missing values if present
# Check for numeric columns first
nan_mask = np.isnan(X).any(axis=1)  # Check for any NaN values in the feature set
print("Rows with NaN in features:", np.where(nan_mask)[0])

# If you find NaN values, you can choose to fill them or remove those rows
# For demonstration, let's remove rows with NaN values
X = X[~nan_mask]
y = y[~nan_mask]  # Ensure y is also updated accordingly

# Preprocess categorical columns (assuming column indices for OneHotEncoder)
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder

# Assuming column indices for 'major' and 'work_industry' are 1 and 4 respectively
ct = ColumnTransformer(
    transformers=[
        ('encoder', OneHotEncoder(), [1, 4])
    ], 
    remainder='passthrough'
)

X = ct.fit_transform(X)  # Transform X into one-hot encoded format
# Note: The output of fit_transform is already a dense array, no need for toarray()

# Encode the target variable
le = LabelEncoder()
y = le.fit_transform(y)

# Split the dataset into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# Feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# SVM Classifier preparation
from sklearn.svm import SVC
classifier = SVC(kernel='rbf', random_state=0)
classifier.fit(X_train, y_train)

# Make predictions
y_pred = classifier.predict(X_test)

# Print comparison table
comparison = np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), axis=1)
print("Comparison (Predicted vs Actual):")
print(comparison)

# Check the model confusion matrix and the accuracy score
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
acs = accuracy_score(y_test, y_pred)

print('Confusion matrix:\n', cm)
print('Accuracy score:', acs)
