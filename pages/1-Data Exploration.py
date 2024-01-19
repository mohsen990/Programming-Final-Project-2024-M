import streamlit as st
import pandas as pd
import numpy as np
import os
import io
from settings import Path

st.subheader("About Dataset:")
st.markdown('''
            This dataset contains the latest information on car prices in Australia for the year 2023.
            It covers various brands, models, types, and features of cars sold in the Australian market. 
            It provides useful insights into the trends and factors influencing the car prices in Australia.
            The dataset includes information such as brand, year, model, car, title, used/new, transmission, 
            engine, drive type, fuel type, fuel consumption, kilometres, colour (exterior/interior), location, 
            cylinders in engine, body type, doors, seats, and price. 
            The dataset has over 16,000 records of car listings from various online platforms in Australia.
            ''')

st.write(":blue[Key Features:]")
with st.expander("See Key Features:"):
   st.markdown('''
              
            :green[Brand:] Name of the car manufacturer
            
            :green[Year:] Year of manufacture or release
            
            :green[Model:] Name or code of the car model

            :green[Car/Suv:] Type of the car (car or suv)

            :green[Title:] Title or description of the car

            :green[UsedOrNew:] Condition of the car (used or new)

            :green[Transmission:] Type of transmission (manual or automatic)

            :green[Engine:] Engine capacity or power (in litres or kilowatts)

            :green[DriveType:] Type of drive (front-wheel, rear-wheel, or all-wheel)

            :green[FuelType:] Type of fuel (petrol, diesel, hybrid, or electric)

            :green[FuelConsumption:] Fuel consumption rate (in litres per 100 km)

            :green[Kilometres:] Distance travelled by the car (in kilometres)

            :green[ColourExtInt:] Colour of the car (exterior and interior)

            :green[Location:] Location of the car (city and state)

            :green[CylindersinEngine:] Number of cylinders in the engine

            :green[BodyType:] Shape or style of the car body (sedan, hatchback, coupe, etc.)

            :green[Doors:] Number of doors in the car

            :green[Seats:] Number of seats in the car

            :green[Price:] Price of the car (in Australian dollars)

            '''
            )
   

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
ListOfOptions = ["Select Brand"]
ListOfOptions.extend(df.Brand.drop_duplicates().tolist())
SelectedBrand = st.selectbox("Filter By Brand" ,ListOfOptions )
if SelectedBrand == "Select Brand":
    FiltterdDf = ""
else:
   FiltterdDf =  df[ df.Brand == SelectedBrand ]
st.write(FiltterdDf)


# Data Cleaning 
st.write(":blue[Cleaning Data:]")
sumNa = df.isnull().sum()
st.write(sumNa)



