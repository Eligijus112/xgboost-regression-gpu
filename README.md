# xgboost-regression-gpu

A template project for xgboost regression using both cpu and gpu. 

# Data 

The data is from the open hackaton hosted by Vinted in 2021 regarding sales data from certain shops in Germany. The data is in the **train.csv** file.

Data column explanations:

Store - store identification number

Date - date of the store sales record

DayOfWeek - weekday of the Date

Sales - revenue from goods sold during that Date (only available in train_data.csv)

ShopOpen - boolean flag if shop was open during that Date (if not open, Sales should be 0)

Promotion - boolean flag if any promotions were done during that Date

StateHoliday - factor variable if the Date is state holiday or not

SchoolHoliday - factor variable if the Date is school holiday or not

StoreType - factor variable describing the type of a store

AssortmentType - factor variable describing the assortment type of a store

The number of rows > 1 000 000. 

# Objective 

Create an xgboost regression model with gpu and cpu and compare the results. 
