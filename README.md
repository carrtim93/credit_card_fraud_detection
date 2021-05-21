# Credit Card Fraud Detection

Technical PoC: 
### Contents:

1. Introduction
2. Data Science Scope //
    2a. Business Case // 
    2b. Key User Stories // 
3. Data
4. Feature Engineering
5. Machine Learning Model
6. Training and Tuning
7. Data Visualization 
8. Testing
9. Ethical/Legal Compliance
10. Cloud Integration

## 1. Introduction
This document details the purpose, methodology, and application of data science within the Credit Card Fraud Detection system. Section 2 outlines the business objective addressed by the data science work, and defines the scope of the effort. Section 3 describes the data collected and utilized during analysis. Sections 4, 5, and 6 detail the methodologies employed, why they were selected, and how they are used and tuned (Section 4), trained (Section 5), and tested (Section 6). 

## 2. Data Science Scope
### Business/Use Case
It is important to be able to recognise fraudulent credit card transactions so users are not charged for purchases they did not make. Given that the dataset is highly imbalanced we will look into methods of dealing with this such as undersampling and oversampling and look at which is better for our dataset. We will propose a number of classification models and determine which is the most accurate.
### Key User Stories

## 3. Data

| Property     | Description |
| ----------- | ----------- |
| Name      | Credit Card Fraud Detection dataset       |
| Description   | Contains transactions made by credit cards in September 2013 by european card holders. The transactions occurred over a 2 day period and have 492 frauds out of a total of 284,807 transactions. Highly unbalanced dataset (0.0172% fraud).Only numerical input variables which are the result of a PCA transformation. Original features are not provided due to confidentiality issues. V1, V2,.., V28 are principal components obtained from PCA. The only features which have not been transformed are time and amount. Time contains the seconds elapsed between each transaction and the first transaction in the dataset.        |
| Data Source | The data source that stores, owns, or transfers the data asset. The operating source should be the ID of the Data Source in the Data Source Catalog. |
| Point(s) of Contact | Name and contact information for a point of contact knowledgeable about details of the data asset.  |
| Format | csv |
| Structure | Table? |
| Schema | datetime, int | 
| Sample Data |  |
| Volume | 143.84 MB (for csv) |
| Velocity | Data streaming velocity (ingest availability), measured in data size per time (e.g., MBs/sec) |
| Refresh Rate | None |
| Location | File path on machine |
| Data access mode | Raw file endpoint for the time being |
| Access Restriction | None |
| Constraints |  |
| Assets Derived From |  |
| Notes | |

## 4. Feature Engineering

## 5. Machine Learning Model
This section details the methodologies proposed to be implemented during the development. This section can either be organised by type of methodology or the user story that they address.
### Preprocessing
Scaling: since the majority of the data has already been scaled we should also scale Time and Amount. We will consider the standard scaler and robust scaler
Subsampling: due to the dataset being incredibly imbalanced we need to create a subsample dataframe with a 50/50 ratio of fraud and non-fraud transactions.
If we use the original dataframe we will face problems such as overfitting since the model will assume that in most cases there are no frauds and wrong correlations. It is difficult to see how each feature influences the result with imbalanced data.
Undersampling vs Oversampling vs SMOTE: Undersampling is likely not the best option as discarding a lot of information is generally bad
### Classifiers
We will use a number of different classifiers and test which gives the most accurate result: 
* Logistic Regression
* SGD Classifier
* Random Forest Classifier
* Decision Tree Classifier

## 6. Training and Tuning

## 7. Data Visualisation

## 8. Testing 

## 9. Ethical/Legal Compliance

## 10. Cloud Integration
