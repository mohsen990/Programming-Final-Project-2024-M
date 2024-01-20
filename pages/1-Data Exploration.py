import streamlit as st
import pandas as pd
import numpy as np

from settings import Path , AboutDataSet , KeyFeaturesInDataSet

st.subheader("About Dataset:")
st.markdown( AboutDataSet )

st.write(":blue[Key Features:]")
with st.expander("See Key Features:"):
   st.markdown( KeyFeaturesInDataSet )
   

# read svc file --> direction is on the setting file
df = pd.read_csv(Path) 
#pd.set_option('display.max_rows', None)

st.markdown('Descrition of Dataset:')
DataSetDescribe = df.describe(include='all')
st.write(DataSetDescribe)


st.write(":red[First 50 Rows of data set:]")
SelectedItem = st.selectbox("select number of rows to show" , ["select number","10","100","1000","All"])
if SelectedItem == "10":
   st.write(df.head(10))
elif SelectedItem == "100":
   st.write(df.head(100))
elif SelectedItem == "1000":
   st.write(df.head(1000))
elif SelectedItem == "All":
    st.write(df)
else:
   st.write(df.head())



# Data Cleaning 
st.write(''':blue[Cleaning Data:]
          First extract Numbers in some of columns 
         ''')

# extract numbers in cell And remove part of string in each cell 
df.Doors = df.Doors.str.extract('(\\d+)')
df.Seats = df.Seats.str.extract('(\\d+)')
df.CylindersinEngine = df.CylindersinEngine.str.extract('(\\d+)')
df.Price = df.Price.str.extract('(\\d+)')
df.Kilometres = df.Kilometres.str.extract('(\\d+)')
df.FuelConsumption = df.FuelConsumption.str.extract('(\\d+)')

sumNa = df.isna().sum()
with st.expander("See Sum of Null values in each columns before cleaning"):
     strs = ""
     for item in sumNa.index:
         strs = strs +'\t\t' +item + ' : :red[' + str(sumNa[item]) +']'
     st.write(strs)

# Delete rows from dataset with less than 5 null values 
DelColumnsNa = ['Brand', 'Year', 'Model', 'Car/Suv', 'Title', 'UsedOrNew', 'Transmission', 'Engine', 'DriveType','FuelType', 'ColourExtInt', 'BodyType', 'Price']
df.dropna(subset=DelColumnsNa, inplace=True)

# Replace Null locations with Unknown
df["Location"].fillna("Unknown" , inplace=True)

# Covert string to integer or float 
df['Year'] = df['Year'].astype('Int64')
df['Price'] = df['Price'].astype(float)
df['Kilometres'] = df['Kilometres'].astype(float)
df['CylindersinEngine'] = df['CylindersinEngine'].astype(float)
df['FuelConsumption'] = df['FuelConsumption'].astype(float)
df['Doors'] = df['Doors'].astype(float)
df['Seats'] = df['Seats'].astype(float)

# Replace null valuse with mean values of column for the columns with many number of null values 
MeanDoor = df['Doors'].mean()
MeanSeat = df["Seats"].mean()
MeanKilometre = df["Kilometres"].mean()
MeanCylindersinEngine = df["CylindersinEngine"].mean()
MeanFuelConsumption = df["FuelConsumption"].mean()

df["Doors"].fillna(MeanDoor, inplace= True)
df["Seats"].fillna(MeanSeat , inplace= True)
df["Kilometres"].fillna(MeanKilometre , inplace= True)
df["CylindersinEngine"].fillna(MeanCylindersinEngine , inplace= True)
df["FuelConsumption"].fillna(MeanFuelConsumption , inplace= True)

# Replace the vell with value '-'  with  'Other' lable
df['Transmission'] = df['Transmission'].replace('-', 'Other')
df['FuelType'] = df['FuelType'].replace('-', 'Other')
df['Engine'] = df['Engine'].replace('-','Other')

# Covert data types into number 
df['Price'] = df['Price'].astype('Int64')
df['Kilometres'] = df['Kilometres'].astype('int64')
df['CylindersinEngine'] = df['CylindersinEngine'].astype(int)
df['FuelConsumption'] = df['FuelConsumption'].astype(int)
df['Doors'] = df['Doors'].astype(int)
df['Seats'] = df['Seats'].astype(int)

# Remove duplicate rows if exists
SumDuplicate = df.duplicated().sum()
df.drop_duplicates()

sumNa = df.isna().sum()
with st.expander("See Sum of Null values in each columns after cleaning"):
     strs = ""
     for item in sumNa.index:
         strs = strs +'\t\t' +item + ' : :red[' + str(sumNa[item]) +']'
     st.write(strs)


#Filter Data exploration

ListOfBrands = ["Select Brand"]
ListOfBrands.extend(df.Brand.drop_duplicates().tolist())
SelectedBrand = st.selectbox("Filter By Brand" ,ListOfBrands )
if SelectedBrand == "Select Brand":
    FiltterdDf = ""
else:
   FiltterdDf =  df[ df.Brand == SelectedBrand ]
st.write(FiltterdDf)


ListOfBody = ["Select BodyTpe"]
ListOfBody.extend(df.BodyType.drop_duplicates().tolist())
SelectedBody = st.selectbox("Filter By BodyType" ,ListOfBody )
if SelectedBody == "Select BodyTpe":
    FiltterdDf2 = ""
else:
   FiltterdDf2 =  df[ df.BodyType == SelectedBody ]
st.write(FiltterdDf2)
