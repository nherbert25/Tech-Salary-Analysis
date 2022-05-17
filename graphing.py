import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv("Levels_Fyi_Salary_Data.csv")

# Feature Engineering - Remove Outlier and Irrelevant Data
# Drop data where Years of Experienced == 0 (Unsure if actually zero, or no answer was given)
data = data.drop(data[data.yearsofexperience == 0.0].index, inplace=False)
data = data.reset_index()

# Drop data that is not from the US
non_us = 0
for i in range(len(data)):
    if len(data['location'][i].split(',')) > 2:
        non_us += 1


def is_in_us(index):
    return len(data['location'][index].split(','))


# graph salary vs years of experience
def moneyplz():
    # x array
    x = data.loc[:, "yearsofexperience"]
    y = data.loc[:, "totalyearlycompensation"]

    fig1, ax3 = plt.subplots()
    ax3.scatter(x, y)
    #ax3.set_ylim([0, .3e6])
    #ax3.set_xlim([0, 42])
    ax3.set_ylabel('Total Yearly Comp')
    ax3.set_xlabel('Years of Experience')
    ax3.set_title("Money Plz", va='bottom')

    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x, p(x), "r--")
    plt.show()
