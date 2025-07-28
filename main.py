import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

data = pd.read_csv("adult.csv")


data.columns = ['age', 'workclass', 'Id','education', 'educational-num',
                'marital-status','occupation','relationship','race','gender',''
                'capital-gain','capital-loss','hours-per-week','native-country','income']


data.rename(columns = {'capital-gain' : 'capital gain', 'capital-loss' : 'capital loss', 'hours-per-week' : 'hours per week',
                        'native-country' : 'country', 'marital-status' : 'marital'}, inplace=True)


print(data.describe())

print(data.info())

print(data.isin(['?']).sum(axis=0))

data.drop(['educational-num','age','hours per week', 'Id','capital gain', 'capital loss', 'country'], axis = 1, inplace = True)

print(data.head())


income = set(data['income'])
print(income)

#convert to numerical 

data["income"] = data["income"].map({' <=50K': 0,' >50K' : 1 }).astype(int)
print(data.head())
#Gender
gender = set(data['gender'])
print(gender)

data["gender"] = data["gender"].map({' Male' : 0,' Female' : 1}).astype(int)
print(data.head())

data.groupby('gender').income.mean().plot(kind='bar')
plt.show()
#Race
race = set(data['race'])
print(race)

data["race"] = data["race"].map({' Other':0,' Amer-Indian-Eskimo':1,' Black':2,' White' :3,' Asian-Pac-Islander': 4}).astype(int)
print(data.head())

data.groupby('race').income.mean().plot(kind="bar")
plt.show()
#Relationship
relationship = set(data["relationship"])
print(relationship)

data["relationship"] = data["relationship"].map({' Unmarried':0, ' Not-in-family':1, ' Own-child':2, ' Other-relative':3, ' Wife':4, ' Husband':5}).astype(int)
print(data.head())

data.groupby("relationship").income.mean().plot(kind="bar")
plt.show()
#Occupation
occupation = set(data["occupation"])
print(occupation)

data["occupation"] = data["occupation"].map({' Armed-Forces':0, ' Craft-repair':1, ' ?':2, ' Sales':3, ' Other-service':4, ' Machine-op-inspct':5, ' Handlers-cleaners':6, ' Farming-fishing':7, ' Exec-managerial':8, ' Priv-house-serv':9, ' Prof-specialty':10, ' Adm-clerical':11, ' Transport-moving':12, ' Protective-serv':13, ' Tech-support':14})
print(data.head())

data.groupby("occupation").income.mean().plot(kind="bar")
plt.show()
#Marital
marital = set(data["marital"])
print(marital)

data["marital"] = data["marital"].map({' Divorced':0, ' Widowed':1, ' Never-married':2, ' Separated':3, ' Married-spouse-absent':4, ' Married-AF-spouse':5, ' Married-civ-spouse':6})
print(data.head())

data.groupby("marital").income.mean().plot(kind="bar")
plt.show()
#Education
education = set(data["education"])
print(education)

data["education"] = data["education"].map({' Masters':0, ' Prof-school':1, ' Preschool':2, ' 12th':3, ' Assoc-voc':4, ' 1st-4th':5, ' Some-college':6, ' 11th':7, ' Assoc-acdm':8, ' Doctorate':9, ' Bachelors':10, ' 9th':11, ' 5th-6th':12, ' 7th-8th':13, ' 10th':14, ' HS-grad':15})
print(data.head())

data.groupby("education").income.mean().plot(kind="bar")
plt.show()
#Workclass
workclass = set(data["workclass"])
print(workclass)

data["workclass"] = data["workclass"].map({' Local-gov':0, ' Federal-gov':1, ' Never-worked':2, ' ?':3, ' Self-emp-not-inc':4, ' State-gov':5, ' Private':6, ' Self-emp-inc':7, ' Without-pay':8})
print(data.head())

data.groupby("workclass").income.mean().plot(kind="bar")
plt.show()