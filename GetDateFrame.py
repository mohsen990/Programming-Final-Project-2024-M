import pandas as pd
from settings import Path , AboutDataSet , KeyFeaturesInDataSet

#Get UncleanData ------------------------------------------------------------------
def GetUncleanData():
    Australian_Vehicle_Prices_db =  pd.read_csv(Path) 
    return Australian_Vehicle_Prices_db


# Data Cleaning -------------------------------------------------------------------
def GetCleanData():
    # extract numbers in cell And remove part of string in each cell 
    df = GetUncleanData()
    df.Doors = df.Doors.str.extract('(\\d+)')
    df.Seats = df.Seats.str.extract('(\\d+)')
    df.CylindersinEngine = df.CylindersinEngine.str.extract('(\\d+)')
    df.Price = df.Price.str.extract('(\\d+)')
    df.Kilometres = df.Kilometres.str.extract('(\\d+)')
    df.FuelConsumption = df.FuelConsumption.str.extract('(\\d+)')
    
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

    return df