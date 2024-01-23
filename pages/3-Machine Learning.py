import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import sklearn as sk
import GetDataFrame as gf

#-- Map string format columns with integer values --------------------------------------------

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

#--- Select Some columns with integer datatype from cleaned data set

def SlecetIntegerCols(Vehicle_df):
    Icolumns = ['Brand','Year','Car/Suv','UsedOrNew','Transmission','FuelConsumption','CylindersinEngine','Kilometres','DriveType','BodyType','Doors','Seats','Price']
    Vehicle_df = Vehicle_df[Icolumns]
    Vehicle_df = Vehicle_df[ Vehicle_df['Price'] < 120000 ]
    Vehicle_df = Vehicle_df[ Vehicle_df['Price'] > 1000 ]
    return Vehicle_df

#--Prediction model -------------------------------------------------------------------------

df = gf.GetCleanData()
df = MapColIntoInteger(df)
df = SlecetIntegerCols(df)
#st.write(df.dtypes)

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


#-- Model 1 : Linear Regression To predict Price -------------------------------------------
model = LinearRegression()
model.fit(X_train , y_train)

y_test_prediction = model.predict(X_test)
mae = mean_absolute_error(y_test, y_test_prediction)
mse = mean_squared_error(y_test, y_test_prediction)
rmse = np.sqrt(mse)
r2_test = r2_score(y_test, y_test_prediction)

y_train_prediction = model.predict(X_train)
maeTrain = mean_absolute_error(y_train, y_train_prediction)
mseTrain = mean_squared_error(y_train, y_train_prediction)
rmseTrain = np.sqrt(mseTrain)
r2_train = r2_score(y_train, y_train_prediction)

st.subheader(':blue[Model 1:] Linear Regression')
st.write("Mean Absolute Error for Test (MAE) :", mae)
st.write("Mean Squared Error for Test  (MSE):", mse)
st.write("R-squared for Test (Coefficient of Determination):", r2_test)

st.write("\n____________________________________________________________________")
st.write("Mean Absolute Error for Train (MAE) :", maeTrain)
st.write("Mean Squared Error for Train  (MSE):", mseTrain)
st.write("R-squared for Train (Coefficient of Determination):", r2_train)
st.write("\n____________________________________________________________________")
st.write(''' \n :red[Result:] The model doesn't work very well becouse the R-squared of traning close to validation and test
         so model is not good and we can try another model to get nmore accurce.''')
st.write("\n____________________________________________________________________")

#-- Model 2 : Random Forest Regression To predict Price -------------------------------------------


Forestreg = RandomForestRegressor().fit(X_train, y_train)
score = Forestreg.score(X_train, y_train)
y_predition = Forestreg.predict(X_test)
mae = mean_absolute_error(y_test, y_predition)
mse = mean_squared_error(y_test, y_predition)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_predition)

st.subheader(':blue[Model 2:] Random Forest Regression')
st.write(f"Mean Absolute Error (MAE):" , mae)
st.write(f"Mean Squared Error (MSE):", mse)
st.write(f"Root Mean Squared Error (RMSE):" ,rmse)
st.write(f"Score:" ,score*100)
#st.write(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
st.write("\n____________________________________________________________________")
st.write(''' \n :red[Result:] The model seems to perform better than the previous one.''')
st.write("\n____________________________________________________________________")
#-----Visualization of Random Forest Regression model --------------------------------------------

st.subheader('Visualization')
st.write("Visualization of Random Forest Regression model:\n")
fig = plt.figure(figsize=(16, 6))
sb.scatterplot(x=y_test, y=y_predition, color='green', alpha=0.9, edgecolor='k', s=80)
sb.regplot(x=y_test.astype(float), y=y_predition.astype(float), scatter=False, color='r')

plt.xlabel("Actual Price", fontsize=14)
plt.ylabel("Predicted Price", fontsize=14)
plt.title("Actual vs Predicted Price", fontsize=18)
st.pyplot(fig)

#------------------------End------------------------------------------------------------------------
