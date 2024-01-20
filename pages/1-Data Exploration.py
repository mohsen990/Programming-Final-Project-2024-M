import streamlit as st
import pandas as pd
import numpy as np

from settings import Path , AboutDataSet , KeyFeaturesInDataSet
import GetDateFrame as gf

st.subheader("About Dataset:")
st.markdown( AboutDataSet )

st.write(":blue[Key Features:]")
with st.expander("See Key Features:"):
   st.markdown( KeyFeaturesInDataSet )
   

# read svc file --> direction is on the setting file
df = gf.GetUncleanData()
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


sumNa = df.isna().sum()
with st.expander("See Sum of Null values in each columns before cleaning"):
     strs = ""
     for item in sumNa.index:
         strs = strs +'\t\t' +item + ' : :red[' + str(sumNa[item]) +']'
     st.write(strs)



CleanDataFrame = gf.GetCleanData()
sumNa = CleanDataFrame.isna().sum()
with st.expander("See Sum of Null values in each columns after cleaning"):
     strs = ""
     for item in sumNa.index:
         strs = strs +'\t\t' +item + ' : :red[' + str(sumNa[item]) +']'
     st.write(strs)


#Filter Data exploration
     
ListOfBrands = ["Select Brand"]
ListOfBrands.extend(CleanDataFrame.Brand.drop_duplicates().tolist())
SelectedBrand = st.selectbox("Filter By Brand" ,ListOfBrands )
if SelectedBrand == "Select Brand":
    FiltterdDf = ""
else:
   FiltterdDf =  CleanDataFrame[ CleanDataFrame.Brand == SelectedBrand ]
st.write(FiltterdDf)


ListOfBody = ["Select BodyTpe"]
ListOfBody.extend(CleanDataFrame.BodyType.drop_duplicates().tolist())
SelectedBody = st.selectbox("Filter By BodyType" ,ListOfBody )
if SelectedBody == "Select BodyTpe":
    FiltterdDf2 = ""
else:
   FiltterdDf2 =  CleanDataFrame[ CleanDataFrame.BodyType == SelectedBody ]
st.write(FiltterdDf2)
