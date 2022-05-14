import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


Report_Card = pd.read_csv("Levels_Fyi_Salary_Data.csv")
# graph salary vs years of experience


def moneyplz():
    # x array
    x = Report_Card.loc[:, "yearsofexperience"]
    y = Report_Card.loc[:, "totalyearlycompensation"]

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
