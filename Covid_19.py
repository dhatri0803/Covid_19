#importing required libraries
import pandas as pd
import matplotlib as plt
import seaborn as sb
import numpy as np

data=pd.read_csv("covid_19_india.csv")
data.columns

data.describe()
#gives count ,mean , standard deviation ,etc

data.isnull().sum()
#chechking for null values

#relating with scatterplots
sb.relplot(x="Confirmed",y="Cured",data=data)
sb.relplot(x="Confirmed",y="Deaths",data=data)
sb.relplot(x="State/UnionTerritory",y="Cured",data=data)
sb.relplot(x="State/UnionTerritory",y="Deaths",hue='Deaths',data=data)

sb.pairplot(data)

sb.relplot(x="Confirmed",y="Deaths",kind="line",data=data)

sb.catplot(x="Confirmed",y="Cured",data=data)

sb.pairplot(data)

#So ,conclusions from this can be: 1.The number of cured are increasing as the confirmed cases increases. 2.Then number of deaths were startening to flatten but have unfortunately increased too. 3.The states with more population tend to have more number of cases.
#So,if rules are followed and good sanitizations with enough quartining is maintaining ,the number of cases can go down.
