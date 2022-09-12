#Author: Vijay Sithambaram
#Date: 6/28/22
#Purpose: Preliminary Analysis for Homeless Clustering Project, Does not include unsupervised learning methods

import pandas as pd
import seaborn as sns

sns.set_style("darkgrid")

df_all_values = pd.read_csv("dfAllValues.csv")
df_no_personal_id = pd.read_csv("dfNoPersonalID.csv")
#checking for any correlation between our newly created variable 'TotalUsage' and the various services
df_no_personal_id.corrwith(df_no_personal_id['TotalUsage'])

#Basic Count Statistics, most each service was used
df_all_values.groupby('personalid').sum().max().sort_values(ascending=False)
df_all_values.groupby('personalid').sum().max().sort_values(ascending=True).plot.barh()#figsize=(40, 15), rot = 1)

#getting an idea of the most used services
df_all_values.groupby('personalid').count().sum()
df_all_values.groupby('personalid').count().sum().sort_values(ascending=True).plot.barh()

#Scatterplots between highly correlated variables
sns.scatterplot(data = df_no_personal_id, x = 'ESNights', y = 'TotalUsage')
sns.scatterplot(data = df_no_personal_id, x = 'ES', y = 'TotalUsage')
