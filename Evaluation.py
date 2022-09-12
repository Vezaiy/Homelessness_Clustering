#Author: Vijay Sithambaram
#Date: 6/28/22
#Purpose: Computing Various Evaluation Scores for Project
import pandas as pd
import numpy as np
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score

df_no_personal_id_clustered = pd.read_csv('df_no_personal_id_clustered.csv')

data = np.array(df_no_personal_id_clustered['TotalUsage']).reshape(-1, 1)

keys = ['Silhouette Score', 'Davies Boudin Scores', 'Calinski Harabasz Score']
values = [silhouette_score(data, labels = df_no_personal_id_clustered['Usage Cluster']),
          davies_bouldin_score(data, labels = df_no_personal_id_clustered['Usage Cluster']),
          calinski_harabasz_score(data, labels = df_no_personal_id_clustered['Usage Cluster'])]

scores = { key : value
                for key, value in zip(keys, values)}
