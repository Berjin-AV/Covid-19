import numpy as np
import pandas as pd

"""
#code to convert to dataframe
mydataset = {'cars':['bmw','benz','audi'],'price':[10,20,30]}
mydf=pd.DataFrame(mydataset)
print(mydf)
print(mydataset)

# code to create a series
l = [34, 543, 45, 89, 43, 53]
myseries=pd.Series(l)
print(myseries)
print(myseries[0])

# code to create label in  series
l = [34, 543, 45, 89, 43, 53]
myseries=pd.Series(l,index=["x","y","z","a","b","c"])
print(myseries)
print(myseries['y'])


mydataset = {'cars':['bmw','benz','audi'],'price':[10,20,30]}
df=pd.DataFrame(mydataset)
print(df.loc[[0,1]])

df=pd.read_csv("D:\data.csv")
# print(df)
# print(df.head(15))
# print(df.tail())
# print(df.info())

mydataset = {'cars':['bmw','benz','audi'],'price':[10,20,30]}
mydf=pd.DataFrame(mydataset)
print(mydf.info())
print(mydf.describe())"""

# mdataset={'bikes':['Royal Enfield','Harley','R15'],'price':[30000,20000,50000]}
# mydf=pd.DataFrame(mdataset)
# print(mydf)

# mydataset=pd.read_csv("D:\data.csv")
# mydf=pd.DataFrame(mydataset)
# print(mydf.describe())

mydataset = {'cars':['bmw','benz','audi'],'price':[10,20,30],'Mileage':[15,12,16]}
mydf=pd.DataFrame(mydataset)
mydf.columns.values[1]='PRICE'
print(mydf)

# mydataset = {'Name':['Berjin','Abinesh','Rikson','Jasper'],'Age':[21,25,18,24]}
# mydf=pd.DataFrame(mydataset)
# Address=['Trivandrum','Marthandam','Chennai','Coimbatore']
# mydf ['Address']=Address
# print(mydf.shape)


# mydataset=pd.read_csv("D:\data.csv")
# mydf=pd.DataFrame(mydataset)
# print(mydf.fillna(0))
# print(mydf.info())


mydataset=pd.read_csv("C:\\Users\\avber\\Downloads\\missing_data.csv")
mydf=pd.DataFrame(mydataset)
# print(mydf)
# print(mydf.shape)
# print(mydf.isnull())
# print(mydf.info())
# print(mydf.describe())
# date_count=mydf['Date'].isna().sum()
# print(date_count)
# print(mydf.info())
# calories_count=mydf['Calories'].isna().sum()
# print(calories_count)

# print(mydf.isna().sum().sum())
# mydf['Calories'].fillna(mydf['Calories'].mean(),inplace=True)
# mydf['Date'].values[22]='\'2020/12/22\''
# mydf.replace(to_replace=np.NaN,value=99)         # Error
# mydf['Calories'].fillna(mydf['Calories'].mean(),inplace=True)
# mydf['Date'].values[22]='\'2020/12/22\''
# mydf['Date'].values[26]='\'2020/12/26\''
# mydf['Date']=pd.to_datetime(mydf['Date'])        #Error
# mydf.drop(mydf.Calories,axis='columns')             #Error
# print(mydf)


#pad , bfill                                       #Error