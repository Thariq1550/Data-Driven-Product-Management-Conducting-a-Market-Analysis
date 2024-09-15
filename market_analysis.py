# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

#Question 1 - Finding when the 'workout'at its peak
workout_df = pd.read_csv("data/workout.csv")
popularity_dec_sorted = workout_df.sort_values(by='workout_worldwide',ascending=False)
year = popularity_dec_sorted.iloc[0]['month']
year_str = year[:4]
print(year_str)

#Question 2 - Popular keyword now and then
three_keywords_df = pd.read_csv("data/three_keywords.csv")

covid_3k_df = three_keywords_df[three_keywords_df['month'].str[:4] == '2020']

hw_covid_dec_sorted = covid_3k_df.sort_values(by='home_workout_worldwide',ascending=False)
gw_covid_dec_sorted = covid_3k_df.sort_values(by='gym_workout_worldwide',ascending=False)
hg_covid_dec_sorted = covid_3k_df.sort_values(by='home_gym_worldwide',ascending=False)

pop_hw_covid = hw_covid_dec_sorted.iloc[0]['home_workout_worldwide']
pop_gw_covid = gw_covid_dec_sorted.iloc[0]['gym_workout_worldwide']
pop_hg_covid = hg_covid_dec_sorted.iloc[0]['home_gym_worldwide']

if(pop_hw_covid > pop_gw_covid and pop_hw_covid > pop_hg_covid):
    peak_covid = "home_workout_worldwide"
elif(pop_gw_covid > pop_hg_covid):
    peak_covid = "gym_workout_worldwide"
else:
    peak_covid = "home_gym_worldwide"
    
print("The popular keyword during covid was "+ peak_covid)

current_df = three_keywords_df.iloc[-1]

hw_current = current_df['home_workout_worldwide']
gw_current = current_df['gym_workout_worldwide']
hg_current = current_df['home_gym_worldwide']   

if(hw_current > gw_current and hw_current > hg_current):
    current = "home_workout_worldwide"
elif(gw_current > hg_current):
    current = "gym_workout_worldwide"
else:
    current = "home_gym_worldwide"
    
print("The current popular keyword is "+ current)

#Question 3 - Country with the highest interests for workouts
workout_geo_df = pd.read_csv("data/workout_geo.csv")
geo_sorted = workout_geo_df.sort_values(by='workout_2018_2023',ascending=False)
top_country = geo_sorted.iloc[0]['country']
print("The popular country is " + top_country)

#Question 4
three_keywords_geo_df = pd.read_csv("data/three_keywords_geo.csv")

home_workout_geo_df = three_keywords_geo_df[['Country','home_workout_2018_2023']]


philippines_value_li = home_workout_geo_df.loc[home_workout_geo_df['Country']=='Philippines'].values[0]
philippines_value = philippines_value_li[1]

malaysia_value_li = home_workout_geo_df.loc[home_workout_geo_df['Country']=='Malaysia'].values[0]
malaysia_value = malaysia_value_li[1]

if(philippines_value>malaysia_value):
    home_workout_geo = "Philippines"
else:
    home_workout_geo = "Malaysia"
    
print("The best company to expant to is " + home_workout_geo)   