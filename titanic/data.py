import pandas as pd
import numpy as np
import os

ds = pd.read_csv('datasets/titanic.csv')
# Titanic CSV headers:
#   PassengerId
#   Survived    Survival        0 = No, 1 = Yes
#   Pclass      Ticket class    1 = 1st, 2 = 2nd, 3 = 3rd
#   Sex         Sex
#   Age         Age in years
#   SibSp       # of siblings / spouses aboard the Titanic
#   Parch       # of parents / children aboard the Titanic
#   Ticket      Ticket number
#   Fare        Passenger fare
#   Cabin       Cabin number
#   Embarked    Port of Embarkation    C = Cherbourg, Q = Queenstown, S = Southampton

def binary_sex(row):
    return 1 if (row['Sex'] == 'male') else 0

ds = ds.drop(["PassengerId", "Name", "Cabin", "Embarked", "Ticket", "Fare"], axis=1)
ds['Sex'] = ds.apply(binary_sex, axis=1)
ds.fillna(0, inplace=True)

training_data = np.array(ds.ix[:, 1:])
target_data = np.ravel(ds.Survived)
test_data_dataframe = ds.drop(["Survived"], axis=1)
test_data = np.array(test_data_dataframe)
