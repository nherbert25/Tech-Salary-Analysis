# pip install -r requirements.txt
import pandas as pd
import numpy as np
import pytest
import matplotlib.pyplot as plt

print('gofuckyaself')

print('cats are great')

print('test')

print('foobar')

print([3, 4])


print(type(np.array([3, 4])))


# graph salary vs years of experience

Report_Card = pd.read_csv("Levels_Fyi_Salary_Data.csv")
# x array
x = Report_Card.loc[:, "yearsofexperience"]

y = Report_Card.loc[:, "totalyearlycompensation"]


fig1, ax3 = plt.subplots()
ax3.scatter(x, y)
ax3.set_ylim([0, .3e6])
ax3.set_xlim([0, 42])
ax3.set_ylabel('Total Yearly Comp')
ax3.set_xlabel('Years of Experience')
ax3.set_title("Money Plz", va='bottom')
plt.show()
