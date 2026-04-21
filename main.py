import pandas as pd


data = pd.read_csv(r"C:\Users\Administrator\Desktop\data science\lesson_4\titanic.csv")


print(data.head())

#loc
adultname = data.loc[data["Age"] >18 , "Name"]
print(adultname)

print(data.iloc[0:11,2:5])# 0:11 row   , 2:5 is for collum  de laatste is niet included dus daarom 11 


data.iloc[0:30,2] = "Tommy"   # CHANGING the names to tommy 
print(data.iloc[0:30,2])
data.to_csv("lesson_4/titanic2.csv")# Saving a csv file

#adding a collum 
data["Test"] = data["Fare"] +10
data["Test2"] = 10
print(data.head())


#ADDING THE FARE AND PcLass
data["product"] = data["Fare"] * data["Pclass"]
print(data)

#changing the name of Pclass

data_rename = data.rename(
    columns={
        "Pclass":"Passenger Class",
        "Fare":"Price",
        "Sex":"Gender"
    }
)
print(data_rename.head())

print(data["Fare"].mean())# print the mean of age 

print(data.agg({ # printing the min max and median
    "Age":["min","max","median"],
    "Fare":["min","max","mean"]
}))# agg = aggregate 

print(data["Age"].value_counts())#value_counts gives the count of rows in each catogory 

