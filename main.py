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



#consept group 
print(data[["Sex","Age"]].groupby("Sex").mean())

print(data.groupby("Sex")["Age"].mean())

print(data.groupby("Pclass")["Age"].mean())
print(data.groupby("Pclass")["Fare"].mean())

print(data.groupby(["Sex","Pclass"])["Fare"].mean())

a = data.sort_values(by="Age")
print(a[["Name","Age"]])

b = data.sort_values(by="Age",ascending=False)
print(b[["Name","Age"]])


#CREATING A NEW COLLUM 
data["lowercasename"] = data["Name"].str.lower()
print(data.head())

#creating a collum named gender 
data["Gender"] = data["Sex"].replace({"male":"M","female":"F"})
print(data.head(8))

#PRACTICE QUESTION
#teen=data.loc[data["Age"]>12&(data["Age"]<18)]  _____ class_2_3__3 = data2[(data2["Pclass"] == 2) | (data2["Pclass"] == 3)]
intwen = data[(data["Age"] >= 20) & (data["Age"] <= 40)]
print(intwen[["Name","Fare"]])

# GET the name class of pass who paid More than 100
morethanhun = data[(data["Fare"] >= 100)&(data["Pclass"] == "3")]
print(morethanhun[["Name","Pclass","Fare"]])

# GET SURVIVED AND IN CLASS 3  
survivedclass3 = data[(data["Survived"]== 1)]
print(survivedclass3["Name"])