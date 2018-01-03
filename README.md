# keras_ai_lab
Lab code after experimenting with AI and machine learning with keras


## Titanic
#### Data:
```bash
python -i titanic/data.py
```

```python
ds.head() # Dataframe
training_data
target_data
test_data
test_data_dataframe
```

#### Train:
```bash
python titanic/train.py
```

#### Test:
```bash
python -i titanic/predict.py

>>> predict(age = 25, sex = 1, pclass = 1)
'Probability of survival for this 25 year old male was 33.62 %.'
>>> predict(age = 25, sex = 1, pclass = 2)
'Probability of survival for this 25 year old male was 19.75 %.'
>>> predict(age = 25, sex = 1, pclass = 3)
'Probability of survival for this 25 year old male was 10.68 %.'
>>>
```
