import pandas as pd

#create a dataframe
df=pd.DataFrame({
    "Name":["ANU","SINDHU","REMI","OLI","a","b","c","d"],
    "age":[12,57,25,13,43,54,32,34],
    "city":["Ajmer","madurai","chennai","Banglaore","x","f","d","w"]
})


print(df.head())#print first 5 rows
print(df.head(8))#printing all rows

#pirnt number of rows and coloumns
print(df.shape)

print(df["Name"])#print name coloumn 

print(type(df.info()))
print(df["age"].shape)

print(df.info())#gives the summery of the data

#gives the importanat calculations on the coloumns
print(df.describe())

#loading the data from a file
data=pd.read_csv("titanic.csv")
print(data.head())

print(data.info())

#selecting multiple coloumns together
nameAndAge=data[["Name","Age"]]

print(nameAndAge.head())
print(nameAndAge.shape)

#filtering 
abv35= data[data["Age"] > 35]
print(abv35.head())
print(abv35.shape)

#combinig multiple conditions together

class2AND3= data[data["Pclass"].isin([2,3])]
print(class2AND3[["Name","Pclass"]].head())
print(class2AND3.shape)

#combing conditions by or (|),by and (&)

class2and3=data[(data["Pclass"] ==2)|(data["Pclass"]==3)]
print(class2and3[["Name","Pclass"]].head())
print(class2and3.shape)

malenmean=data[(data["Sex"]=="male")&(data["Pclass"]==1)]
print(malenmean.head())

print(malenmean["Fare"].mean())