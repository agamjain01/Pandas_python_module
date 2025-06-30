''' In this first code we are see How to read the  file 
    with the read_csv ,read_excel and read_json files 
    
    when file read some error are see then we are use encoding = "Uft-8 " and "latin1" 
'''

import pandas as pd 

# df =pd.read_csv("D:\Data Scientist\Python\Ad Python\Pandas\Read.csv")
# print(df)

# df=pd.read_excel("D:\Data Scientist\Python\Ad Python\Pandas\Read_file.xlsx")
# print(df)


""" 
 Now we are see how to save the data frame and series files to our system
 when file save in csv --> pd.to_csv("file_name.csv ")
 when file save in excel --> pd.to_excel("file_name.xlsx ")
 when file save in csv --> pd.to_json("file_name.json") 
"""

dataframe={
    "Name" : ["Agam Jain","Harsh Modi","Hardik Balsunni","Dev Pancholi"],
    "Age":[20,21,23,22],
    "State":["UP","MP","UP","MP"],
    "Salary":[25000,65000,45000,30000]
}

dataframe=pd.DataFrame(dataframe)

print(dataframe)

dataframe.to_csv("output.csv",index=False)
dataframe.to_excel("output.xlsx",index=False)
dataframe.to_json("output.json",index=False)