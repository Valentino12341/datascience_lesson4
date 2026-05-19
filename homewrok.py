import pandas as pd 

data = pd.read_csv(r"C:/Users\Administrator\Desktop\data science/lesson_4/titanic.csv")

child =data.loc[data["Age"]<12]
teen=data.loc[data["Age"]>12&(data["Age"]<18)]
adult=data.loc[data["Age"]>18]


print(len(child))
print(len(teen))
print(len(adult))

print(child.shape)
print(teen.shape)
print(adult.shape)

