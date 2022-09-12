# Homeless Clustering Summary 
Maricopa County has experienced a significant amount of homelessness during the past ten years. Unsheltered homelessness has steadily increased since 2014 and will climb by almost 92% between 2018 and 2022. Government Magazine of Arizona The county's rising homelessness rate raises the possibility of problems with criminality, health policy, transportation, and the financial strain on the government. In a 2017 external assessment by the RAND Corporation, researchers discovered that the typical homeless person in California receives governmental services valued $38,416. (RAND) Additionally, due to a shortage of public health services, possible outbreaks of diseases including STDs, hepatitis, and more are increased by those who are homeless. According to CDC reports, the effectiveness of several hepatitis outbreak treatments rose where there was a lot of homeless people. (CDC) Furthermore, it is impossible to overlook the safety and social risk that homeless people pose because most people become more tense or anxious around homeless individuals and communities.

The aforementioned homeless problem thus raises the question of how we might understand homeless behavior to make political choices that have a favorable effect on homeless populations. However, in order to create such a model, we must first have a thorough knowledge of homeless populations. Therefore, I suggest using various statistical methods and approaches on homeless service data in Maricopa County from 2014 to 2018 to promote knowledge and awareness of homeless statistics.

I was able to determine via the use of several clustering algorithms that it is possible to group homeless persons into 5 optimally selected unique clusters, ranking from "Very Low Usage" to "Very High Usage," based on the number of services they use. After using Jenks Natural Breaks Optimization to create the final cluster model, I examined it and discovered that 80% of homeless people belong to the "Very Low Usage" cluster, the with other 20% belonging to the higher "Usage" clusters. I was also able to locate other descriptive information about the most popular services and depict different statistical relationships.

The clusters show that there is a significant disparity between both the variety of services offered as well as the number of homeless people using them. In our dataset from 2014 to 2018, we discover that the median number of services used by a homeless person totals just 2, while the maximum number hovers around 685. Additionally, the top five total service counts, which account for 71% of all services used, are 1, 2, 3, 4, and 5. This demonstrates that the majority of residents of Maricopa County do not fully utilize the services offered, potentially wasting resources. I infer from this that additional information will be required to understand whom and why solutions are needed and not put to use. Ideally, demographic information would significantly improve our comprehension.

## Final Visualizations

### Vizualizing Jenks Natural Breaks Optimization 
<img width="500" alt="Screen Shot 2022-07-13 at 7 26 51 AM" src="https://user-images.githubusercontent.com/88412646/178794274-67b8e63f-07c9-4768-ba78-4a0384236818.png">

On this graph we can see the clear Breaks/Usage Clusters that our model detected. The results are very fascinating and the graph clearly shows that clusters do exist based of the amount of services that homeless people use in the Maricopa County. Additionally it becomes clear that there is severe imbalance in the amount of services used as the majority of homeless individuals are not making use of services and fall with the low usage towards the far left.

### Bar Chart Cluster Distribution
<img width="500" alt="Screen Shot 2022-07-13 at 7 29 57 AM" src="https://user-images.githubusercontent.com/88412646/178794847-54c9b189-58cb-4bf8-ac8e-a804beceebe1.png">

This graph builds off our model and graphs the distribution of each cluster we found. It is clear that the majority of homeless indviduals fall within the 'Very Low Use' cluster. This shows a clear imbalance between service users in the homeless community. Though it is out of scope for this project, it's clear that there are other factors involved that may lead to this. For example it may be due to a lack of services in certain regions, improper resource management, or other external factors.

### Bar Chart Showing Service Distribution

<img width="500" alt="Screen Shot 2022-07-13 at 7 47 30 AM" src="https://user-images.githubusercontent.com/88412646/178797792-df053698-f8e2-4642-b4ea-d07066ac8193.png">

This graph shows the distribution of various homeless services in the Maricopa County. From here we can see that various services tend to be used quite often by homeless individuals. But the pattern of constant imbalance continues in this graph as well, with certain services being used often and others not at all.

### Elbow Method for Optimal K Clusters 
<img width="500" alt="Screen Shot 2022-06-29 at 8 11 31 AM" src="https://user-images.githubusercontent.com/88412646/176506581-1b5f9bdb-777b-4f67-9711-e2fff4b92c30.png">

This graph shows the elbow method, which we used to choose the final number of clusters for our model. This method iterates through multiple versions of a model and tries to find the model that minimizes the amount of variation within clusters while maximizing variation between clusters. We then choose the optimal number of clusters based on the lowest number of clusters that min's the most variation.

## Exploratory Visualizations

### Initial Principal Component Analysis, with K Means Clusters for the various changes in color (code in prototype file)

Each of these graphs were used in the preliminary analysis and display a 'Projection' of the total dataset onto a scatterplot. As you can see the results of our projections are very hard to interpret and do not show any clear clusters within our dataset. Becuase of this we did not use these methods and instead used the model mentioned above. 

<img width="1100" alt="Screen Shot 2022-06-29 at 8 15 33 AM" src="https://user-images.githubusercontent.com/88412646/176507285-90327ed6-c66f-4467-a15b-cb90d7839742.png">

### Initial Principal Component Analysis, with DBSCAN for the various changes in color (code in prototype file)
<img width="1100" alt="Screen Shot 2022-06-29 at 8 16 38 AM" src="https://user-images.githubusercontent.com/88412646/176507482-6d0c22ea-417f-448a-bdf9-338a6ca612d5.png">

### Initial Principal Component Analysis, with BIRCH for the various changes in color (code in prototype file)
<img width="1100" alt="Screen Shot 2022-06-29 at 8 17 52 AM" src="https://user-images.githubusercontent.com/88412646/176507703-7f64a3db-be0a-4caa-a2f7-bba0a168c338.png">


## Final Evaluation Methods for Clusters
<img width="500" alt="Screen Shot 2022-06-29 at 8 01 39 AM" src="https://user-images.githubusercontent.com/88412646/176504982-f1bfba89-1341-4ff2-8d0d-d76dad3b1894.png">

