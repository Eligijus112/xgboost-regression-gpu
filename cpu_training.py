# Reading packages
import pandas as pd 

# Iteration tracking
import time

# Xgboost models 
import xgboost as xgb

# Reading data
d = pd.read_csv("train_data.csv", low_memory=False).sample(100000)

# Converting to categorical all the categorical variables
cat_cols = [
    'Store', 
    'DayOfWeek', 
    'ShopOpen', 
    'Promotion', 
    'StateHoliday', 
    'SchoolHoliday', 
    'StoreType', 
    'AssortmentType'
]

d[cat_cols] = d[cat_cols].astype(str)

# Creating the X and Y matrices
features = [
    "Store",
    'DayOfWeek', 
    'Promotion', 
    'StateHoliday', 
    'SchoolHoliday', 
    'StoreType', 
    'AssortmentType'
]

X = d[features]
X = pd.get_dummies(X)

Y = d['Sales']

# Defining the HP parameters for xgboost
hp = {
    'objective': 'reg:squarederror',
    'n_estimators': 120
}

# Initiating the xgb model 
model = xgb.XGBRegressor(**hp)

# Fiting on data 
start = time.time()
model.fit(X, Y)
print(f"Time taken to build the model: {time.time() - start} s\n")