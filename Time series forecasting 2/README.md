# Tasks

The primary dataset which is a Parquet file related to corn yield in USA, i concentrated on predicting the area harvested for all the states in US.
I have used regression algorithms to predict the area harvested every year based on the corn features.

The features required to forecast the area harvesed are average tenmperature, cooling degree in days, heating degree in days, and precipitation. There features are secondary datasets.

**Approach:**
Firstly, i have used the secpndary datasets to make the features ready. I have chosen precipitation and the average temperature, to forecast them for future 10 years. 
I have used SARIMAX model to forecast the average temperature and the precipitation every month. The results came out as good in predicting for all the states.
Then, taking those 2 features annually i have passed it to predict the area harvested into a regression model.
