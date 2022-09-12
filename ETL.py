#Author: Vijay Sithambaram
#Date: 6/28/22
#Purpose: Basic Data cleaning for Homeless Clustering Project, Run once and data will be cleaned

import pandas as pd

url = 'https://raw.githubusercontent.com/djlittle/Homelessness_Clustering_Comparisons/master/Data/HMIS%20Data%20Extract.csv'

df_all_values = pd.read_csv(url)

#renaming columns
df_all_values.rename(columns={'projecttype_1_bednights':'ESNights', 'projecttype_1_count':'ES',
                   'projecttype_2_count': 'TransitionalHousing', 'projecttype_3_count': 'PH'
                   ,'projecttype_4_count': 'StreetOutReach', 'projecttype_6_count': 'ServicesOnly',
                   'projecttype_7_count': 'Other', 'projecttype_8_count': 'SafeHaven', 'projecttype_10_count': 'PH-NoDis',
                   'projecttype_12_count': 'HomelessPrev', 'projecttype_13_count': 'PHRapid',
                   'projecttype_14_count': 'CoordinatedAsses'}, inplace=True)

#dealing with null values, while also getting rid of the personal ID's
df_no_personal_id = dfAllValues.iloc[:, 1:]
df_no_personal_id.fillna(0, inplace=True)

#creating a column with aggregated usage data
aggregate_usage = df_no_personal_id.sum(axis=1)
df_no_personal_id['TotalUsage'] = aggregate_usage

#saving our new dataframes
df_all_values.to_csv("dfAllValues.csv", index =False)
df_no_personal_id.to_csv("dfNoPersonalID.csv", index =False)
