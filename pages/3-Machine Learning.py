import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import sklearn as sk
import GetDataFrame as gf


def MapColIntoInteger(Vehicle_df):
    from sklearn.preprocessing import LabelEncoder
    lb = LabelEncoder()
    Vehicle_df['Brand'] = lb.fit_transform(Vehicle_df['Brand'])
    Vehicle_df['Car/Suv'] = lb.fit_transform(Vehicle_df['Car/Suv'])
    Vehicle_df['BodyType'] = lb.fit_transform(Vehicle_df['BodyType'])
    Vehicle_df['Transmission'] = lb.fit_transform(Vehicle_df['Transmission'])
    Vehicle_df['DriveType'] = lb.fit_transform(Vehicle_df['DriveType'])
    Vehicle_df['UsedOrNew'] = lb.fit_transform(Vehicle_df['UsedOrNew'])

    return Vehicle_df

def SlecetIntegerCols(Vehicle_df):
    Icolumns = ['Brand','Year','Car/Suv','UsedOrNew','Transmission','FuelConsumption','CylindersinEngine','Kilometres','DriveType','BodyType','Doors','Seats','Price']
    Vehicle_df = Vehicle_df[Icolumns]
    Vehicle_df = Vehicle_df[ Vehicle_df['Price'] < 100000 ]
    Vehicle_df = Vehicle_df[ Vehicle_df['Price'] > 1000 ]
    return Vehicle_df


df = gf.GetCleanData()
df = MapColIntoInteger(df)
df = SlecetIntegerCols(df)
st.write(df.dtypes)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import accuracy_score


X , y = df.drop(['Price'] ,axis=1) , df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2 ,random_state=42)


from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accu =   sum(y_pred == y_test) / len(y_test) 
st.write("accuracy score:", accu)



model = LinearRegression()
model.fit(X_train , y_train)

y_test_prediction = model.predict(X_test)
y_train_prediction = model.predict(X_train)
mae = mean_absolute_error(y_test, y_test_prediction)
mse = mean_squared_error(y_test, y_test_prediction)
rmse = np.sqrt(mse)

r2_test = r2_score(y_test, y_test_prediction)
r2_train = r2_score(y_train, y_train_prediction)
st.write("Mean Absolute Error (MAE):", mae)
st.write("Mean Squared Error (MSE):", mse)
st.write("R-squared for Test(Coefficient of Determination):", r2_test)
st.write("R-squared for Train(Coefficient of Determination):", r2_train)
#st.write("Accuracy Score:", accuracy)

st.write(''' \n the model doesn't overfit or underfit becouse the R^2 of traning close to validation and test
         but the model in general is not perfect and we can use another model to get nore accurce like random forest''')






Forestreg = RandomForestRegressor().fit(X_train, y_train)
score = Forestreg.score(X_train, y_train)
y_predition = Forestreg.predict(X_test)
mae = mean_absolute_error(y_test, y_predition)
mse = mean_squared_error(y_test, y_predition)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_predition)
st.write(f"Mean Absolute Error (MAE) f: {mae:.2f}")
st.write(f"Mean Squared Error (MSE) f: {mse:.2f}")
st.write(f"Root Mean Squared Error (RMSE) f: {rmse:.2f}")
st.write(f"Score f:{score*100}")



fig = plt.figure(figsize=(16, 6))

sb.scatterplot(x=y_test, y=y_predition, color='green', alpha=0.9, edgecolor='k', s=80)
sb.regplot(x=y_test.astype(float), y=y_predition.astype(float), scatter=False, color='r')

plt.xlabel("Actual Values", fontsize=14)
plt.ylabel("Predicted Values", fontsize=14)
plt.title("Model Performance - Actual vs. Predicted Values", fontsize=16)
st.pyplot(fig)



#plt.scatter(x=y_train, y=y_train_prediction, c='lightblue', alpha=0.3)
#plt.plot(x=y_test, y=y_test_prediction, c='red', alpha=0.3)
#plt.xlabel("Predicted Values")
#plt.ylabel("Residuals")
#st.pyplot(preFig)