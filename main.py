# import csv
#
# with open("season18-19.csv", 'r') as f:
#     scores = list(csv.reader(f))
#
# am = [int(w[4]) for w in scores]
# a = sum(am)
# a_len = len(am)
#
# print(a/a_len)

# отключим предупреждения Anaconda
import warnings
warnings.simplefilter('ignore')

# будем отображать графики прямо в jupyter'e
#%matplotlib inline
import seaborn as sns
import matplotlib.pyplot as plt
#графики в svg выглядят более четкими
#%config InlineBackend.figure_format = 'svg'

#увеличим дефолтный размер графиков
from pylab import rcParams
rcParams['figure.figsize'] = 8, 5
import pandas as pd

kolumn = {"a" : "Date", "b" : "HomeTeam", "c" : "AwayTeam", "d" : "FTHG", "e": "FTAG", "f" : "FTR", "g" : "HTHG", "h" : "HTAG", "i" : "HTR",
        "j" : "Referee", "k" : "HS", "l":"AS", "m": "HST","n":"AST", "o": "HF", "p" : "AF", "q":"HC", "r":"AC","s" : "HY", "t":"AY",
        "u" : "HR", "v":"AR", "w" : "HP", "x" : "HGP", "y" : "AP", "z" : "AGP", "aa" : "AytogolH", "bb" : "AutogolA" }
data = pd.read_csv("season18-19.csv")
data1=pd.read_csv("season19-20.csv")
# am = [int(w) for w in data["FTHG"]]
# a = sum(am)
# a_len = len(am)
#
# print(a/a_len)
# print(data.describe())
# teams = input("Vvedite Home Team : "), input("Vvedite Away Team : ")
# a=data[(data[kolumn['b']] == teams[0])&(data["AwayTeam"]==teams[1])]["FTHG"].sum()
# b=data[data["HomeTeam"] == "Chelsea"]["FTHG"].max()
#
#
# print(data1['HS'].mean())
#
# print(data1.iloc[0:2, 0:3])
#
# a=pd.crosstab(data[kolumn['b']], data[kolumn['k']], margins= True)
#
# b = data1[data1.].corr()["AS"]
# print(b)

cols = [kolumn['e'], kolumn['f'], kolumn['h'],kolumn['i']]
sns_plot = sns.pairplot(data1[cols])
sns_plot.savefig('pairplot.png')
sns_1=sns.jointplot(data1.FTHG, data1.HTHG)
sns_1.savefig("pairplot1")
