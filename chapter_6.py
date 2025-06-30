"""
In chapter 6 we see how to merge and concat two data sat 
"""

# 1. merge --> pd.merge(df1.df2,on="Column_name",how="Right)
import pandas as pd
dataframe={
    "Id":["001","002","003","004"],
    "Name" : ["Agam Jain","Harsh Modi","Hardik Balsunni","Dev Pancholi"],
    "Age":[20,21,55,22],
    "State":["UP","MP","UP","MP"],
    "Salary":[50000,65000,45000,30000]
}

Course={
    "Id":["001","002","003","004"],
    "Course_name":["B.tech","B.tech","B.tech","BCA"]
    
}

dS= pd.DataFrame(dataframe)
Cours=pd.DataFrame(Course)
Df=pd.merge(dS,Cours,on="Id",how="right")

print(Df)


# 2. concatenate --> pd.concate([df1,df2],axis=0,ignore_index=True)
g=pd.concat([dS,Cours],axis=0,ignore_index=True)
print(g)
