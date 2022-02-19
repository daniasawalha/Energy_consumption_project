import pandas as pd

train = pd.read_csv("train.csv")
test= pd.read_csv("test.csv")

# Columns that will be droped and will not be included in the calculations
ignore_list=['Year_Factor','State_Factor','building_class'
             ,'facility_type','floor_area','year_built',
             'direction_max_wind_speed','direction_peak_wind_speed'
             ,'max_wind_speed','days_with_fog','site_eui','id']
target='site_eui'
no_usar=['site_eui','id']

#replacing rest of the values with mean
train['year_built'] = train['year_built'].fillna(2013)
train['energy_star_rating'] = train['energy_star_rating'].fillna(train['energy_star_rating'].mean())
train['direction_max_wind_speed'] = train['direction_max_wind_speed'].fillna(train['direction_max_wind_speed'].mean())
train['direction_peak_wind_speed'] = train['direction_peak_wind_speed'].fillna(train['direction_peak_wind_speed'].mean())
train['max_wind_speed'] = train['max_wind_speed'].fillna(train['max_wind_speed'].mean())
train['days_with_fog'] = train['days_with_fog'].fillna(train['days_with_fog'].mean())

##for testdata

# year_built: replace with current year.
test['year_built'] = test['year_built'].fillna(2013)
#replacing rest of the values with mean
test['energy_star_rating'] = test['energy_star_rating'].fillna(test['energy_star_rating'].mean())
test['direction_max_wind_speed'] = test['direction_max_wind_speed'].fillna(test['direction_max_wind_speed'].mean())
test['direction_peak_wind_speed'] = test['direction_peak_wind_speed'].fillna(test['direction_peak_wind_speed'].mean())
test['max_wind_speed'] = test['max_wind_speed'].fillna(test['max_wind_speed'].mean())
test['days_with_fog'] = test['days_with_fog'].fillna(test['days_with_fog'].mean())

for i in train.columns:
    if i in ignore_list:
         train.drop(i, axis=1, inplace=True)
       
for i in test.columns:
    if i in ignore_list:
         test.drop(i, axis=1, inplace=True)

#print(train)
#print(test)