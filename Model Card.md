# Model card for Maricopa County Clustering Analysis

Sections and prompts from the [model cards paper](https://arxiv.org/abs/1810.03993), v2.

Jump to section:

- [Model details](#model-details)
- [Intended use](#intended-use)
- [Factors](#factors)
- [Metrics](#metrics)
- [Evaluation data](#evaluation-data)
- [Training data](#training-data)
- [Quantitative analyses](#quantitative-analyses)
- [Ethical considerations](#ethical-considerations)
- [Caveats and recommendations](#caveats-and-recommendations)

## Model details

- Person or organization developing model: Vijay Sithambaram, ASU Unit for Data Science & Analytics

- Model date: 
  6/28/22
  
- Model version: 
  - 1.0
 
- Final Model type: 
  - Jenks Natrual Breaks Optimization

- Information about training algorithms, parameters, fairness constraints or other applied
  approaches, and features:   
  - Features were collected from Macricopa County and contain data about the activities of 'tagged' homeless individuals from 2014 - 2018. There are around 12 or so variables analyzed for the models proposed in this card. Due to limitations with confidentiality, only varaibles realted to a specific homless persons usage of services are included, specifically in a 'count' / aggregate form, for each service the Maricopa County offers.
  - 'personId' is a unique field which caputures the usage data for one homeless person
  - Additionally we create a variable known as 'TotalUsage' which aggregates the total amount of services a homeless person used
  - After conducting intial PCA and iterating over various unsupervised learning algorithims, we settled with Jenks Natrual Breaks Optimization, a univariate clustering algorithim.
 
- Paper or other resource for more information:
  - Original Repo: https://github.com/UnitForDataScience
  - Model: https://www.semanticscholar.org/topic/Jenks-natural-breaks-optimization/1788806
  - Python Model Package: https://github.com/mthh/jenkspy

- Where to send questions or comments about the model: 
  - veezaiy.addon@gmail.com

## Intended use

_Use cases that were envisioned during development._

Review section 4.2 of the [model cards paper](https://arxiv.org/abs/1810.03993).

### Primary intended uses
- Exploratory understanding of Homeless persons behaviors
- Aid in the development of predictive models 
- Cluster homeless individuals into various groups

### Primary intended users
- Maricopa County Officials 
- ASU Unit For Data Science & Analytics 

### Out-of-scope use cases
- Building clusters that further than a 4 - year period from 2018, without finding optimal clusters 
- Using the clusters to identify homeless persons, without consider other demographic variables

## Factors

### Relevant factors
- Maricopa County has seen steady homeless growth since 2014 (https://azmag.gov/Portals/0/Documents/MagContent/2019-07-31_PIT-Report.pdf?ver=T-l4h0uTPBJRk96khy5kwA%3d%3d)
- Unsheltered individuals are very common in Maricopa County with a 22 % increase from 2014 - 2018
- More info on Homelessness in Maricopa County can be found here: https://azmag.gov/Portals/0/Documents/MagContent/2019-07-31_PIT-Report.pdf?ver=T-l4h0uTPBJRk96khy5kwA%3d%3d 

## Evalutation Metrics
- Sillouthe Method Score
- Calinski Harabasz Score
- Davies Boudin Score
- Elbow method computed the opitmal number of clusters for both the whole dataset and 'total usage'

### Model performance measures
- For this project the above evaluation metrics were used to track cluster purity and performance
- The results above show promising results in terms of cluster purity 

### Approaches to uncertainty and variability
- Due to possible data collection issues there is potential for error within our model, especially since the model relies on counts to properly cluster homeless persons 

## Training Data


### Datasets
- 'https://raw.githubusercontent.com/djlittle/Homelessness_Clustering_Comparisons/master/Data/HMIS%20Data%20Extract.csv'

### Motivation
- Understand homless behaviors in terms of service usage in Maricopa County 

### Preprocessing
- Replacing NA values with 0's. This is a key assumption in our model, however in terms of the project it does make sense as we excpect the majority of services to not be used by homeless individuals. For this project key stakeholders agreed as well.


## Quantitative analyses

### Unitary results:
- 5 Optimal Clusters
- Our final implementation using Jenks Natrual Breaks Optimization recieved the following scores based on our evaluation metrics: 
  - Calinski Harabasz Score: 133475.0909
  - Davies Boudin Scores: 0.4620
  - Silhouette Score: 0.8495

## Ethical considerations

### Data
- Collected data does represent the services that a homeless person used and could possibly be a violation of privacy. However the dataset used circumvents this by giving each homless inividual a personalID.

### Risks and harms
- Clusters should not be treated as 'absolute' and instead should be a starting point for further analysis
- Assumptions about data collection being accurate are made throughout the project
- Additionally during data cleaning, we filled NA values with 0's which is another potentially naive assumption

## Caveats and recommendations
- Moving forward I recommend demographic data be collected to supplement the dataset provided. Doing so will increase the depth and potential of the various clusters. In particular collecting data on fields such as age, race, and years homeless could provide fruitful insights


