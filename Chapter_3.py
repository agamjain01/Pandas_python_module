'''
   In a chapter three we are see how to modified the data set 
   1. adding new columns 
   2. update the particular rows 
   3. delete the column 
'''

# In data set insert any new columns we are two type .
# 1. direct method --> df["New_column_name "]=[new data] that is add the any where 
# 2. By using insert method--> df.inaert(index,"New_column_name","new_data")


import pandas as pd
dataframe={
    "Name" : ["Agam Jain","Harsh Modi","Hardik Balsunni","Dev Pancholi"],
    "Age":[20,21,23,22],
    "State":["UP","MP","UP","MP"],
    "Salary":[25000,65000,45000,30000]
}


dS= pd.DataFrame(dataframe)

dS["ID"]=["001","002","003","004"]

print(dS)


del dS["ID"]

print(dS)


dS.insert(0,"ID",["001","002","003","004"])

print(dS)


# 2. when update the rows then we are use loc method

dS.loc[2,"Salary"]=200000

print(dS)


# 3. drop any column when we are use drop  method

dS.drop(columns=["Age"],inplace=True)
print(dS)