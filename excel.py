import pandas as pd
import math

titanic =  pd.io.parsers.read_csv("titanic.csv", nrows=50)
age = titanic[['age']]
print(age)