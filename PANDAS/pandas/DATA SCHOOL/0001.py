import pandas as pd 
coloumnnames =["Stydent ID" , "Student Name" ,"Class" ,"Section" ,"Exam" ,"Subject" , "Marks"]
df =pd.read_csv('mark.csv' ,coloumnnames=coloumnnames)
print(df.head())