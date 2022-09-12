# Files Overview:

## Order to Run + Breif Overview:

Notic: Run from top to bottom for optimal results

1. ETL.py (Extract Transform Load):
  - This file takes the raw data provided by the Unit For Data Science and Analytics and coverts it into two cleaned files. Output file:
  - dfAllValues.csv
  - dfNoPersonalID.csv
  - As mentioned in the csv file name, one of the dataframes does not cointain personalId's whereas the other does 

File: https://github.com/Vezaiy/Homelessness_Clustering/blob/main/ETL.py

2. exploratory_data_analysis.py:
  - This file conducts basic exploratory analysis on the cleaned datasets
  - Additionally several commands are built in to do basic plotting of various statistical relationships

File: https://github.com/Vezaiy/Homelessness_Clustering/blob/main/exploratory_data_analysis.py

3. statistical_models.py:
  - This file contains the final Jenks Natrual Breaks Optimization model for this project
  - Additionally this model outputs two complete CSV file that includes the new clusters.
  - df_all_values_clustered.csv
  - df_no_personal_id_clustered.csv

File: https://github.com/Vezaiy/Homelessness_Clustering/blob/main/statistical_models.py

4. Evaluation.py  
  - This file contains the evaluation metrics used in this project 
  - It takes the final clustered dataframes and computes various metric scores
 
File: https://github.com/Vezaiy/Homelessness_Clustering/blob/main/Evaluation.py
