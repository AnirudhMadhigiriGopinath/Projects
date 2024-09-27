# Bank Marketing Dataset with Social/Economic Context


**[Moro et al., 2014]**  
S. Moro, P. Cortez, and P. Rita. A Data-Driven Approach to Predict the Success of Bank Telemarketing.  
*Decision Support Systems*, In press,  
DOI: [10.1016/j.dss.2014.03.001](http://dx.doi.org/10.1016/j.dss.2014.03.001)

## Dataset Overview

This dataset contains information about a Portuguese bank's telemarketing campaign to predict whether a client will subscribe to a term deposit (binary classification). It includes social and economic features, enhancing prediction accuracy. The dataset is based on the UCI "Bank Marketing" dataset, with additional attributes sourced from Banco de Portugal.

### Dataset Versions
1. **Full dataset**: `bank-additional-full.csv` (41,188 instances)

### Goal
The task is a binary classification problem where the goal is to predict whether a client will subscribe to a term deposit.

## Attributes

### Bank Client Data
1. **age**: (numeric)  
2. **job**: type of job (categorical)  
3. **marital**: marital status (categorical)  
4. **education**: (categorical)  
5. **default**: has credit in default? (categorical)  
6. **housing**: has a housing loan? (categorical)  
7. **loan**: has a personal loan? (categorical)  

### Campaign-related Information
8. **contact**: communication type (categorical)  
9. **month**: last contact month (categorical)  
10. **day_of_week**: last contact day (categorical)  
11. **duration**: last contact duration (numeric, in seconds)  
12. **campaign**: number of contacts in the current campaign (numeric)  
13. **pdays**: days since the client was last contacted from a previous campaign (numeric)  
14. **previous**: number of contacts before this campaign (numeric)  
15. **poutcome**: outcome of the previous campaign (categorical)  

### Social and Economic Context Attributes
16. **emp.var.rate**: employment variation rate (numeric)  
17. **cons.price.idx**: consumer price index (numeric)  
18. **cons.conf.idx**: consumer confidence index (numeric)  
19. **euribor3m**: Euribor 3-month rate (numeric)  
20. **nr.employed**: number of employees (numeric)  

### Output Variable
21. **y**: client subscribed to a term deposit (binary: `"yes"` or `"no"`)
