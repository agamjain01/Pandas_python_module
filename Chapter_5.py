"""
 In this chapter we seen the how to sorting the data and aggregation the data
 agggreation mean --> min , max ... etc
"""

# 1. sorting the data --> ds.sort_value(by=["column_name",asceding=true/false,inplace=True])
import pandas as pd
dataframe={
    "Name" : ["Agam Jain","Harsh Modi","Hardik Balsunni","Dev Pancholi"],
    "Age":[20,21,55,22],
    "State":["UP","MP","UP","MP"],
    "Salary":[50000,65000,45000,30000]
}


dS= pd.DataFrame(dataframe)
dS.sort_values(by="Age",ascending=True,inplace=True)
print(dS)
dS.sort_values(by="Age",ascending=False,inplace=True)
print(dS)


# 2. aggregation 

# dS.["Column_name"].min() ... like this 

a=dS["Age"].min()
b=dS["Age"].max()
c=dS["Age"].count()

print(a)
print(b)
print(c)