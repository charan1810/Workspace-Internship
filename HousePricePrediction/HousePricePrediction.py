import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset= pd.read_csv(r"C:\Users\CHARAN\Datascience-programs\MachineLeaarningPrograms\LinearRegression\HousePricePrediction\house_price.csv")

x=dataset.iloc[:,:2].values
y=dataset.iloc[:,2].values

x_test,x_train,y_test,y_train=train_test_split(x,y,test_size=0.80,random_state=42)

regressor=LinearRegression()
regressor.fit(x_train, y_train)

y_pred=regressor.predict(x_test)

comp=pd.DataFrame({'Actual':y_test,'Predicted':y_pred})
print(comp)

coeff=regressor.coef_
print(coeff)

interc=regressor.intercept_
print(interc)

sns.scatterplot(x=y_test,y=y_pred)

sns.histplot(y_test, label='Actual', color='blue', kde=True)
sns.histplot(y_pred, label='Predicted', color='red', kde=True)

plt.legend()
plt.title('Distribution of Actual vs Predicted')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()

residuals = y_test - y_pred
sns.scatterplot(x=y_test, y=residuals)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel('Actual Values')
plt.ylabel('Residuals')
plt.title('Residuals vs Actual Values')
plt.show()



print("r2 score: ",r2_score(y_test, y_pred))
print("Mean squared Error is : ",mean_squared_error(y_test, y_pred))

bias=regressor.score(x_train,y_train)
bias

f_d= [[852,2]]
f_pred=regressor.predict(f_d)
print(f_pred,"future predicted value")

variance=regressor.score(x_test,y_test) 
variance

regressor.summary()
