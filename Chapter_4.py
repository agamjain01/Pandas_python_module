'''
  In chapter 4  we are see the how handle missing data.
  
'''

# isnull() --> that show null data in data set 

import pandas as pd
dataframe={
    "Name" : ["Agam Jain","Harsh Modi","Hardik Balsunni","Dev Pancholi"],
    "Age":[20,21,None,22],
    "State":["UP","MP",None,"MP"],
    "Salary":[None,65000,45000,30000]
}


dS= pd.DataFrame(dataframe)

print(dS.isnull())

# how deal  the none data -->  1. remove null data 2. fill the none data

dS.dropna(axis=0,inplace=True) 

print(dS)

# 2. Fill null value

dataframe={
    "Name" : ["Agam Jain","Harsh Modi","Hardik Balsunni","Dev Pancholi"],
    "Age":[20,21,None,22],
    "State":["UP","MP",None,"MP"],
    "Salary":[None,65000,45000,30000]
}


dS= pd.DataFrame(dataframe)

dS.fillna(dS["Age"].min(),inplace=True)
print(dS)

# 3. interpolate method

dataframe={
    "Name" : ["Agam Jain","Harsh Modi","Hardik Balsunni","Dev Pancholi"],
    "Age":[20,21,None,22],
    "State":["UP","MP",None,"MP"],
    "Salary":[None,65000,45000,30000]
}


dS= pd.DataFrame(dataframe)

dS["Age"] = dS['Age'].interpolate(method="linear")

print(dS)