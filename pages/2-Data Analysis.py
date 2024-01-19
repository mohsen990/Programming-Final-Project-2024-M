import streamlit as st
import pandas as pd
import numpy as np
import os 
FileName = "Australian Vehicle Prices.csv"
MainRoot = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Path  = str(MainRoot) + "\\data\\" + FileName

print(Path)

df = pd.read_csv(Path) 
ss = df.head(10).info()
st.write(ss)
