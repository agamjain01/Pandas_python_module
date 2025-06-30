"""
   In chapter two we are see how to analysis the data.
   1. understand the data set
   2. identify the problem
   3.plan next step      
"""

''' 1. first we are check the row column infomation with help of 
       head and tail function head() without any paramiter head show 5 first row and
       tail show last 5 rows 
'''
import pandas as pd 

df=pd.read_csv('D:\Data Scientist\Python\Ad Python\Pandas\Read.csv')

print("First 5  rows ","\n",df.head(1))

print("Last 5  rows ","\n",df.tail(1))


"""
    Now we analysis the data size and data informatin with help of
    info mothed --> df.info()
"""

print("Data sat information ","\n",df.info())


#  describe() method help to nemeric   analysis 

print(df.describe())

""" Next step is we are see how many rows and column are oresent in data sat
    then we are use the shape and column motheds 
    shape method are return --> no. rows and column are present in my data set 
    columns mrthod are return --> column names 

"""

print(f"Shape: {df.shape}")

print(f"Column name : {df.columns}")


"""
   Now 5 step is selecting and filtering  data set like when you needed 
   the selected rows are see you then yoy run this query dataframe_name["Column_name"]
   and multiple row you are access then use this query dataframe_name["Column_name1",Column_name2",...]
   
   second part is Filtering the data set 
   single column then we run this query --> dataframe_name["Column_name" > condition]
    
   when apply filtering multiple condition then we are use 
   --> dataframe_name[("Column_name1" > condition) & ("Column_name2" > condition)]
"""

dataframe={
    "Name" : ["Agam Jain","Harsh Modi","Hardik Balsunni","Dev Pancholi"],
    "Age":[20,21,23,22],
    "State":["UP","MP","UP","MP"],
    "Salary":[25000,65000,45000,30000]
}


dS= pd.DataFrame(dataframe)

print(dS)

print(dS["Salary"])

print(dS[["Name","Salary"]])


print("Filtering data:\n", dS[dS["Salary"] > 40000])

print("Filtering  multiple column then ","\n",dS[(dS["Salary"] >20000) & dS["Age"] >20])