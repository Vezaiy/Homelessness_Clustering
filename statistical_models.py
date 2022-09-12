#Author: Vijay Sithambaram
#Date: 6/28/22
#Purpose: final model, clustering model based on 'TotalUsage', does not include previous model iterations, find those in prototype notebook
#prototype link: https://github.com/Vezaiy/Homelessness_Clustering/blob/main/Homeless_Clustering_Prototype.ipynb

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import jenkspy
from sklearn.cluster import KMeans

df_all_values = pd.read_csv("dfAllValues.csv")
df_no_personal_id = pd.read_csv("dfNoPersonalID.csv")

#this function computes the optimal number of clusters for our various algorithims
def elbow_method(data_frame, lower_bound, upper_bound):
    sum_square_distance = []
    K = range(lower_bound, upper_bound)
    for k in K:
        print("Beginning k = " + str(k))
        kmeans_k = KMeans(n_clusters=k).fit(data_frame) #
        sum_square_distance.append(kmeans_k.inertia_)

    plt.plot(K, sum_square_distance, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Sum_of_squared_distances')
    plt.title('Elbow Method For Optimal k')
    plt.show()

#plots jenks break intervals
def plot_jenks(data_frame, break_intervals, col_name):
    plt.figure(figsize=(40,12))
    sns.stripplot(x = f"{col_name}", data = data_frame, jitter = True, edgecolor = 'none')
    sns.despine()
    for b in break_intervals:
      plt.vlines(b, ymin=-0.2, ymax = 0.5)

#final model, with nb_class chosen based on the Kmeans elbow method
breaks = jenkspy.jenks_breaks(df_no_personal_id['TotalUsage'], nb_class = 5)

#updating dataframe with new cluster based on usage
df_no_personal_id['Usage Cluster'] = pd.cut(df_no_personal_id['TotalUsage'],
    bins = breaks, labels = ['Very Low Use', 'Low Use', 'Medium Use', 'High Use', 'Very High Use'],
    include_lowest=True)

df_all_values['Usage Cluster'] = pd.cut(df_no_personal_id['TotalUsage'],
    bins = breaks, labels = ['Very Low Use', 'Low Use', 'Medium Use', 'High Use', 'Very High Use'],
    include_lowest=True)

df_no_personal_id.to_csv("df_no_personal_id_clustered.csv", index =False)
df_all_values.to_csv("df_all_values_clustered.csv", index =False)
