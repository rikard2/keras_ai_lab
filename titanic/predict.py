from keras.models import load_model
import numpy as np
import pandas as pd
from data import test_data, test_data_dataframe

model = load_model("titanic.model")

predictions = model.predict(test_data)
test_data_dataframe['Survival_probability'] = predictions
test_data_dataframe['Survived'] = np.round(predictions)

predictions = test_data_dataframe

def predict(sex = 0, age = 25, pclass = 1, sibsp = 0, parch = 0, embarked = 1):
    sex_label = 'male' if sex == 1 else 'female';
    data = np.array([ [ pclass, sex, age, sibsp, parch, embarked ] ])
    p = model.predict(data)
    return "Probability of survival for this {0} year old {1} was {2} %.".format(age, sex_label, round(p[0][0] * 100, 2))
