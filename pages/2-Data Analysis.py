import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import GetDateFrame as gf
#--------------------------------------------------------------------------------------------------
Vehicle_Prices_db = gf.GetCleanData()

#--Histogram-------------------------------------------------------------------
fig = plt.figure(figsize=(18,12))
SubFig_1 = fig.add_subplot(2,3,1)
sb.histplot(Vehicle_Prices_db[['Year']] , bins=20 , kde=True)
plt.title('Years', fontsize = 16)

SubFig_2 = fig.add_subplot(2,3,2)
sb.histplot(Vehicle_Prices_db[['Price']] , bins=20 , kde=True )
plt.title('Price', fontsize = 16)

SubFig_3 = fig.add_subplot(2,3,3)
sb.histplot(Vehicle_Prices_db[['Seats']] , bins=20 ,kde=True)
plt.title('Seats', fontsize = 16)

SubFig_4 = fig.add_subplot(2,3,4)
sb.histplot(Vehicle_Prices_db[['Doors']] , bins=20 ,kde=True)
plt.title('Doors', fontsize = 16)
plt.suptitle('Histogram of integer columns')

SubFig_5 = fig.add_subplot(2,3,5)
sb.histplot(Vehicle_Prices_db[['FuelConsumption']] , bins=20 ,kde=True )
plt.title('Fuel Consumption', fontsize = 16)


SubFig_6 = fig.add_subplot(2,3,6)
sb.histplot(Vehicle_Prices_db[['Kilometres']] , bins=20 , kde=True )
plt.title('Kilometres', fontsize = 16)
plt.suptitle('Histogram of integer columns', fontsize = 40)

st.pyplot(fig)


#--Heat map matrix-----------------------------------------------------------------

df_Number = Vehicle_Prices_db[['Year','FuelConsumption','CylindersinEngine','Kilometres','Doors','Seats','Price']]
df_Corr = df_Number.corr()
HeatFig = plt.figure(figsize=(8,6))
sb.heatmap(df_Corr  , annot=True)
plt.title('Correlation Matrix', fontsize = 20)
st.pyplot(HeatFig)

#--

CountOfTransmission = Vehicle_Prices_db['Transmission'].value_counts()
CountOfUse = Vehicle_Prices_db['UsedOrNew'].value_counts()
CountOfDoors = Vehicle_Prices_db['Doors'].value_counts()
CountOfCylinder = Vehicle_Prices_db['CylindersinEngine'].value_counts()

MainFig = plt.figure(figsize=(8,8) )
SubFig_1 = MainFig.add_subplot(2,2,1)
SubFig_1.bar(CountOfTransmission.index , CountOfTransmission.values, color = 'pink' )
plt.title("Transmission")

SubFig_2 = MainFig.add_subplot(2,2,2)
SubFig_2.bar(CountOfUse.index, CountOfUse.values , color = 'lightgreen')
plt.title("Use Or New Cars")

SubFig_3 = MainFig.add_subplot(2,2,3)
SubFig_3.bar(CountOfDoors.index , CountOfDoors.values , color = 'cyan')
plt.title("Distribution of Doors")

SubFig_4 = MainFig.add_subplot(2,2,4)
SubFig_4.bar(CountOfCylinder.index , CountOfCylinder.values , color = 'magenta')
plt.title("Cylinder In Engin")
plt.suptitle('Distribution Of Items', fontsize = 20)

st.pyplot(MainFig)

#---
CountOfBrand = Vehicle_Prices_db['Brand'].value_counts()
BrandFigure = plt.figure(figsize=(12,8))
plt.bar(CountOfBrand.index , CountOfBrand.values , color = 'darkblue')
plt.xticks(rotation=90 ,ha='right')
plt.title('Distribution Of Brands' ,fontsize = 20)
plt.xlabel('Brand' ,fontsize = 12)
plt.ylabel('Count' ,fontsize = 12)

st.pyplot(BrandFigure)

#-- -----------------------------------------------------
Top10Brand = Vehicle_Prices_db['Brand'].value_counts(ascending=True).tail(5)
PieFig = plt.figure(figsize=(8,8))
explode1 = [0, 0, 0, 0 , 0.2]
plt.subplot(2,2,1)
plt.pie(Top10Brand.values , labels= Top10Brand.index ,explode= explode1 ,autopct='%.1f%%', shadow=True)
plt.title('Top 5 Brands', fontsize = 12)

plt.subplot(2,2,2)
explode2 = [0.2, 0, 0, 0, 0, 0, 0, 0, 0]
plt.pie(CountOfCylinder.values , labels = CountOfCylinder.index , explode= explode2 , autopct='%.1f%%', shadow=True)
plt.title('Cylinders In Engine' , fontsize = 12)

plt.subplot(2,2,3)
CountOfDriveType = Vehicle_Prices_db[['DriveType']].value_counts()
plt.pie(CountOfDriveType.values , labels= CountOfDriveType.index,autopct='%.1f%%' ,shadow=True)
plt.title('Drive Type' , fontsize = 12)

plt.subplot(2,2,4)
CountOfFuelType = Vehicle_Prices_db[['FuelType']].value_counts()
explode3 = [0.1, 0, 0, 0, 0.2, 0.4, 0.4, 0.4]
plt.pie(CountOfFuelType.values ,labels=CountOfFuelType.index, explode= explode3 , autopct='%.1f%%' )
plt.title('Fuel Type' , fontsize = 12)

st.pyplot(PieFig)


#---------------------------------------------------------

pFig = plt.figure(figsize=(15,6))
GroupByYearPrice = Vehicle_Prices_db[['Year','Price']].groupby(['Year']).sum()
plt.subplot(1,2,1)
plt.plot(GroupByYearPrice.index,GroupByYearPrice.values )
plt.title("Total Price By Year" , fontsize = 20)
plt.xlabel("Year" , fontsize = 14)
plt.ylabel("Total Price" , fontsize = 14)
plt.grid()

GroupByYearKilometer = Vehicle_Prices_db[['Year','Kilometres']].groupby(['Year']).mean()
plt.subplot(1,2,2)
plt.plot(GroupByYearKilometer.index, GroupByYearKilometer.values)
plt.title("Mean Kilometer By Price" , fontsize = 20)
plt.xlabel("Year" , fontsize = 14)
plt.ylabel("Mean Kilometer" , fontsize = 14)
plt.grid()

st.pyplot(pFig)