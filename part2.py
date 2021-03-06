import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(sum(map(ord,"aesthetics")))

def sinplot(flip=1):
    x =np.linspace(0,14,100)
    for i in range(1,7):
        plt.plot(x,np.sin(x+i*0.5)*(7-i)*flip)
        sinplot()
sns.set_style("whitegrid")

tips = sns.load_dataset("tips")
ax = sns.boxplot(x=tips["total_bill"])
ax = sns.boxplot(y=tips["total_bill"])
ax = sns.boxplot(x="day", y="total_bill", data=tips）