#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[5]:


file_1 = pd.read_csv("Top_10k_MidAtlantic.csv")
file_1.info()


# In[6]:


# subdivide each category from the master dataset

body_care = file_1[file_1["Department"].isin(["BODY CARE"])]
body_care_1 = body_care[["Description", "UPC", "Department", "SalesAnnual", "Sales, Yago Annual", "Sales % Annual", "Sales 3Q", "Sales, Yago 3Q", "Sales 4Q", "Sales, Yago 4Q", "Sales 1Q", "Sales, Yago 1Q", "Sales 2Q", "Sales, Yago 2Q"]]
body_care_1 = body_care_1.replace([np.inf, -np.inf, np.nan], 0)

general_merchandise = file_1[file_1["Department"].isin(["GENERAL MERCHANDISE"])]
general_merchandise_1 = general_merchandise[["Description", "UPC", "Department", "SalesAnnual", "Sales, Yago Annual", "Sales % Annual", "Sales 3Q", "Sales, Yago 3Q", "Sales 4Q", "Sales, Yago 4Q", "Sales 1Q", "Sales, Yago 1Q", "Sales 2Q", "Sales, Yago 2Q"]]
general_merchandise_1 = general_merchandise_1.replace([np.inf, -np.inf, np.nan], 0)

medicine = file_1[file_1["Department"].isin(["MEDICINE & PERSONAL HEALTH"])]
medicine_1 = medicine[["Description", "UPC", "Department", "SalesAnnual", "Sales, Yago Annual", "Sales % Annual", "Sales 3Q", "Sales, Yago 3Q", "Sales 4Q", "Sales, Yago 4Q", "Sales 1Q", "Sales, Yago 1Q", "Sales 2Q", "Sales, Yago 2Q"]]
medicine_1 = medicine_1.replace([np.inf, -np.inf, np.nan], 0)

alcohol = file_1[file_1["Department"].isin(["ALCOHOL"])]
alcohol_1 = alcohol[["Description", "UPC", "Department", "SalesAnnual", "Sales, Yago Annual", "Sales % Annual", "Sales 3Q", "Sales, Yago 3Q", "Sales 4Q", "Sales, Yago 4Q", "Sales 1Q", "Sales, Yago 1Q", "Sales 2Q", "Sales, Yago 2Q"]]
alcohol_1 = alcohol_1.replace([np.inf, -np.inf, np.nan], 0)

refrigerate = file_1[file_1["Department"].isin(["REFRIGERATED"])]
refrigerate_1 = refrigerate[["Description", "UPC", "Department", "SalesAnnual", "Sales, Yago Annual", "Sales % Annual", "Sales 3Q", "Sales, Yago 3Q", "Sales 4Q", "Sales, Yago 4Q", "Sales 1Q", "Sales, Yago 1Q", "Sales 2Q", "Sales, Yago 2Q"]]
refrigerate_1 = refrigerate_1.replace([np.inf, -np.inf, np.nan], 0)

vitamin = file_1[file_1["Department"].isin(["VITAMINS & SUPPLEMENTS"])]
vitamin_1 = vitamin[["Description", "UPC", "Department", "SalesAnnual", "Sales, Yago Annual", "Sales % Annual", "Sales 3Q", "Sales, Yago 3Q", "Sales 4Q", "Sales, Yago 4Q", "Sales 1Q", "Sales, Yago 1Q", "Sales 2Q", "Sales, Yago 2Q"]]
vitamin_1 = vitamin_1.replace([np.inf, -np.inf, np.nan], 0)

pet = file_1[file_1["Department"].isin(["PET"])]
pet_1 = pet[["Description", "UPC", "Department", "SalesAnnual", "Sales, Yago Annual", "Sales % Annual", "Sales 3Q", "Sales, Yago 3Q", "Sales 4Q", "Sales, Yago 4Q", "Sales 1Q", "Sales, Yago 1Q", "Sales 2Q", "Sales, Yago 2Q"]]
pet_1 = pet_1.replace([np.inf, -np.inf, np.nan], 0)

produce = file_1[file_1["Department"].isin(["PRODUCE"])]
produce_1 = produce[["Description", "UPC", "Department", "SalesAnnual", "Sales, Yago Annual", "Sales % Annual", "Sales 3Q", "Sales, Yago 3Q", "Sales 4Q", "Sales, Yago 4Q", "Sales 1Q", "Sales, Yago 1Q", "Sales 2Q", "Sales, Yago 2Q"]]
produce_1 = produce_1.replace([np.inf, -np.inf, np.nan], 0)

grocery = file_1[file_1["Department"].isin(["GROCERY"])]
grocery_1 = grocery[["Description", "UPC", "Department", "SalesAnnual", "Sales, Yago Annual", "Sales % Annual", "Sales 3Q", "Sales, Yago 3Q", "Sales 4Q", "Sales, Yago 4Q", "Sales 1Q", "Sales, Yago 1Q", "Sales 2Q", "Sales, Yago 2Q"]]
grocery_1 = grocery_1.replace([np.inf, -np.inf, np.nan], 0)

frozen = file_1[file_1["Department"].isin(["FROZEN"])]
frozen_1 = frozen[["Description", "UPC", "Department", "SalesAnnual", "Sales, Yago Annual", "Sales % Annual", "Sales 3Q", "Sales, Yago 3Q", "Sales 4Q", "Sales, Yago 4Q", "Sales 1Q", "Sales, Yago 1Q", "Sales 2Q", "Sales, Yago 2Q"]]
frozen_1 = frozen_1.replace([np.inf, -np.inf, np.nan], 0)

other = file_1[file_1["Department"].isin(["OTHER"])]
other_1 = other[["Description", "UPC", "Department", "SalesAnnual", "Sales, Yago Annual", "Sales % Annual", "Sales 3Q", "Sales, Yago 3Q", "Sales 4Q", "Sales, Yago 4Q", "Sales 1Q", "Sales, Yago 1Q", "Sales 2Q", "Sales, Yago 2Q"]]
other_1 = other_1.replace([np.inf, -np.inf, np.nan], 0)


# In[7]:


# body_care_1.set_index("UPC", inplace = True)
# general_merchandise_1.set_index("UPC", inplace = True)
# medicine_1.set_index("UPC", inplace = True)
# alcohol_1.set_index("UPC", inplace = True)
# refrigerate_1.set_index("UPC", inplace = True)
# vitamin_1.set_index("UPC", inplace = True)
# pet_1.set_index("UPC", inplace = True)
# produce_1.set_index("UPC", inplace = True)
# grocery_1.set_index("UPC", inplace = True)
# frozen_1.set_index("UPC", inplace = True)
# other_1.set_index("UPC", inplace = True)


body_care_mean = body_care_1["Sales % Annual"].mean()
body_care_median = body_care_1["Sales % Annual"].median()
body_care_IQR_Q1 = np.percentile(body_care_1["Sales % Annual"], 25)

general_merchandise_mean = general_merchandise_1["Sales % Annual"].mean()
general_merchandise_median = general_merchandise_1["Sales % Annual"].median()
general_merchandise_IQR_Q1 = np.percentile(general_merchandise_1["Sales % Annual"], 25)

medicine_mean = medicine_1["Sales % Annual"].mean()
medicine_median = medicine_1["Sales % Annual"].median()
medicine_IQR_Q1 = np.percentile(medicine_1["Sales % Annual"], 25)

alcohol_mean = alcohol_1["Sales % Annual"].mean()
alcohol_median = alcohol_1["Sales % Annual"].median()
alcohol_IQR_Q1 = np.percentile(alcohol_1["Sales % Annual"], 25)

refrigerate_mean = refrigerate_1["Sales % Annual"].mean()
refrigerate_median = refrigerate_1["Sales % Annual"].median()
refrigerate_IQR_Q1 = np.percentile(refrigerate_1["Sales % Annual"], 25)

vitamin_mean = vitamin_1["Sales % Annual"].mean()
vitamin_median = vitamin_1["Sales % Annual"].median()
vitamin_IQR_Q1 = np.percentile(vitamin_1["Sales % Annual"], 25)

pet_mean = pet_1["Sales % Annual"].mean()
pet_median = pet_1["Sales % Annual"].median()
pet_IQR_Q1 = np.percentile(pet_1["Sales % Annual"], 25)

produce_mean = produce_1["Sales % Annual"].mean()
produce_median = produce_1["Sales % Annual"].median()
produce_IQR_Q1 = np.percentile(produce_1["Sales % Annual"], 25)

grocery_mean = grocery_1["Sales % Annual"].mean()
grocery_median = grocery_1["Sales % Annual"].median()
grocery_IQR_Q1 = np.percentile(grocery_1["Sales % Annual"], 25)

frozen_mean = frozen_1["Sales % Annual"].mean()
frozen_median = frozen_1["Sales % Annual"].median()
frozen_IQR_Q1 = np.percentile(frozen_1["Sales % Annual"], 25)

other_mean = other_1["Sales % Annual"].mean()
other_median = other_1["Sales % Annual"].median()
other_IQR_Q1 = np.percentile(other_1["Sales % Annual"], 25)

# numpy.percentile(values, 65)


# In[161]:


# UPC count distribution by Department (Category)

file_2 = file_1[["UPC", "Department"]]
print(file_2.head(3))

upc_count = file_2.groupby(["Department"])["UPC"].count().reset_index(name="Count").sort_values("Count",ascending = False)
print(upc_count)


upc_count_1 = pd.DataFrame({'Count': upc_count["Count"], 'Department': upc_count["Department"]})

# plot

g = sns.catplot(kind='bar', data=upc_count_1, x='Department', y='Count', height=6, aspect=2)
# iterate through the axes
for ax in g.axes.flat:

    ax.bar_label(ax.containers[0], label_type='edge')

    ax.margins(y= 0.1)
    
g.set_xticklabels(rotation=60)


# In[174]:


# Annual Sales distribution by Department (Category)

file_3 = file_1[["SalesAnnual", "Department"]]
salesannual = file_3.groupby("Department")["SalesAnnual"].sum().reset_index(name = "SalesAnnual").sort_values("SalesAnnual",ascending = False)

salesannual_1 = pd.DataFrame({'SalesAnnual' : salesannual["SalesAnnual"], 'Department' : salesannual["Department"]})
print(salesannual_1)

g_1 = sns.catplot(kind='bar', data=salesannual_1, x='Department', y='SalesAnnual', height=6, aspect=2)

for ax in g_1.axes.flat:

    ax.bar_label(ax.containers[0], labels=[f'{x.get_height():.0f}' for x in ax.containers[0]],label_type='edge')

    ax.margins(y= 0.1)

g_1.set_xticklabels(rotation=60)
    
plt.ticklabel_format(style='plain', axis='y')


# In[177]:


# Annual % Sales mean value distribution by Department (Category)

file_4 = file_1[["Sales % Annual", "Department"]]
saleschange = file_4.groupby("Department")["Sales % Annual"].mean().reset_index(name = "Sales % Change").sort_values("Sales % Change", ascending = False)

saleschange_1 = pd.DataFrame({'Sales % Change' : saleschange["Sales % Change"], 'Department' : saleschange["Department"]})
print(saleschange_1)

g_2 = sns.catplot(kind='bar', data=saleschange_1, x='Department', y='Sales % Change', height=6, aspect=2)

for ax in g_2.axes.flat:

    ax.bar_label(ax.containers[0], labels = [f'{x.get_height()*100: .2f}%' for x in ax.containers[0]], label_type='edge')
 
    ax.margins(y= 0.1)
    
g_2.set_xticklabels(rotation=60)


# In[11]:


# sort the upc lists above 25% of quartile range

body_care_1["IQR_25"] = body_care_IQR_Q1
produce_1["IQR_25"] = produce_IQR_Q1
pet_1["IQR_25"] = pet_IQR_Q1
other_1["IQR_25"] = other_IQR_Q1
refrigerate_1["IQR_25"] = refrigerate_IQR_Q1
medicine_1["IQR_25"] = medicine_IQR_Q1
grocery_1["IQR_25"] = grocery_IQR_Q1
vitamin_1["IQR_25"] = vitamin_IQR_Q1
general_merchandise_1["IQR_25"] = general_merchandise_IQR_Q1
frozen_1["IQR_25"] = frozen_IQR_Q1
alcohol_1["IQR_25"] = alcohol_IQR_Q1


body_care_1.loc[body_care_1["Sales % Annual"] >= body_care_1["IQR_25"], "Pass Y/N"] = "Y"
body_care_1.loc[body_care_1["Sales % Annual"] < body_care_1["IQR_25"], "Pass Y/N"] = "N"

produce_1.loc[produce_1["Sales % Annual"] >= produce_1["IQR_25"], "Pass Y/N"] = "Y"
produce_1.loc[produce_1["Sales % Annual"] < produce_1["IQR_25"], "Pass Y/N"] = "N"

pet_1.loc[pet_1["Sales % Annual"] >= pet_1["IQR_25"], "Pass Y/N"] = "Y"
pet_1.loc[pet_1["Sales % Annual"] < pet_1["IQR_25"], "Pass Y/N"] = "N"

other_1.loc[other_1["Sales % Annual"] >= other_1["IQR_25"], "Pass Y/N"] = "Y"
other_1.loc[other_1["Sales % Annual"] < other_1["IQR_25"], "Pass Y/N"] = "N"

refrigerate_1.loc[refrigerate_1["Sales % Annual"] >= refrigerate_1["IQR_25"], "Pass Y/N"] = "Y"
refrigerate_1.loc[refrigerate_1["Sales % Annual"] < refrigerate_1["IQR_25"], "Pass Y/N"] = "N"

medicine_1.loc[medicine_1["Sales % Annual"] >= medicine_1["IQR_25"], "Pass Y/N"] = "Y"
medicine_1.loc[medicine_1["Sales % Annual"] < medicine_1["IQR_25"], "Pass Y/N"] = "N"

grocery_1.loc[grocery_1["Sales % Annual"] >= grocery_1["IQR_25"], "Pass Y/N"] = "Y"
grocery_1.loc[grocery_1["Sales % Annual"] < grocery_1["IQR_25"], "Pass Y/N"] = "N"

vitamin_1.loc[vitamin_1["Sales % Annual"] >= vitamin_1["IQR_25"], "Pass Y/N"] = "Y"
vitamin_1.loc[vitamin_1["Sales % Annual"] < vitamin_1["IQR_25"], "Pass Y/N"] = "N"

general_merchandise_1.loc[general_merchandise_1["Sales % Annual"] >= general_merchandise_1["IQR_25"], "Pass Y/N"] = "Y"
general_merchandise_1.loc[general_merchandise_1["Sales % Annual"] < general_merchandise_1["IQR_25"], "Pass Y/N"] = "N"

frozen_1.loc[frozen_1["Sales % Annual"] >= frozen_1["IQR_25"], "Pass Y/N"] = "Y"
frozen_1.loc[frozen_1["Sales % Annual"] < frozen_1["IQR_25"], "Pass Y/N"] = "N"

alcohol_1.loc[alcohol_1["Sales % Annual"] >= alcohol_1["IQR_25"], "Pass Y/N"] = "Y"
alcohol_1.loc[alcohol_1["Sales % Annual"] < alcohol_1["IQR_25"], "Pass Y/N"] = "N"


# In[12]:


# sort

body_care_2 = body_care_1[body_care_1["Pass Y/N"] == "Y"].reset_index()
body_care_sort = body_care_2[["UPC", "Description", "Department", "SalesAnnual", "Sales, Yago Annual", "Sales % Annual" , "Sales 4Q"]]

produce_2 = produce_1[produce_1["Pass Y/N"] == "Y"].reset_index()
produce_sort = produce_2[["UPC", "Description", "Department", "SalesAnnual", "Sales, Yago Annual", "Sales % Annual", "Sales 4Q"]]

pet_2 = pet_1[pet_1["Pass Y/N"] == "Y"].reset_index()
pet_sort = pet_2[["UPC", "Description", "Department", "SalesAnnual", "Sales, Yago Annual", "Sales % Annual" , "Sales 4Q"]]

other_2 = other_1[other_1["Pass Y/N"] == "Y"].reset_index()
other_sort = other_2[["UPC", "Description", "Department", "SalesAnnual", "Sales, Yago Annual", "Sales % Annual" , "Sales 4Q"]]

refrigerate_2 = refrigerate_1[refrigerate_1["Pass Y/N"] == "Y"].reset_index()
refrigerate_sort = refrigerate_2[["UPC", "Description", "Department", "SalesAnnual", "Sales, Yago Annual", "Sales % Annual" , "Sales 4Q"]]

grocery_2 = grocery_1[grocery_1["Pass Y/N"] == "Y"].reset_index()
grocery_sort = grocery_2[["UPC", "Description", "Department", "SalesAnnual", "Sales, Yago Annual", "Sales % Annual" , "Sales 4Q"]]

vitamin_2 = vitamin_1[vitamin_1["Pass Y/N"] == "Y"].reset_index()
vitamin_sort = vitamin_2[["UPC", "Description", "Department", "SalesAnnual", "Sales, Yago Annual", "Sales % Annual" , "Sales 4Q"]]

general_merchandise_2 = general_merchandise_1[general_merchandise_1["Pass Y/N"] == "Y"].reset_index()
general_merchandise_sort = general_merchandise_2[["UPC", "Description", "Department", "SalesAnnual", "Sales, Yago Annual", "Sales % Annual" , "Sales 4Q"]]

frozen_2 = frozen_1[frozen_1["Pass Y/N"] == "Y"].reset_index()
frozen_sort = frozen_2[["UPC", "Description", "Department", "SalesAnnual", "Sales, Yago Annual", "Sales % Annual" , "Sales 4Q"]]

alcohol_2 = alcohol_1[alcohol_1["Pass Y/N"] == "Y"].reset_index()
alcohol_sort = alcohol_2[["UPC", "Description", "Department", "SalesAnnual", "Sales, Yago Annual", "Sales % Annual" , "Sales 4Q"]]

medicine_2 = medicine_1[medicine_1["Pass Y/N"] == "Y"].reset_index()
medicine_sort = medicine_2[["UPC", "Description", "Department", "SalesAnnual", "Sales, Yago Annual", "Sales % Annual" , "Sales 4Q"]]


# In[12]:


selected_list_1 = pd.concat([body_care_sort, produce_sort, pet_sort, other_sort, refrigerate_sort, grocery_sort,                            vitamin_sort, general_merchandise_sort, frozen_sort, alcohol_sort], axis = 0)

print(selected_list_1)


# In[13]:


# test

import openpyxl
body_care_2.to_excel('test.xlsx', sheet_name='new_sheet_name')


# In[14]:


# remove seasonal items by checking drastic surge on the quarterly sales change in between two consecutive quarters

# add columns (Q3 - Q4 % change / Q4 - Q1 % change / Q1 - Q2 % change)

body_care_2["Q3/Q4 % Change"] = (body_care_2["Sales 4Q"] - body_care_2["Sales 3Q"]) / body_care_2["Sales 4Q"]
body_care_2["Q4/Q1 % Change"] = (body_care_2["Sales 1Q"] - body_care_2["Sales 4Q"]) / body_care_2["Sales 1Q"]
body_care_2["Q1/Q2 % Change"] = (body_care_2["Sales 2Q"] - body_care_2["Sales 1Q"]) / body_care_2["Sales 2Q"]
 
body_care_3 = body_care_2.replace([np.inf, -np.inf, np.nan], 0).fillna(0)
body_care_3 = body_care_3[["UPC", "Q3/Q4 % Change", "Q4/Q1 % Change", "Q1/Q2 % Change"]]

produce_2["Q3/Q4 % Change"] = (produce_2["Sales 4Q"] - produce_2["Sales 3Q"]) / produce_2["Sales 4Q"]
produce_2["Q4/Q1 % Change"] = (produce_2["Sales 1Q"] - produce_2["Sales 4Q"]) / produce_2["Sales 1Q"]
produce_2["Q1/Q2 % Change"] = (produce_2["Sales 2Q"] - produce_2["Sales 1Q"]) / produce_2["Sales 2Q"]
 
produce_3 = produce_2.replace([np.inf, -np.inf, np.nan], 0)
produce_3 = produce_3[["UPC", "Q3/Q4 % Change", "Q4/Q1 % Change", "Q1/Q2 % Change"]]

pet_2["Q3/Q4 % Change"] = (pet_2["Sales 4Q"] - pet_2["Sales 3Q"]) / pet_2["Sales 4Q"]
pet_2["Q4/Q1 % Change"] = (pet_2["Sales 1Q"] - pet_2["Sales 4Q"]) / pet_2["Sales 1Q"]
pet_2["Q1/Q2 % Change"] = (pet_2["Sales 2Q"] - pet_2["Sales 1Q"]) / pet_2["Sales 2Q"]
 
pet_3 = pet_2.replace([np.inf, -np.inf, np.nan], 0)
pet_3 = pet_3[["UPC", "Q3/Q4 % Change", "Q4/Q1 % Change", "Q1/Q2 % Change"]]

other_2["Q3/Q4 % Change"] = (other_2["Sales 4Q"] - other_2["Sales 3Q"]) / other_2["Sales 4Q"]
other_2["Q4/Q1 % Change"] = (other_2["Sales 1Q"] - other_2["Sales 4Q"]) / other_2["Sales 1Q"]
other_2["Q1/Q2 % Change"] = (other_2["Sales 2Q"] - other_2["Sales 1Q"]) / other_2["Sales 2Q"]
 
other_3 = other_2.replace([np.inf, -np.inf, np.nan], 0)
other_3 = other_3[["UPC", "Q3/Q4 % Change", "Q4/Q1 % Change", "Q1/Q2 % Change"]]

refrigerate_2["Q3/Q4 % Change"] = (refrigerate_2["Sales 4Q"] - refrigerate_2["Sales 3Q"]) / refrigerate_2["Sales 4Q"]
refrigerate_2["Q4/Q1 % Change"] = (refrigerate_2["Sales 1Q"] - refrigerate_2["Sales 4Q"]) / refrigerate_2["Sales 1Q"]
refrigerate_2["Q1/Q2 % Change"] = (refrigerate_2["Sales 2Q"] - refrigerate_2["Sales 1Q"]) / refrigerate_2["Sales 2Q"]
 
refrigerate_3 = refrigerate_2.replace([np.inf, -np.inf, np.nan], 0)
refrigerate_3 = refrigerate_3[["UPC", "Q3/Q4 % Change", "Q4/Q1 % Change", "Q1/Q2 % Change"]]

grocery_2["Q3/Q4 % Change"] = (grocery_2["Sales 4Q"] - grocery_2["Sales 3Q"]) / grocery_2["Sales 4Q"]
grocery_2["Q4/Q1 % Change"] = (grocery_2["Sales 1Q"] - grocery_2["Sales 4Q"]) / grocery_2["Sales 1Q"]
grocery_2["Q1/Q2 % Change"] = (grocery_2["Sales 2Q"] - grocery_2["Sales 1Q"]) / grocery_2["Sales 2Q"]
 
grocery_3 = grocery_2.replace([np.inf, -np.inf, np.nan], 0)
grocery_3 = grocery_3[["UPC", "Q3/Q4 % Change", "Q4/Q1 % Change", "Q1/Q2 % Change"]]

vitamin_2["Q3/Q4 % Change"] = (vitamin_2["Sales 4Q"] - vitamin_2["Sales 3Q"]) / vitamin_2["Sales 4Q"]
vitamin_2["Q4/Q1 % Change"] = (vitamin_2["Sales 1Q"] - vitamin_2["Sales 4Q"]) / vitamin_2["Sales 1Q"]
vitamin_2["Q1/Q2 % Change"] = (vitamin_2["Sales 2Q"] - vitamin_2["Sales 1Q"]) / vitamin_2["Sales 2Q"]
 
vitamin_3 = vitamin_2.replace([np.inf, -np.inf, np.nan], 0)
vitamin_3 = vitamin_3[["UPC", "Q3/Q4 % Change", "Q4/Q1 % Change", "Q1/Q2 % Change"]]

general_merchandise_2["Q3/Q4 % Change"] = (general_merchandise_2["Sales 4Q"] - general_merchandise_2["Sales 3Q"]) / general_merchandise_2["Sales 4Q"]
general_merchandise_2["Q4/Q1 % Change"] = (general_merchandise_2["Sales 1Q"] - general_merchandise_2["Sales 4Q"]) / general_merchandise_2["Sales 1Q"]
general_merchandise_2["Q1/Q2 % Change"] = (general_merchandise_2["Sales 2Q"] - general_merchandise_2["Sales 1Q"]) / general_merchandise_2["Sales 2Q"]
 
general_merchandise_3 = general_merchandise_2.replace([np.inf, -np.inf, np.nan], 0)
general_merchandise_3 = general_merchandise_3[["UPC", "Q3/Q4 % Change", "Q4/Q1 % Change", "Q1/Q2 % Change"]]

frozen_2["Q3/Q4 % Change"] = (frozen_2["Sales 4Q"] - frozen_2["Sales 3Q"]) / frozen_2["Sales 4Q"]
frozen_2["Q4/Q1 % Change"] = (frozen_2["Sales 1Q"] - frozen_2["Sales 4Q"]) / frozen_2["Sales 1Q"]
frozen_2["Q1/Q2 % Change"] = (frozen_2["Sales 2Q"] - frozen_2["Sales 1Q"]) / frozen_2["Sales 2Q"]
 
frozen_3 = frozen_2.replace([np.inf, -np.inf, np.nan], 0)
frozen_3 = frozen_3[["UPC", "Q3/Q4 % Change", "Q4/Q1 % Change", "Q1/Q2 % Change"]]

alcohol_2["Q3/Q4 % Change"] = (alcohol_2["Sales 4Q"] - alcohol_2["Sales 3Q"]) / alcohol_2["Sales 4Q"]
alcohol_2["Q4/Q1 % Change"] = (alcohol_2["Sales 1Q"] - alcohol_2["Sales 4Q"]) / alcohol_2["Sales 1Q"]
alcohol_2["Q1/Q2 % Change"] = (alcohol_2["Sales 2Q"] - alcohol_2["Sales 1Q"]) / alcohol_2["Sales 2Q"]
 
alcohol_3 = alcohol_2.replace([np.inf, -np.inf, np.nan], 0)
alcohol_3 = alcohol_3[["UPC", "Q3/Q4 % Change", "Q4/Q1 % Change", "Q1/Q2 % Change"]]

medicine_2["Q3/Q4 % Change"] = (medicine_2["Sales 4Q"] - medicine_2["Sales 3Q"]) / medicine_2["Sales 4Q"]
medicine_2["Q4/Q1 % Change"] = (medicine_2["Sales 1Q"] - medicine_2["Sales 4Q"]) / medicine_2["Sales 1Q"]
medicine_2["Q1/Q2 % Change"] = (medicine_2["Sales 2Q"] - medicine_2["Sales 1Q"]) / medicine_2["Sales 2Q"]
 
medicine_3 = medicine_2.replace([np.inf, -np.inf, np.nan], 0)
medicine_3 = medicine_3[["UPC", "Q3/Q4 % Change", "Q4/Q1 % Change", "Q1/Q2 % Change"]]


# 1-2. Quartile maximum -- (Q1 + (Q3 - Q1)*1.5)
# 1-3. Quartile minimum -- (Q1 - (Q3 - Q1)*1.5)

# body_care 

body_care_Q34_Q1 = np.percentile(body_care_3["Q3/Q4 % Change"], 25)
body_care_Q34_Q3 = np.percentile(body_care_3["Q3/Q4 % Change"], 75)
body_care_Q34_max = body_care_Q34_Q1 + (body_care_Q34_Q3 - body_care_Q34_Q1) * 1.5
body_care_Q34_min = body_care_Q34_Q1 - (body_care_Q34_Q3 - body_care_Q34_Q1) * 1.5

body_care_Q41_Q1 = np.percentile(body_care_3["Q4/Q1 % Change"], 25)
body_care_Q41_Q3 = np.percentile(body_care_3["Q4/Q1 % Change"], 75)
body_care_Q41_max = body_care_Q41_Q1 + (body_care_Q41_Q3 - body_care_Q41_Q1) * 1.5 
body_care_Q41_min = body_care_Q41_Q1 - (body_care_Q41_Q3 - body_care_Q41_Q1) * 1.5

body_care_Q12_Q1 = np.percentile(body_care_3["Q1/Q2 % Change"], 25)
body_care_Q12_Q3 = np.percentile(body_care_3["Q1/Q2 % Change"], 75)
body_care_Q12_max = body_care_Q12_Q1 + (body_care_Q12_Q3 - body_care_Q12_Q1) * 1.5 
body_care_Q12_min = body_care_Q12_Q1 - (body_care_Q12_Q3 - body_care_Q12_Q1) * 1.5


# produce

produce_Q34_Q1 = np.percentile(produce_3["Q3/Q4 % Change"], 25)
produce_Q34_Q3 = np.percentile(produce_3["Q3/Q4 % Change"], 75)
produce_Q34_max = produce_Q34_Q1 + (produce_Q34_Q3 - produce_Q34_Q1) * 1.5
produce_Q34_min = produce_Q34_Q1 - (produce_Q34_Q3 - produce_Q34_Q1) * 1.5

produce_Q41_Q1 = np.percentile(produce_3["Q4/Q1 % Change"], 25)
produce_Q41_Q3 = np.percentile(produce_3["Q4/Q1 % Change"], 75)
produce_Q41_max = produce_Q41_Q1 + (produce_Q41_Q3 - produce_Q41_Q1) * 1.5 
produce_Q41_min = produce_Q41_Q1 - (produce_Q41_Q3 - produce_Q41_Q1) * 1.5

produce_Q12_Q1 = np.percentile(produce_3["Q1/Q2 % Change"], 25)
produce_Q12_Q3 = np.percentile(produce_3["Q1/Q2 % Change"], 75)
produce_Q12_max = produce_Q12_Q1 + (produce_Q12_Q3 - produce_Q12_Q1) * 1.5 
produce_Q12_min = produce_Q12_Q1 - (produce_Q12_Q3 - produce_Q12_Q1) * 1.5

# pet

pet_Q34_Q1 = np.percentile(pet_3["Q3/Q4 % Change"], 25)
pet_Q34_Q3 = np.percentile(pet_3["Q3/Q4 % Change"], 75)
pet_Q34_max = pet_Q34_Q1 + (pet_Q34_Q3 - pet_Q34_Q1) * 1.5
pet_Q34_min = pet_Q34_Q1 - (pet_Q34_Q3 - pet_Q34_Q1) * 1.5

pet_Q41_Q1 = np.percentile(pet_3["Q4/Q1 % Change"], 25)
pet_Q41_Q3 = np.percentile(pet_3["Q4/Q1 % Change"], 75)
pet_Q41_max = pet_Q41_Q1 + (pet_Q41_Q3 - pet_Q41_Q1) * 1.5 
pet_Q41_min = pet_Q41_Q1 - (pet_Q41_Q3 - pet_Q41_Q1) * 1.5

pet_Q12_Q1 = np.percentile(pet_3["Q1/Q2 % Change"], 25)
pet_Q12_Q3 = np.percentile(pet_3["Q1/Q2 % Change"], 75)
pet_Q12_max = pet_Q12_Q1 + (pet_Q12_Q3 - pet_Q12_Q1) * 1.5 
pet_Q12_min = pet_Q12_Q1 - (pet_Q12_Q3 - pet_Q12_Q1) * 1.5

# other

other_Q34_Q1 = np.percentile(other_3["Q3/Q4 % Change"], 25)
other_Q34_Q3 = np.percentile(other_3["Q3/Q4 % Change"], 75)
other_Q34_max = other_Q34_Q1 + (other_Q34_Q3 - other_Q34_Q1) * 1.5
other_Q34_min = other_Q34_Q1 - (other_Q34_Q3 - other_Q34_Q1) * 1.5

other_Q41_Q1 = np.percentile(other_3["Q4/Q1 % Change"], 25)
other_Q41_Q3 = np.percentile(other_3["Q4/Q1 % Change"], 75)
other_Q41_max = other_Q41_Q1 + (other_Q41_Q3 - other_Q41_Q1) * 1.5 
other_Q41_min = other_Q41_Q1 - (other_Q41_Q3 - other_Q41_Q1) * 1.5

other_Q12_Q1 = np.percentile(other_3["Q1/Q2 % Change"], 25)
other_Q12_Q3 = np.percentile(other_3["Q1/Q2 % Change"], 75)
other_Q12_max = other_Q12_Q1 + (other_Q12_Q3 - other_Q12_Q1) * 1.5 
other_Q12_min = other_Q12_Q1 - (other_Q12_Q3 - other_Q12_Q1) * 1.5


# refrigerate

refrigerate_Q34_Q1 = np.percentile(refrigerate_3["Q3/Q4 % Change"], 25)
refrigerate_Q34_Q3 = np.percentile(refrigerate_3["Q3/Q4 % Change"], 75)
refrigerate_Q34_max = refrigerate_Q34_Q1 + (refrigerate_Q34_Q3 - refrigerate_Q34_Q1) * 1.5
refrigerate_Q34_min = refrigerate_Q34_Q1 - (refrigerate_Q34_Q3 - refrigerate_Q34_Q1) * 1.5

refrigerate_Q41_Q1 = np.percentile(refrigerate_3["Q4/Q1 % Change"], 25)
refrigerate_Q41_Q3 = np.percentile(refrigerate_3["Q4/Q1 % Change"], 75)
refrigerate_Q41_max = refrigerate_Q41_Q1 + (refrigerate_Q41_Q3 - refrigerate_Q41_Q1) * 1.5 
refrigerate_Q41_min = refrigerate_Q41_Q1 - (refrigerate_Q41_Q3 - refrigerate_Q41_Q1) * 1.5

refrigerate_Q12_Q1 = np.percentile(refrigerate_3["Q1/Q2 % Change"], 25)
refrigerate_Q12_Q3 = np.percentile(refrigerate_3["Q1/Q2 % Change"], 75)
refrigerate_Q12_max = refrigerate_Q12_Q1 + (refrigerate_Q12_Q3 - refrigerate_Q12_Q1) * 1.5 
refrigerate_Q12_min = refrigerate_Q12_Q1 - (refrigerate_Q12_Q3 - refrigerate_Q12_Q1) * 1.5

# grocery

grocery_Q34_Q1 = np.percentile(grocery_3["Q3/Q4 % Change"], 25)
grocery_Q34_Q3 = np.percentile(grocery_3["Q3/Q4 % Change"], 75)
grocery_Q34_max = grocery_Q34_Q1 + (grocery_Q34_Q3 - grocery_Q34_Q1) * 1.5
grocery_Q34_min = grocery_Q34_Q1 - (grocery_Q34_Q3 - grocery_Q34_Q1) * 1.5

grocery_Q41_Q1 = np.percentile(grocery_3["Q4/Q1 % Change"], 25)
grocery_Q41_Q3 = np.percentile(grocery_3["Q4/Q1 % Change"], 75)
grocery_Q41_max = grocery_Q41_Q1 + (grocery_Q41_Q3 - grocery_Q41_Q1) * 1.5 
grocery_Q41_min = grocery_Q41_Q1 - (grocery_Q41_Q3 - grocery_Q41_Q1) * 1.5

grocery_Q12_Q1 = np.percentile(grocery_3["Q1/Q2 % Change"], 25)
grocery_Q12_Q3 = np.percentile(grocery_3["Q1/Q2 % Change"], 75)
grocery_Q12_max = grocery_Q12_Q1 + (grocery_Q12_Q3 - grocery_Q12_Q1) * 1.5 
grocery_Q12_min = grocery_Q12_Q1 - (grocery_Q12_Q3 - grocery_Q12_Q1) * 1.5

# vitamin

vitamin_Q34_Q1 = np.percentile(vitamin_3["Q3/Q4 % Change"], 25)
vitamin_Q34_Q3 = np.percentile(vitamin_3["Q3/Q4 % Change"], 75)
vitamin_Q34_max = vitamin_Q34_Q1 + (vitamin_Q34_Q3 - vitamin_Q34_Q1) * 1.5
vitamin_Q34_min = vitamin_Q34_Q1 - (vitamin_Q34_Q3 - vitamin_Q34_Q1) * 1.5

vitamin_Q41_Q1 = np.percentile(vitamin_3["Q4/Q1 % Change"], 25)
vitamin_Q41_Q3 = np.percentile(vitamin_3["Q4/Q1 % Change"], 75)
vitamin_Q41_max = vitamin_Q41_Q1 + (vitamin_Q41_Q3 - vitamin_Q41_Q1) * 1.5 
vitamin_Q41_min = vitamin_Q41_Q1 - (vitamin_Q41_Q3 - vitamin_Q41_Q1) * 1.5

vitamin_Q12_Q1 = np.percentile(vitamin_3["Q1/Q2 % Change"], 25)
vitamin_Q12_Q3 = np.percentile(vitamin_3["Q1/Q2 % Change"], 75)
vitamin_Q12_max = vitamin_Q12_Q1 + (vitamin_Q12_Q3 - vitamin_Q12_Q1) * 1.5 
vitamin_Q12_min = vitamin_Q12_Q1 - (vitamin_Q12_Q3 - vitamin_Q12_Q1) * 1.5



# general_merchandise

general_merchandise_Q34_Q1 = np.percentile(general_merchandise_3["Q3/Q4 % Change"], 25)
general_merchandise_Q34_Q3 = np.percentile(general_merchandise_3["Q3/Q4 % Change"], 75)
general_merchandise_Q34_max = general_merchandise_Q34_Q1 + (general_merchandise_Q34_Q3 - general_merchandise_Q34_Q1) * 1.5
general_merchandise_Q34_min = general_merchandise_Q34_Q1 - (general_merchandise_Q34_Q3 - general_merchandise_Q34_Q1) * 1.5

general_merchandise_Q41_Q1 = np.percentile(general_merchandise_3["Q4/Q1 % Change"], 25)
general_merchandise_Q41_Q3 = np.percentile(general_merchandise_3["Q4/Q1 % Change"], 75)
general_merchandise_Q41_max = general_merchandise_Q41_Q1 + (general_merchandise_Q41_Q3 - general_merchandise_Q41_Q1) * 1.5 
general_merchandise_Q41_min = general_merchandise_Q41_Q1 - (general_merchandise_Q41_Q3 - general_merchandise_Q41_Q1) * 1.5

general_merchandise_Q12_Q1 = np.percentile(general_merchandise_3["Q1/Q2 % Change"], 25)
general_merchandise_Q12_Q3 = np.percentile(general_merchandise_3["Q1/Q2 % Change"], 75)
general_merchandise_Q12_max = general_merchandise_Q12_Q1 + (general_merchandise_Q12_Q3 - general_merchandise_Q12_Q1) * 1.5 
general_merchandise_Q12_min = general_merchandise_Q12_Q1 - (general_merchandise_Q12_Q3 - general_merchandise_Q12_Q1) * 1.5


# frozen

frozen_Q34_Q1 = np.percentile(frozen_3["Q3/Q4 % Change"], 25)
frozen_Q34_Q3 = np.percentile(frozen_3["Q3/Q4 % Change"], 75)
frozen_Q34_max = frozen_Q34_Q1 + (frozen_Q34_Q3 - frozen_Q34_Q1) * 1.5
frozen_Q34_min = frozen_Q34_Q1 - (frozen_Q34_Q3 - frozen_Q34_Q1) * 1.5

frozen_Q41_Q1 = np.percentile(frozen_3["Q4/Q1 % Change"], 25)
frozen_Q41_Q3 = np.percentile(frozen_3["Q4/Q1 % Change"], 75)
frozen_Q41_max = frozen_Q41_Q1 + (frozen_Q41_Q3 - frozen_Q41_Q1) * 1.5 
frozen_Q41_min = frozen_Q41_Q1 - (frozen_Q41_Q3 - frozen_Q41_Q1) * 1.5

frozen_Q12_Q1 = np.percentile(frozen_3["Q1/Q2 % Change"], 25)
frozen_Q12_Q3 = np.percentile(frozen_3["Q1/Q2 % Change"], 75)
frozen_Q12_max = frozen_Q12_Q1 + (frozen_Q12_Q3 - frozen_Q12_Q1) * 1.5 
frozen_Q12_min = frozen_Q12_Q1 - (frozen_Q12_Q3 - frozen_Q12_Q1) * 1.5


# alcohol

alcohol_Q34_Q1 = np.percentile(alcohol_3["Q3/Q4 % Change"], 25)
alcohol_Q34_Q3 = np.percentile(alcohol_3["Q3/Q4 % Change"], 75)
alcohol_Q34_max = alcohol_Q34_Q1 + (alcohol_Q34_Q3 - alcohol_Q34_Q1) * 1.5
alcohol_Q34_min = alcohol_Q34_Q1 - (alcohol_Q34_Q3 - alcohol_Q34_Q1) * 1.5

alcohol_Q41_Q1 = np.percentile(alcohol_3["Q4/Q1 % Change"], 25)
alcohol_Q41_Q3 = np.percentile(alcohol_3["Q4/Q1 % Change"], 75)
alcohol_Q41_max = alcohol_Q41_Q1 + (alcohol_Q41_Q3 - alcohol_Q41_Q1) * 1.5 
alcohol_Q41_min = alcohol_Q41_Q1 - (alcohol_Q41_Q3 - alcohol_Q41_Q1) * 1.5

alcohol_Q12_Q1 = np.percentile(alcohol_3["Q1/Q2 % Change"], 25)
alcohol_Q12_Q3 = np.percentile(alcohol_3["Q1/Q2 % Change"], 75)
alcohol_Q12_max = alcohol_Q12_Q1 + (alcohol_Q12_Q3 - alcohol_Q12_Q1) * 1.5 
alcohol_Q12_min = alcohol_Q12_Q1 - (alcohol_Q12_Q3 - alcohol_Q12_Q1) * 1.5



# medicine

medicine_Q34_Q1 = np.percentile(medicine_3["Q3/Q4 % Change"], 25)
medicine_Q34_Q3 = np.percentile(medicine_3["Q3/Q4 % Change"], 75)
medicine_Q34_max = medicine_Q34_Q1 + (medicine_Q34_Q3 - medicine_Q34_Q1) * 1.5
medicine_Q34_min = medicine_Q34_Q1 - (medicine_Q34_Q3 - medicine_Q34_Q1) * 1.5

medicine_Q41_Q1 = np.percentile(medicine_3["Q4/Q1 % Change"], 25)
medicine_Q41_Q3 = np.percentile(medicine_3["Q4/Q1 % Change"], 75)
medicine_Q41_max = medicine_Q41_Q1 + (medicine_Q41_Q3 - medicine_Q41_Q1) * 1.5 
medicine_Q41_min = medicine_Q41_Q1 - (medicine_Q41_Q3 - medicine_Q41_Q1) * 1.5

medicine_Q12_Q1 = np.percentile(medicine_3["Q1/Q2 % Change"], 25)
medicine_Q12_Q3 = np.percentile(medicine_3["Q1/Q2 % Change"], 75)
medicine_Q12_max = medicine_Q12_Q1 + (medicine_Q12_Q3 - medicine_Q12_Q1) * 1.5 
medicine_Q12_min = medicine_Q12_Q1 - (medicine_Q12_Q3 - medicine_Q12_Q1) * 1.5


# In[15]:


# body_care

body_care_3["Q34_max"] = body_care_Q34_max
body_care_3["Q41_max"] = body_care_Q41_max
body_care_3["Q12_max"] = body_care_Q12_max

body_care_3["Q34_min"] = body_care_Q34_min
body_care_3["Q41_min"] = body_care_Q41_min
body_care_3["Q12_min"] = body_care_Q12_min


# produce

produce_3["Q34_max"] = produce_Q34_max
produce_3["Q41_max"] = produce_Q41_max
produce_3["Q12_max"] = produce_Q12_max

produce_3["Q34_min"] = produce_Q34_min
produce_3["Q41_min"] = produce_Q41_min
produce_3["Q12_min"] = produce_Q12_min

# pet

pet_3["Q34_max"] = pet_Q34_max
pet_3["Q41_max"] = pet_Q41_max
pet_3["Q12_max"] = pet_Q12_max

pet_3["Q34_min"] = pet_Q34_min
pet_3["Q41_min"] = pet_Q41_min
pet_3["Q12_min"] = pet_Q12_min


# other

other_3["Q34_max"] = other_Q34_max
other_3["Q41_max"] = other_Q41_max
other_3["Q12_max"] = other_Q12_max

other_3["Q34_min"] = other_Q34_min
other_3["Q41_min"] = other_Q41_min
other_3["Q12_min"] = other_Q12_min

# refrigerate

refrigerate_3["Q34_max"] = refrigerate_Q34_max
refrigerate_3["Q41_max"] = refrigerate_Q41_max
refrigerate_3["Q12_max"] = refrigerate_Q12_max

refrigerate_3["Q34_min"] = refrigerate_Q34_min
refrigerate_3["Q41_min"] = refrigerate_Q41_min
refrigerate_3["Q12_min"] = refrigerate_Q12_min

# grocery

grocery_3["Q34_max"] = grocery_Q34_max
grocery_3["Q41_max"] = grocery_Q41_max
grocery_3["Q12_max"] = grocery_Q12_max

grocery_3["Q34_min"] = grocery_Q34_min
grocery_3["Q41_min"] = grocery_Q41_min
grocery_3["Q12_min"] = grocery_Q12_min

# vitamax

vitamin_3["Q34_max"] = vitamin_Q34_max
vitamin_3["Q41_max"] = vitamin_Q41_max
vitamin_3["Q12_max"] = vitamin_Q12_max

vitamin_3["Q34_min"] = vitamin_Q34_min
vitamin_3["Q41_min"] = vitamin_Q41_min
vitamin_3["Q12_min"] = vitamin_Q12_min


# general_merchandise

general_merchandise_3["Q34_max"] = general_merchandise_Q34_max
general_merchandise_3["Q41_max"] = general_merchandise_Q41_max
general_merchandise_3["Q12_max"] = general_merchandise_Q12_max

general_merchandise_3["Q34_min"] = general_merchandise_Q34_min
general_merchandise_3["Q41_min"] = general_merchandise_Q41_min
general_merchandise_3["Q12_min"] = general_merchandise_Q12_min


# frozen

frozen_3["Q34_max"] = frozen_Q34_max
frozen_3["Q41_max"] = frozen_Q41_max
frozen_3["Q12_max"] = frozen_Q12_max

frozen_3["Q34_min"] = frozen_Q34_min
frozen_3["Q41_min"] = frozen_Q41_min
frozen_3["Q12_min"] = frozen_Q12_min

# medicine

medicine_3["Q34_max"] = medicine_Q34_max
medicine_3["Q41_max"] = medicine_Q41_max
medicine_3["Q12_max"] = medicine_Q12_max

medicine_3["Q34_min"] = medicine_Q34_min
medicine_3["Q41_min"] = medicine_Q41_min
medicine_3["Q12_min"] = medicine_Q12_min


# alcohol

alcohol_3["Q34_max"] = alcohol_Q34_max
alcohol_3["Q41_max"] = alcohol_Q41_max
alcohol_3["Q12_max"] = alcohol_Q12_max

alcohol_3["Q34_min"] = alcohol_Q34_min
alcohol_3["Q41_min"] = alcohol_Q41_min
alcohol_3["Q12_min"] = alcohol_Q12_min


# In[19]:


# body_care

body_care_3.loc[body_care_3['Q3/Q4 % Change'] < body_care_3['Q34_max'], "Q34 PASS Y/N MAX"] = "Y"
body_care_3.loc[body_care_3['Q3/Q4 % Change'] >= body_care_3['Q34_max'], "Q34 PASS Y/N MAX"] = "N"
body_care_3.loc[body_care_3['Q4/Q1 % Change'] < body_care_3['Q41_max'], "Q41 PASS Y/N MAX"] = "Y"
body_care_3.loc[body_care_3['Q4/Q1 % Change'] >= body_care_3['Q41_max'], "Q41 PASS Y/N MAX"] = "N"
body_care_3.loc[body_care_3['Q1/Q2 % Change'] < body_care_3['Q12_max'], "Q12 PASS Y/N MAX"] = "Y"
body_care_3.loc[body_care_3['Q1/Q2 % Change'] >= body_care_3['Q12_max'], "Q12 PASS Y/N MAX"] = "N"

body_care_3.loc[body_care_3['Q3/Q4 % Change'] > body_care_3['Q34_min'], "Q34 PASS Y/N MIN"] = "Y"
body_care_3.loc[body_care_3['Q3/Q4 % Change'] <= body_care_3['Q34_min'], "Q34 PASS Y/N MIN"] = "N"
body_care_3.loc[body_care_3['Q4/Q1 % Change'] > body_care_3['Q41_min'], "Q41 PASS Y/N MIN"] = "Y"
body_care_3.loc[body_care_3['Q4/Q1 % Change'] <= body_care_3['Q41_min'], "Q41 PASS Y/N MIN"] = "N"
body_care_3.loc[body_care_3['Q1/Q2 % Change'] > body_care_3['Q12_min'], "Q12 PASS Y/N MIN"] = "Y"
body_care_3.loc[body_care_3['Q1/Q2 % Change'] <= body_care_3['Q12_min'], "Q12 PASS Y/N MIN"] = "N"

body_care_3.loc[body_care_3['Q3/Q4 % Change'] == 1 , "Q34 Newly List"] = "Y"
body_care_3.loc[body_care_3['Q3/Q4 % Change'] != 1 , "Q34 Newly List"] = "N"
body_care_3.loc[body_care_3['Q4/Q1 % Change'] == 1 , "Q41 Newly List"] = "Y"
body_care_3.loc[body_care_3['Q4/Q1 % Change'] != 1 , "Q41 Newly List"] = "N"
body_care_3.loc[body_care_3['Q1/Q2 % Change'] == 1, "Q12 Newly List"] = "Y"
body_care_3.loc[body_care_3['Q1/Q2 % Change'] != 1, "Q12 Newly List"] = "N"



def outlier_body_care(body_care_3) :
    if (body_care_3['Q34 PASS Y/N MAX'] == "N") or (body_care_3['Q34 PASS Y/N MIN'] == "N") or (body_care_3['Q34 Newly List'] == "Y"):
        return "Y"
    
    elif (body_care_3['Q41 PASS Y/N MAX'] == "N") or (body_care_3['Q41 PASS Y/N MIN'] == "N") or (body_care_3['Q41 Newly List'] == "Y"):
        return "Y"
    
    elif (body_care_3['Q12 PASS Y/N MAX'] == "N") or (body_care_3['Q12 PASS Y/N MIN'] == "N") or (body_care_3['Q12 Newly List'] == "Y"):
        return "Y"
    
    else :
        return "N"
    
body_care_3["Outlier Y/N"] = body_care_3.apply(outlier_body_care, axis = 1)

# produce

produce_3.loc[produce_3['Q3/Q4 % Change'] < produce_3['Q34_max'], "Q34 PASS Y/N MAX"] = "Y"
produce_3.loc[produce_3['Q3/Q4 % Change'] >= produce_3['Q34_max'], "Q34 PASS Y/N MAX"] = "N"
produce_3.loc[produce_3['Q4/Q1 % Change'] < produce_3['Q41_max'], "Q41 PASS Y/N MAX"] = "Y"
produce_3.loc[produce_3['Q4/Q1 % Change'] >= produce_3['Q41_max'], "Q41 PASS Y/N MAX"] = "N"
produce_3.loc[produce_3['Q1/Q2 % Change'] < produce_3['Q12_max'], "Q12 PASS Y/N MAX"] = "Y"
produce_3.loc[produce_3['Q1/Q2 % Change'] >= produce_3['Q12_max'], "Q12 PASS Y/N MAX"] = "N"

produce_3.loc[produce_3['Q3/Q4 % Change'] > produce_3['Q34_min'], "Q34 PASS Y/N MIN"] = "Y"
produce_3.loc[produce_3['Q3/Q4 % Change'] <= produce_3['Q34_min'], "Q34 PASS Y/N MIN"] = "N"
produce_3.loc[produce_3['Q4/Q1 % Change'] > produce_3['Q41_min'], "Q41 PASS Y/N MIN"] = "Y"
produce_3.loc[produce_3['Q4/Q1 % Change'] <= produce_3['Q41_min'], "Q41 PASS Y/N MIN"] = "N"
produce_3.loc[produce_3['Q1/Q2 % Change'] > produce_3['Q12_min'], "Q12 PASS Y/N MIN"] = "Y"
produce_3.loc[produce_3['Q1/Q2 % Change'] <= produce_3['Q12_min'], "Q12 PASS Y/N MIN"] = "N"


def newly_list(produce_3) :
    if (produce_3['Q3/Q4 % Change'] == 1) and (produce_3['Q4/Q1 % Change'] == 0)     and (produce_3['Q1/Q2 % Change'] == 0) :
        return "Y"
    elif (produce_3['Q3/Q4 % Change'] == 0) and (produce_3['Q4/Q1 % Change'] == 1)     and (produce_3['Q1/Q2 % Change'] == 0) :
        return "Y"
    elif (produce_3['Q3/Q4 % Change'] == 0) and (produce_3['Q4/Q1 % Change'] == 0)     and (produce_3['Q1/Q2 % Change'] == 1) :
        return "Y"
    else :
        return "N"

produce_3["Newly List"] = produce_3.apply(newly_list, axis = 1)


def outlier_produce(produce_3) :
    
    if (produce_3['Q34 PASS Y/N MAX'] == "N") or (produce_3['Q34 PASS Y/N MIN'] == "N") :
        return "Y"
    
    elif (produce_3['Q41 PASS Y/N MAX'] == "N") or (produce_3['Q41 PASS Y/N MIN'] == "N") :
        return "Y"
    
    elif (produce_3['Q12 PASS Y/N MAX'] == "N") or (produce_3['Q12 PASS Y/N MIN'] == "N") :
        return "Y"
    
    else :
        return "N"
    
produce_3["Outlier Y/N"] = produce_3.apply(outlier_produce, axis = 1)

def outlier_produce_1(produce_3) :
    
    if (produce_3['Newly List'] == "Y") and (produce_3["Outlier Y/N"] == "Y") :
        return "N"
    
    elif (produce_3['Newly List'] == "Y") and (produce_3["Outlier Y/N"] == "Y") :
        return "N"
    
    elif (produce_3['Newly List'] == "Y") and (produce_3["Outlier Y/N"] == "Y") :
        return "N"
    
    else :
        return produce_3["Outlier Y/N"]

produce_3["Outlier Y/N_1"] = produce_3.apply(outlier_produce_1, axis = 1)



# pet

pet_3.loc[pet_3['Q3/Q4 % Change'] < pet_3['Q34_max'], "Q34 PASS Y/N MAX"] = "Y"
pet_3.loc[pet_3['Q3/Q4 % Change'] >= pet_3['Q34_max'], "Q34 PASS Y/N MAX"] = "N"
pet_3.loc[pet_3['Q4/Q1 % Change'] < pet_3['Q41_max'], "Q41 PASS Y/N MAX"] = "Y"
pet_3.loc[pet_3['Q4/Q1 % Change'] >= pet_3['Q41_max'], "Q41 PASS Y/N MAX"] = "N"
pet_3.loc[pet_3['Q1/Q2 % Change'] < pet_3['Q12_max'], "Q12 PASS Y/N MAX"] = "Y"
pet_3.loc[pet_3['Q1/Q2 % Change'] >= pet_3['Q12_max'], "Q12 PASS Y/N MAX"] = "N"

pet_3.loc[pet_3['Q3/Q4 % Change'] > pet_3['Q34_min'], "Q34 PASS Y/N MIN"] = "Y"
pet_3.loc[pet_3['Q3/Q4 % Change'] <= pet_3['Q34_min'], "Q34 PASS Y/N MIN"] = "N"
pet_3.loc[pet_3['Q4/Q1 % Change'] > pet_3['Q41_min'], "Q41 PASS Y/N MIN"] = "Y"
pet_3.loc[pet_3['Q4/Q1 % Change'] <= pet_3['Q41_min'], "Q41 PASS Y/N MIN"] = "N"
pet_3.loc[pet_3['Q1/Q2 % Change'] > pet_3['Q12_min'], "Q12 PASS Y/N MIN"] = "Y"
pet_3.loc[pet_3['Q1/Q2 % Change'] <= pet_3['Q12_min'], "Q12 PASS Y/N MIN"] = "N"

pet_3.loc[pet_3['Q3/Q4 % Change'] == 1 , "Q34 Newly List"] = "Y"
pet_3.loc[pet_3['Q3/Q4 % Change'] != 1 , "Q34 Newly List"] = "N"
pet_3.loc[pet_3['Q4/Q1 % Change'] == 1 , "Q41 Newly List"] = "Y"
pet_3.loc[pet_3['Q4/Q1 % Change'] != 1 , "Q41 Newly List"] = "N"
pet_3.loc[pet_3['Q1/Q2 % Change'] == 1, "Q12 Newly List"] = "Y"
pet_3.loc[pet_3['Q1/Q2 % Change'] != 1, "Q12 Newly List"] = "N"



def outlier_pet(pet_3) :
    if (pet_3['Q34 PASS Y/N MAX'] == "N") or (pet_3['Q34 PASS Y/N MIN'] == "N") or (pet_3['Q34 Newly List'] == "Y"):
        return "Y"
    
    elif (pet_3['Q41 PASS Y/N MAX'] == "N") or (pet_3['Q41 PASS Y/N MIN'] == "N") or (pet_3['Q41 Newly List'] == "Y"):
        return "Y"
    
    elif (pet_3['Q12 PASS Y/N MAX'] == "N") or (pet_3['Q12 PASS Y/N MIN'] == "N") or (pet_3['Q12 Newly List'] == "Y"):
        return "Y"
    
    else :
        return "N"
    
pet_3["Outlier Y/N"] = pet_3.apply(outlier_pet, axis = 1)



# other

other_3.loc[other_3['Q3/Q4 % Change'] < other_3['Q34_max'], "Q34 PASS Y/N MAX"] = "Y"
other_3.loc[other_3['Q3/Q4 % Change'] >= other_3['Q34_max'], "Q34 PASS Y/N MAX"] = "N"
other_3.loc[other_3['Q4/Q1 % Change'] < other_3['Q41_max'], "Q41 PASS Y/N MAX"] = "Y"
other_3.loc[other_3['Q4/Q1 % Change'] >= other_3['Q41_max'], "Q41 PASS Y/N MAX"] = "N"
other_3.loc[other_3['Q1/Q2 % Change'] < other_3['Q12_max'], "Q12 PASS Y/N MAX"] = "Y"
other_3.loc[other_3['Q1/Q2 % Change'] >= other_3['Q12_max'], "Q12 PASS Y/N MAX"] = "N"

other_3.loc[other_3['Q3/Q4 % Change'] > other_3['Q34_min'], "Q34 PASS Y/N MIN"] = "Y"
other_3.loc[other_3['Q3/Q4 % Change'] <= other_3['Q34_min'], "Q34 PASS Y/N MIN"] = "N"
other_3.loc[other_3['Q4/Q1 % Change'] > other_3['Q41_min'], "Q41 PASS Y/N MIN"] = "Y"
other_3.loc[other_3['Q4/Q1 % Change'] <= other_3['Q41_min'], "Q41 PASS Y/N MIN"] = "N"
other_3.loc[other_3['Q1/Q2 % Change'] > other_3['Q12_min'], "Q12 PASS Y/N MIN"] = "Y"
other_3.loc[other_3['Q1/Q2 % Change'] <= other_3['Q12_min'], "Q12 PASS Y/N MIN"] = "N"


def newly_list(other_3) :
    if (other_3['Q3/Q4 % Change'] == 1) and (other_3['Q4/Q1 % Change'] == 0)     and (other_3['Q1/Q2 % Change'] == 0) :
        return "Y"
    elif (other_3['Q3/Q4 % Change'] == 0) and (other_3['Q4/Q1 % Change'] == 1)     and (other_3['Q1/Q2 % Change'] == 0) :
        return "Y"
    elif (other_3['Q3/Q4 % Change'] == 0) and (other_3['Q4/Q1 % Change'] == 0)     and (other_3['Q1/Q2 % Change'] == 1) :
        return "Y"
    else :
        return "N"

other_3["Newly List"] = other_3.apply(newly_list, axis = 1)


def outlier_other(other_3) :
    
    if (other_3['Q34 PASS Y/N MAX'] == "N") or (other_3['Q34 PASS Y/N MIN'] == "N") :
        return "Y"
    
    elif (other_3['Q41 PASS Y/N MAX'] == "N") or (other_3['Q41 PASS Y/N MIN'] == "N") :
        return "Y"
    
    elif (other_3['Q12 PASS Y/N MAX'] == "N") or (other_3['Q12 PASS Y/N MIN'] == "N") :
        return "Y"
    
    else :
        return "N"
    
other_3["Outlier Y/N"] = other_3.apply(outlier_other, axis = 1)

def outlier_other_1(other_3) :
    
    if (other_3['Newly List'] == "Y") and (other_3["Outlier Y/N"] == "Y") :
        return "N"
    
    elif (other_3['Newly List'] == "Y") and (other_3["Outlier Y/N"] == "Y") :
        return "N"
    
    elif (other_3['Newly List'] == "Y") and (other_3["Outlier Y/N"] == "Y") :
        return "N"
    
    else :
        return other_3["Outlier Y/N"]

other_3["Outlier Y/N_1"] = other_3.apply(outlier_other_1, axis = 1)


# refrigerate

refrigerate_3.loc[refrigerate_3['Q3/Q4 % Change'] < refrigerate_3['Q34_max'], "Q34 PASS Y/N MAX"] = "Y"
refrigerate_3.loc[refrigerate_3['Q3/Q4 % Change'] >= refrigerate_3['Q34_max'], "Q34 PASS Y/N MAX"] = "N"
refrigerate_3.loc[refrigerate_3['Q4/Q1 % Change'] < refrigerate_3['Q41_max'], "Q41 PASS Y/N MAX"] = "Y"
refrigerate_3.loc[refrigerate_3['Q4/Q1 % Change'] >= refrigerate_3['Q41_max'], "Q41 PASS Y/N MAX"] = "N"
refrigerate_3.loc[refrigerate_3['Q1/Q2 % Change'] < refrigerate_3['Q12_max'], "Q12 PASS Y/N MAX"] = "Y"
refrigerate_3.loc[refrigerate_3['Q1/Q2 % Change'] >= refrigerate_3['Q12_max'], "Q12 PASS Y/N MAX"] = "N"

refrigerate_3.loc[refrigerate_3['Q3/Q4 % Change'] > refrigerate_3['Q34_min'], "Q34 PASS Y/N MIN"] = "Y"
refrigerate_3.loc[refrigerate_3['Q3/Q4 % Change'] <= refrigerate_3['Q34_min'], "Q34 PASS Y/N MIN"] = "N"
refrigerate_3.loc[refrigerate_3['Q4/Q1 % Change'] > refrigerate_3['Q41_min'], "Q41 PASS Y/N MIN"] = "Y"
refrigerate_3.loc[refrigerate_3['Q4/Q1 % Change'] <= refrigerate_3['Q41_min'], "Q41 PASS Y/N MIN"] = "N"
refrigerate_3.loc[refrigerate_3['Q1/Q2 % Change'] > refrigerate_3['Q12_min'], "Q12 PASS Y/N MIN"] = "Y"
refrigerate_3.loc[refrigerate_3['Q1/Q2 % Change'] <= refrigerate_3['Q12_min'], "Q12 PASS Y/N MIN"] = "N"

refrigerate_3.loc[refrigerate_3['Q3/Q4 % Change'] == 1 , "Q34 Newly List"] = "Y"
refrigerate_3.loc[refrigerate_3['Q3/Q4 % Change'] != 1 , "Q34 Newly List"] = "N"
refrigerate_3.loc[refrigerate_3['Q4/Q1 % Change'] == 1 , "Q41 Newly List"] = "Y"
refrigerate_3.loc[refrigerate_3['Q4/Q1 % Change'] != 1 , "Q41 Newly List"] = "N"
refrigerate_3.loc[refrigerate_3['Q1/Q2 % Change'] == 1, "Q12 Newly List"] = "Y"
refrigerate_3.loc[refrigerate_3['Q1/Q2 % Change'] != 1, "Q12 Newly List"] = "N"



def outlier_refrigerate(refrigerate_3) :
    if (refrigerate_3['Q34 PASS Y/N MAX'] == "N") or (refrigerate_3['Q34 PASS Y/N MIN'] == "N") or (refrigerate_3['Q34 Newly List'] == "Y"):
        return "Y"
    
    elif (refrigerate_3['Q41 PASS Y/N MAX'] == "N") or (refrigerate_3['Q41 PASS Y/N MIN'] == "N") or (refrigerate_3['Q41 Newly List'] == "Y"):
        return "Y"
    
    elif (refrigerate_3['Q12 PASS Y/N MAX'] == "N") or (refrigerate_3['Q12 PASS Y/N MIN'] == "N") or (refrigerate_3['Q12 Newly List'] == "Y"):
        return "Y"
    
    else :
        return "N"
    
refrigerate_3["Outlier Y/N"] = refrigerate_3.apply(outlier_refrigerate, axis = 1)

# grocery

grocery_3.loc[grocery_3['Q3/Q4 % Change'] < grocery_3['Q34_max'], "Q34 PASS Y/N MAX"] = "Y"
grocery_3.loc[grocery_3['Q3/Q4 % Change'] >= grocery_3['Q34_max'], "Q34 PASS Y/N MAX"] = "N"
grocery_3.loc[grocery_3['Q4/Q1 % Change'] < grocery_3['Q41_max'], "Q41 PASS Y/N MAX"] = "Y"
grocery_3.loc[grocery_3['Q4/Q1 % Change'] >= grocery_3['Q41_max'], "Q41 PASS Y/N MAX"] = "N"
grocery_3.loc[grocery_3['Q1/Q2 % Change'] < grocery_3['Q12_max'], "Q12 PASS Y/N MAX"] = "Y"
grocery_3.loc[grocery_3['Q1/Q2 % Change'] >= grocery_3['Q12_max'], "Q12 PASS Y/N MAX"] = "N"

grocery_3.loc[grocery_3['Q3/Q4 % Change'] > grocery_3['Q34_min'], "Q34 PASS Y/N MIN"] = "Y"
grocery_3.loc[grocery_3['Q3/Q4 % Change'] <= grocery_3['Q34_min'], "Q34 PASS Y/N MIN"] = "N"
grocery_3.loc[grocery_3['Q4/Q1 % Change'] > grocery_3['Q41_min'], "Q41 PASS Y/N MIN"] = "Y"
grocery_3.loc[grocery_3['Q4/Q1 % Change'] <= grocery_3['Q41_min'], "Q41 PASS Y/N MIN"] = "N"
grocery_3.loc[grocery_3['Q1/Q2 % Change'] > grocery_3['Q12_min'], "Q12 PASS Y/N MIN"] = "Y"
grocery_3.loc[grocery_3['Q1/Q2 % Change'] <= grocery_3['Q12_min'], "Q12 PASS Y/N MIN"] = "N"


def newly_list(grocery_3) :
    if (grocery_3['Q3/Q4 % Change'] == 1) and (grocery_3['Q4/Q1 % Change'] == 0)     and (grocery_3['Q1/Q2 % Change'] == 0) :
        return "Y"
    elif (grocery_3['Q3/Q4 % Change'] == 0) and (grocery_3['Q4/Q1 % Change'] == 1)     and (grocery_3['Q1/Q2 % Change'] == 0) :
        return "Y"
    elif (grocery_3['Q3/Q4 % Change'] == 0) and (grocery_3['Q4/Q1 % Change'] == 0)     and (grocery_3['Q1/Q2 % Change'] == 1) :
        return "Y"
    else :
        return "N"

grocery_3["Newly List"] = grocery_3.apply(newly_list, axis = 1)


def outlier_grocery(grocery_3) :
    
    if (grocery_3['Q34 PASS Y/N MAX'] == "N") or (grocery_3['Q34 PASS Y/N MIN'] == "N") :
        return "Y"
    
    elif (grocery_3['Q41 PASS Y/N MAX'] == "N") or (grocery_3['Q41 PASS Y/N MIN'] == "N") :
        return "Y"
    
    elif (grocery_3['Q12 PASS Y/N MAX'] == "N") or (grocery_3['Q12 PASS Y/N MIN'] == "N") :
        return "Y"
    
    else :
        return "N"
    
grocery_3["Outlier Y/N"] = grocery_3.apply(outlier_grocery, axis = 1)

def outlier_grocery_1(grocery_3) :
    
    if (grocery_3['Newly List'] == "Y") and (grocery_3["Outlier Y/N"] == "Y") :
        return "N"
    
    elif (grocery_3['Newly List'] == "Y") and (grocery_3["Outlier Y/N"] == "Y") :
        return "N"
    
    elif (grocery_3['Newly List'] == "Y") and (grocery_3["Outlier Y/N"] == "Y") :
        return "N"
    
    else :
        return grocery_3["Outlier Y/N"]

grocery_3["Outlier Y/N_1"] = grocery_3.apply(outlier_grocery_1, axis = 1)
    
    
# vitamin

vitamin_3.loc[vitamin_3['Q3/Q4 % Change'] < vitamin_3['Q34_max'], "Q34 PASS Y/N MAX"] = "Y"
vitamin_3.loc[vitamin_3['Q3/Q4 % Change'] >= vitamin_3['Q34_max'], "Q34 PASS Y/N MAX"] = "N"
vitamin_3.loc[vitamin_3['Q4/Q1 % Change'] < vitamin_3['Q41_max'], "Q41 PASS Y/N MAX"] = "Y"
vitamin_3.loc[vitamin_3['Q4/Q1 % Change'] >= vitamin_3['Q41_max'], "Q41 PASS Y/N MAX"] = "N"
vitamin_3.loc[vitamin_3['Q1/Q2 % Change'] < vitamin_3['Q12_max'], "Q12 PASS Y/N MAX"] = "Y"
vitamin_3.loc[vitamin_3['Q1/Q2 % Change'] >= vitamin_3['Q12_max'], "Q12 PASS Y/N MAX"] = "N"

vitamin_3.loc[vitamin_3['Q3/Q4 % Change'] > vitamin_3['Q34_min'], "Q34 PASS Y/N MIN"] = "Y"
vitamin_3.loc[vitamin_3['Q3/Q4 % Change'] <= vitamin_3['Q34_min'], "Q34 PASS Y/N MIN"] = "N"
vitamin_3.loc[vitamin_3['Q4/Q1 % Change'] > vitamin_3['Q41_min'], "Q41 PASS Y/N MIN"] = "Y"
vitamin_3.loc[vitamin_3['Q4/Q1 % Change'] <= vitamin_3['Q41_min'], "Q41 PASS Y/N MIN"] = "N"
vitamin_3.loc[vitamin_3['Q1/Q2 % Change'] > vitamin_3['Q12_min'], "Q12 PASS Y/N MIN"] = "Y"
vitamin_3.loc[vitamin_3['Q1/Q2 % Change'] <= vitamin_3['Q12_min'], "Q12 PASS Y/N MIN"] = "N"

vitamin_3.loc[vitamin_3['Q3/Q4 % Change'] == 1 , "Q34 Newly List"] = "Y"
vitamin_3.loc[vitamin_3['Q3/Q4 % Change'] != 1 , "Q34 Newly List"] = "N"
vitamin_3.loc[vitamin_3['Q4/Q1 % Change'] == 1 , "Q41 Newly List"] = "Y"
vitamin_3.loc[vitamin_3['Q4/Q1 % Change'] != 1 , "Q41 Newly List"] = "N"
vitamin_3.loc[vitamin_3['Q1/Q2 % Change'] == 1, "Q12 Newly List"] = "Y"
vitamin_3.loc[vitamin_3['Q1/Q2 % Change'] != 1, "Q12 Newly List"] = "N"



def outlier_vitamin(vitamin_3) :
    if (vitamin_3['Q34 PASS Y/N MAX'] == "N") or (vitamin_3['Q34 PASS Y/N MIN'] == "N") or (vitamin_3['Q34 Newly List'] == "Y"):
        return "Y"
    
    elif (vitamin_3['Q41 PASS Y/N MAX'] == "N") or (vitamin_3['Q41 PASS Y/N MIN'] == "N") or (vitamin_3['Q41 Newly List'] == "Y"):
        return "Y"
    
    elif (vitamin_3['Q12 PASS Y/N MAX'] == "N") or (vitamin_3['Q12 PASS Y/N MIN'] == "N") or (vitamin_3['Q12 Newly List'] == "Y"):
        return "Y"
    
    else :
        return "N"
    
vitamin_3["Outlier Y/N"] = vitamin_3.apply(outlier_vitamin, axis = 1)

# general_merchandise

general_merchandise_3.loc[general_merchandise_3['Q3/Q4 % Change'] < general_merchandise_3['Q34_max'], "Q34 PASS Y/N MAX"] = "Y"
general_merchandise_3.loc[general_merchandise_3['Q3/Q4 % Change'] >= general_merchandise_3['Q34_max'], "Q34 PASS Y/N MAX"] = "N"
general_merchandise_3.loc[general_merchandise_3['Q4/Q1 % Change'] < general_merchandise_3['Q41_max'], "Q41 PASS Y/N MAX"] = "Y"
general_merchandise_3.loc[general_merchandise_3['Q4/Q1 % Change'] >= general_merchandise_3['Q41_max'], "Q41 PASS Y/N MAX"] = "N"
general_merchandise_3.loc[general_merchandise_3['Q1/Q2 % Change'] < general_merchandise_3['Q12_max'], "Q12 PASS Y/N MAX"] = "Y"
general_merchandise_3.loc[general_merchandise_3['Q1/Q2 % Change'] >= general_merchandise_3['Q12_max'], "Q12 PASS Y/N MAX"] = "N"

general_merchandise_3.loc[general_merchandise_3['Q3/Q4 % Change'] > general_merchandise_3['Q34_min'], "Q34 PASS Y/N MIN"] = "Y"
general_merchandise_3.loc[general_merchandise_3['Q3/Q4 % Change'] <= general_merchandise_3['Q34_min'], "Q34 PASS Y/N MIN"] = "N"
general_merchandise_3.loc[general_merchandise_3['Q4/Q1 % Change'] > general_merchandise_3['Q41_min'], "Q41 PASS Y/N MIN"] = "Y"
general_merchandise_3.loc[general_merchandise_3['Q4/Q1 % Change'] <= general_merchandise_3['Q41_min'], "Q41 PASS Y/N MIN"] = "N"
general_merchandise_3.loc[general_merchandise_3['Q1/Q2 % Change'] > general_merchandise_3['Q12_min'], "Q12 PASS Y/N MIN"] = "Y"
general_merchandise_3.loc[general_merchandise_3['Q1/Q2 % Change'] <= general_merchandise_3['Q12_min'], "Q12 PASS Y/N MIN"] = "N"

general_merchandise_3.loc[general_merchandise_3['Q3/Q4 % Change'] == 1 , "Q34 Newly List"] = "Y"
general_merchandise_3.loc[general_merchandise_3['Q3/Q4 % Change'] != 1 , "Q34 Newly List"] = "N"
general_merchandise_3.loc[general_merchandise_3['Q4/Q1 % Change'] == 1 , "Q41 Newly List"] = "Y"
general_merchandise_3.loc[general_merchandise_3['Q4/Q1 % Change'] != 1 , "Q41 Newly List"] = "N"
general_merchandise_3.loc[general_merchandise_3['Q1/Q2 % Change'] == 1, "Q12 Newly List"] = "Y"
general_merchandise_3.loc[general_merchandise_3['Q1/Q2 % Change'] != 1, "Q12 Newly List"] = "N"



def outlier_general_merchandise(general_merchandise_3) :
    if (general_merchandise_3['Q34 PASS Y/N MAX'] == "N") or (general_merchandise_3['Q34 PASS Y/N MIN'] == "N") or (general_merchandise_3['Q34 Newly List'] == "Y"):
        return "Y"
    
    elif (general_merchandise_3['Q41 PASS Y/N MAX'] == "N") or (general_merchandise_3['Q41 PASS Y/N MIN'] == "N") or (general_merchandise_3['Q41 Newly List'] == "Y"):
        return "Y"
    
    elif (general_merchandise_3['Q12 PASS Y/N MAX'] == "N") or (general_merchandise_3['Q12 PASS Y/N MIN'] == "N") or (general_merchandise_3['Q12 Newly List'] == "Y"):
        return "Y"
    
    else :
        return "N"
    
general_merchandise_3["Outlier Y/N"] = general_merchandise_3.apply(outlier_general_merchandise, axis = 1)

# medicine

medicine_3.loc[medicine_3['Q3/Q4 % Change'] < medicine_3['Q34_max'], "Q34 PASS Y/N MAX"] = "Y"
medicine_3.loc[medicine_3['Q3/Q4 % Change'] >= medicine_3['Q34_max'], "Q34 PASS Y/N MAX"] = "N"
medicine_3.loc[medicine_3['Q4/Q1 % Change'] < medicine_3['Q41_max'], "Q41 PASS Y/N MAX"] = "Y"
medicine_3.loc[medicine_3['Q4/Q1 % Change'] >= medicine_3['Q41_max'], "Q41 PASS Y/N MAX"] = "N"
medicine_3.loc[medicine_3['Q1/Q2 % Change'] < medicine_3['Q12_max'], "Q12 PASS Y/N MAX"] = "Y"
medicine_3.loc[medicine_3['Q1/Q2 % Change'] >= medicine_3['Q12_max'], "Q12 PASS Y/N MAX"] = "N"

medicine_3.loc[medicine_3['Q3/Q4 % Change'] > medicine_3['Q34_min'], "Q34 PASS Y/N MIN"] = "Y"
medicine_3.loc[medicine_3['Q3/Q4 % Change'] <= medicine_3['Q34_min'], "Q34 PASS Y/N MIN"] = "N"
medicine_3.loc[medicine_3['Q4/Q1 % Change'] > medicine_3['Q41_min'], "Q41 PASS Y/N MIN"] = "Y"
medicine_3.loc[medicine_3['Q4/Q1 % Change'] <= medicine_3['Q41_min'], "Q41 PASS Y/N MIN"] = "N"
medicine_3.loc[medicine_3['Q1/Q2 % Change'] > medicine_3['Q12_min'], "Q12 PASS Y/N MIN"] = "Y"
medicine_3.loc[medicine_3['Q1/Q2 % Change'] <= medicine_3['Q12_min'], "Q12 PASS Y/N MIN"] = "N"

medicine_3.loc[medicine_3['Q3/Q4 % Change'] == 1 , "Q34 Newly List"] = "Y"
medicine_3.loc[medicine_3['Q3/Q4 % Change'] != 1 , "Q34 Newly List"] = "N"
medicine_3.loc[medicine_3['Q4/Q1 % Change'] == 1 , "Q41 Newly List"] = "Y"
medicine_3.loc[medicine_3['Q4/Q1 % Change'] != 1 , "Q41 Newly List"] = "N"
medicine_3.loc[medicine_3['Q1/Q2 % Change'] == 1, "Q12 Newly List"] = "Y"
medicine_3.loc[medicine_3['Q1/Q2 % Change'] != 1, "Q12 Newly List"] = "N"



def outlier_medicine(medicine_3) :
    if (medicine_3['Q34 PASS Y/N MAX'] == "N") or (medicine_3['Q34 PASS Y/N MIN'] == "N") or (medicine_3['Q34 Newly List'] == "Y"):
        return "Y"
    
    elif (medicine_3['Q41 PASS Y/N MAX'] == "N") or (medicine_3['Q41 PASS Y/N MIN'] == "N") or (medicine_3['Q41 Newly List'] == "Y"):
        return "Y"
    
    elif (medicine_3['Q12 PASS Y/N MAX'] == "N") or (medicine_3['Q12 PASS Y/N MIN'] == "N") or (medicine_3['Q12 Newly List'] == "Y"):
        return "Y"
    
    else :
        return "N"
    
medicine_3["Outlier Y/N"] = medicine_3.apply(outlier_medicine, axis = 1)

## frozen

frozen_3.loc[frozen_3['Q3/Q4 % Change'] < frozen_3['Q34_max'], "Q34 PASS Y/N MAX"] = "Y"
frozen_3.loc[frozen_3['Q3/Q4 % Change'] >= frozen_3['Q34_max'], "Q34 PASS Y/N MAX"] = "N"
frozen_3.loc[frozen_3['Q4/Q1 % Change'] < frozen_3['Q41_max'], "Q41 PASS Y/N MAX"] = "Y"
frozen_3.loc[frozen_3['Q4/Q1 % Change'] >= frozen_3['Q41_max'], "Q41 PASS Y/N MAX"] = "N"
frozen_3.loc[frozen_3['Q1/Q2 % Change'] < frozen_3['Q12_max'], "Q12 PASS Y/N MAX"] = "Y"
frozen_3.loc[frozen_3['Q1/Q2 % Change'] >= frozen_3['Q12_max'], "Q12 PASS Y/N MAX"] = "N"

frozen_3.loc[frozen_3['Q3/Q4 % Change'] > frozen_3['Q34_min'], "Q34 PASS Y/N MIN"] = "Y"
frozen_3.loc[frozen_3['Q3/Q4 % Change'] <= frozen_3['Q34_min'], "Q34 PASS Y/N MIN"] = "N"
frozen_3.loc[frozen_3['Q4/Q1 % Change'] > frozen_3['Q41_min'], "Q41 PASS Y/N MIN"] = "Y"
frozen_3.loc[frozen_3['Q4/Q1 % Change'] <= frozen_3['Q41_min'], "Q41 PASS Y/N MIN"] = "N"
frozen_3.loc[frozen_3['Q1/Q2 % Change'] > frozen_3['Q12_min'], "Q12 PASS Y/N MIN"] = "Y"
frozen_3.loc[frozen_3['Q1/Q2 % Change'] <= frozen_3['Q12_min'], "Q12 PASS Y/N MIN"] = "N"

frozen_3.loc[frozen_3['Q3/Q4 % Change'] == 1 , "Q34 Newly List"] = "Y"
frozen_3.loc[frozen_3['Q3/Q4 % Change'] != 1 , "Q34 Newly List"] = "N"
frozen_3.loc[frozen_3['Q4/Q1 % Change'] == 1 , "Q41 Newly List"] = "Y"
frozen_3.loc[frozen_3['Q4/Q1 % Change'] != 1 , "Q41 Newly List"] = "N"
frozen_3.loc[frozen_3['Q1/Q2 % Change'] == 1, "Q12 Newly List"] = "Y"
frozen_3.loc[frozen_3['Q1/Q2 % Change'] != 1, "Q12 Newly List"] = "N"



def outlier_frozen(frozen_3) :
    if (frozen_3['Q34 PASS Y/N MAX'] == "N") or (frozen_3['Q34 PASS Y/N MIN'] == "N") or (frozen_3['Q34 Newly List'] == "Y"):
        return "Y"
    
    elif (frozen_3['Q41 PASS Y/N MAX'] == "N") or (frozen_3['Q41 PASS Y/N MIN'] == "N") or (frozen_3['Q41 Newly List'] == "Y"):
        return "Y"
    
    elif (frozen_3['Q12 PASS Y/N MAX'] == "N") or (frozen_3['Q12 PASS Y/N MIN'] == "N") or (frozen_3['Q12 Newly List'] == "Y"):
        return "Y"
    
    else :
        return "N"
    
frozen_3["Outlier Y/N"] = frozen_3.apply(outlier_frozen, axis = 1)


# alcohol

alcohol_3.loc[alcohol_3['Q3/Q4 % Change'] < alcohol_3['Q34_max'], "Q34 PASS Y/N MAX"] = "Y"
alcohol_3.loc[alcohol_3['Q3/Q4 % Change'] >= alcohol_3['Q34_max'], "Q34 PASS Y/N MAX"] = "N"
alcohol_3.loc[alcohol_3['Q4/Q1 % Change'] < alcohol_3['Q41_max'], "Q41 PASS Y/N MAX"] = "Y"
alcohol_3.loc[alcohol_3['Q4/Q1 % Change'] >= alcohol_3['Q41_max'], "Q41 PASS Y/N MAX"] = "N"
alcohol_3.loc[alcohol_3['Q1/Q2 % Change'] < alcohol_3['Q12_max'], "Q12 PASS Y/N MAX"] = "Y"
alcohol_3.loc[alcohol_3['Q1/Q2 % Change'] >= alcohol_3['Q12_max'], "Q12 PASS Y/N MAX"] = "N"

alcohol_3.loc[alcohol_3['Q3/Q4 % Change'] > alcohol_3['Q34_min'], "Q34 PASS Y/N MIN"] = "Y"
alcohol_3.loc[alcohol_3['Q3/Q4 % Change'] <= alcohol_3['Q34_min'], "Q34 PASS Y/N MIN"] = "N"
alcohol_3.loc[alcohol_3['Q4/Q1 % Change'] > alcohol_3['Q41_min'], "Q41 PASS Y/N MIN"] = "Y"
alcohol_3.loc[alcohol_3['Q4/Q1 % Change'] <= alcohol_3['Q41_min'], "Q41 PASS Y/N MIN"] = "N"
alcohol_3.loc[alcohol_3['Q1/Q2 % Change'] > alcohol_3['Q12_min'], "Q12 PASS Y/N MIN"] = "Y"
alcohol_3.loc[alcohol_3['Q1/Q2 % Change'] <= alcohol_3['Q12_min'], "Q12 PASS Y/N MIN"] = "N"

alcohol_3.loc[alcohol_3['Q3/Q4 % Change'] == 1 , "Q34 Newly List"] = "Y"
alcohol_3.loc[alcohol_3['Q3/Q4 % Change'] != 1 , "Q34 Newly List"] = "N"
alcohol_3.loc[alcohol_3['Q4/Q1 % Change'] == 1 , "Q41 Newly List"] = "Y"
alcohol_3.loc[alcohol_3['Q4/Q1 % Change'] != 1 , "Q41 Newly List"] = "N"
alcohol_3.loc[alcohol_3['Q1/Q2 % Change'] == 1, "Q12 Newly List"] = "Y"
alcohol_3.loc[alcohol_3['Q1/Q2 % Change'] != 1, "Q12 Newly List"] = "N"



def outlier_alcohol(alcohol_3) :
    if (alcohol_3['Q34 PASS Y/N MAX'] == "N") or (alcohol_3['Q34 PASS Y/N MIN'] == "N") or (alcohol_3['Q34 Newly List'] == "Y"):
        return "Y"
    
    elif (alcohol_3['Q41 PASS Y/N MAX'] == "N") or (alcohol_3['Q41 PASS Y/N MIN'] == "N") or (alcohol_3['Q41 Newly List'] == "Y"):
        return "Y"
    
    elif (alcohol_3['Q12 PASS Y/N MAX'] == "N") or (alcohol_3['Q12 PASS Y/N MIN'] == "N") or (alcohol_3['Q12 Newly List'] == "Y"):
        return "Y"
    
    else :
        return "N"
    
alcohol_3["Outlier Y/N"] = alcohol_3.apply(outlier_alcohol, axis = 1)


# In[20]:


# left merge file_2 by department

# body_care, produce, other, general_merchandise, vitamin, grocery, medicine, pet, refrigerate, frozen, alcohol

body_care_outlier = body_care_3[["UPC", "Outlier Y/N"]]
produce_outlier = produce_3[["UPC", "Outlier Y/N_1"]]
other_outlier = other_3[["UPC", "Outlier Y/N_1"]]
general_merchandise_outlier = general_merchandise_3[["UPC", "Outlier Y/N"]]
vitamin_outlier = vitamin_3[["UPC", "Outlier Y/N"]]
grocery_outlier = grocery_3[["UPC", "Outlier Y/N_1"]]
medicine_outlier = medicine_3[["UPC", "Outlier Y/N"]]
pet_outlier = pet_3[["UPC", "Outlier Y/N"]]
refrigerate_outlier = refrigerate_3[["UPC", "Outlier Y/N"]]
frozen_outlier = frozen_3[["UPC", "Outlier Y/N"]]
alcohol_outlier = alcohol_3[["UPC", "Outlier Y/N"]]


# In[21]:


# produce, other, general_merchandise, vitamin, grocery, medicine, pet, refrigerate, frozen, alcohol

body_care_5 = pd.merge(body_care_2, body_care_outlier[["UPC", "Outlier Y/N"]], on = "UPC", how = 'left')
body_care_5 = body_care_5.replace([np.inf, -np.inf, np.nan], 0)
body_care_5_1 = body_care_5[body_care_5["Outlier Y/N"] == "N"]

produce_5 = pd.merge(produce_2, produce_outlier[["UPC", "Outlier Y/N_1"]], on = "UPC", how = 'left')
produce_5 = produce_5.replace([np.inf, -np.inf, np.nan], 0)
produce_5_1 = produce_5[produce_5["Outlier Y/N_1"] == "N"]
produce_5_1.rename(columns = {"Outlier Y/N_1" : "Outlier Y/N"}, inplace = True)
produce_5.rename(columns = {"Outlier Y/N_1" : "Outlier Y/N"}, inplace = True)

other_5 = pd.merge(other_2, other_outlier[["UPC", "Outlier Y/N_1"]], on = "UPC", how = 'left')
other_5 = other_5.replace([np.inf, -np.inf, np.nan], 0)
other_5_1 = other_5[other_5["Outlier Y/N_1"] == "N"]
other_5_1.rename(columns = {"Outlier Y/N_1" : "Outlier Y/N"}, inplace = True)
other_5.rename(columns = {"Outlier Y/N_1" : "Outlier Y/N"}, inplace = True)


general_merchandise_5 = pd.merge(general_merchandise_2, general_merchandise_outlier[["UPC", "Outlier Y/N"]], on = "UPC", how = 'left')
general_merchandise_5 = general_merchandise_5.replace([np.inf, -np.inf, np.nan], 0)
general_merchandise_5_1 = general_merchandise_5[general_merchandise_5["Outlier Y/N"] == "N"]


vitamin_5 = pd.merge(vitamin_2, vitamin_outlier[["UPC", "Outlier Y/N"]], on = "UPC", how = 'left')
vitamin_5 = vitamin_5.replace([np.inf, -np.inf, np.nan], 0)
vitamin_5_1 = vitamin_5[vitamin_5["Outlier Y/N"] == "N"]

grocery_5 = pd.merge(grocery_2, grocery_outlier[["UPC", "Outlier Y/N_1"]], on = "UPC", how = 'left')
grocery_5 = grocery_5.replace([np.inf, -np.inf, np.nan], 0)
grocery_5_1 = grocery_5[grocery_5["Outlier Y/N_1"] == "N"]
grocery_5_1.rename(columns = {"Outlier Y/N_1" : "Outlier Y/N"}, inplace = True)
grocery_5.rename(columns = {"Outlier Y/N_1" : "Outlier Y/N"}, inplace = True)


medicine_5 = pd.merge(medicine_2, medicine_outlier[["UPC", "Outlier Y/N"]], on = "UPC", how = 'left')
medicine_5 = medicine_5.replace([np.inf, -np.inf, np.nan], 0)
medicine_5_1 = medicine_5[medicine_5["Outlier Y/N"] == "N"]


pet_5 = pd.merge(pet_2, pet_outlier[["UPC", "Outlier Y/N"]], on = "UPC", how = 'left')
pet_5 = pet_5.replace([np.inf, -np.inf, np.nan], 0)
pet_5_1 = pet_5[pet_5["Outlier Y/N"] == "N"]


refrigerate_5 = pd.merge(refrigerate_2, refrigerate_outlier[["UPC", "Outlier Y/N"]], on = "UPC", how = 'left')
refrigerate_5 = refrigerate_5.replace([np.inf, -np.inf, np.nan], 0)
refrigerate_5_1 = refrigerate_5[refrigerate_5["Outlier Y/N"] == "N"]


frozen_5 = pd.merge(frozen_2, frozen_outlier[["UPC", "Outlier Y/N"]], on = "UPC", how = 'left')
frozen_5 = frozen_5.replace([np.inf, -np.inf, np.nan], 0)
frozen_5_1 = frozen_5[frozen_5["Outlier Y/N"] == "N"]


alcohol_5 = pd.merge(alcohol_2, alcohol_outlier[["UPC", "Outlier Y/N"]], on = "UPC", how = 'left')
alcohol_5 = alcohol_5.replace([np.inf, -np.inf, np.nan], 0)
alcohol_5_1 = alcohol_5[alcohol_5["Outlier Y/N"] == "N"]


# In[22]:


print(body_care_5_1.count().head(1))
print(produce_5_1.count().head(1))
print(other_5_1.count().head(1))
print(general_merchandise_5_1.count().head(1))
print(vitamin_5_1.count().head(1))
print(grocery_5_1.count().head(1))
print(medicine_5_1.count().head(1))
print(pet_5_1.count().head(1))
print(refrigerate_5_1.count().head(1))
print(frozen_5_1.count().head(1))
print(alcohol_5_1.count().head(1))


# In[23]:


selected_list_2 = pd.concat([body_care_5_1, produce_5_1, pet_5_1, other_5_1, refrigerate_5_1, grocery_5_1,                            vitamin_5_1, general_merchandise_5_1, frozen_5_1, alcohol_5_1, medicine_5_1], axis = 0)

print(selected_list_2)


# In[24]:


# top 12 seasonal items (Descending 4Q Sales values from outlier lists)

pre_data = pd.concat([body_care_5, produce_5, pet_5, other_5, refrigerate_5,                            vitamin_5, general_merchandise_5, alcohol_5, medicine_5], axis = 0)

pre_data_1 = pre_data[pre_data['Outlier Y/N'] == "Y"].drop("index", axis = 1)


pre_data_2 = pre_data_1[["UPC", "Sales 4Q"]].sort_values("Sales 4Q", ascending = False).head(12)

pre_data_3 = pre_data_2["UPC"]

seasonal_list_12 = pd.merge(pre_data_3, pre_data, on = "UPC", how = "left")

seasonal_list_12 = seasonal_list_12.drop("index", axis = 1)


final_select_list = pd.concat([selected_list_2, seasonal_list_12]).drop("index", axis = 1)

print(final_select_list)



# In[61]:


# distribution_selected_items
d_1 = final_select_list.groupby(['Department'])['UPC'].count().reset_index(name="Count").sort_values("Count", ascending = False)
d_1["Percentage"] = d_1["Count"]/d_1["Count"].sum()

print(d_1)

d_2 = final_select_list.groupby(['Department'])['SalesAnnual'].sum().reset_index        (name="SalesAnnual").sort_values("SalesAnnual", ascending = False)

pd.options.display.float_format = "{:,.2f}".format
d_2['SalesAnnual'].astype(float)

d_2["Percentage"] = d_2["SalesAnnual"]/d_2["SalesAnnual"].sum()

print(d_2)


# In[221]:


# Create a pieplot

#x, explode=explode, labels=labels, colors=colors,
 #  2746         autopct=autopct, pctdistance=pctdistance, shadow=shadow,
  # 2747         labeldistance=labeldistance, startangle=startangle,
   #2748         radius=radius, counterclock=counterclock,
   #2749         wedgeprops=wedgeprops, textprops=textprops, center=center,
   #2750         frame=frame, rotatelabels=rotatelabels, normalize=normalize,
   # 2751         **({"data": data} if data is not None else {}))

total_count = d_1["Count"].sum()
label = d_1["Department"]
value = d_1["Count"]

def func(pct, value):
    f_value = int(np.round(pct/100.*np.sum(value)))
    return "{:.1f}%\n({:d})".format(pct,f_value)


fig, ax = plt.subplots(figsize=(13, 13))
ax.pie(value, labels = label, normalize = True , autopct=lambda pct: func(pct,value), data = d_1)

# add a circle at the center to transform it in a donut chart
my_circle=plt.Circle( (0,0), 0.75, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)

plt.title("Item Count Disribution by Department", size = 20)
plt.show()


# In[236]:


total_SalesAnnual = d_2["SalesAnnual"].sum()
label = d_2["Department"]
value = d_2["SalesAnnual"]
departments = d_2["Department"]


def func(pct, value):
    f_value = int(np.round(pct/100.*np.sum(value)))
    return "{:.1f}%\n({:d})".format(pct,f_value)


fig, ax = plt.subplots(figsize=(13, 13))
wedges, texts, autotexts = ax.pie(value, labels = label, normalize = True , autopct=lambda pct: func(pct,value), textprops = dict(color = "w"), data = d_2)


ax.legend(wedges, departments,          title = "Department", loc="center left",
         bbox_to_anchor = (1, 0, 0.5, 1))

# add a circle at the center to transform it in a donut chart
my_circle=plt.Circle( (0,0), 0, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.title("Annual Sales Disribution by Department", size = 20)
plt.show()


# In[484]:


# Annual Sales vs. Annual % Change (Mid-Atlantic)

mid_atl_1 = file_1.replace([np.inf, -np.inf, np.nan], 0)

mid_atl_1 = mid_atl_1[["UPC", "Department", "SalesAnnual", "Sales, Yago Annual"]]

mid_atl_1["Sales % Change"] = (mid_atl_1["SalesAnnual"] - mid_atl_1["Sales, Yago Annual"]) / mid_atl_1["SalesAnnual"] * 100

# count mid atlantic data by department

count_dept = mid_atl_1.groupby("Department")["SalesAnnual"].sum().reset_index(name = "SalesAnnual").sort_values("SalesAnnual", ascending = False)


mid_atl_perc_pre = mid_atl_1.groupby("Department")["Sales % Change"].mean().reset_index(name = "Sales % Change").sort_values("Sales % Change", ascending = False)


mid_atl_merge = pd.merge(count_dept, mid_atl_perc_pre, how = "left", on = "Department")


fig, ax = plt.subplots(figsize=(12, 10))
sns.set_style(style = None, rc = None)
ax.grid(False)

sales_change = mid_atl_merge['Sales % Change']
department = mid_atl_merge['Department']
n = (sales_change.round(2)).astype(str) + str('%')

plt.scatter(department, sales_change)

for i, txt in enumerate(n) :
    plt.annotate(txt, (department[i], sales_change[i]))    
    

kwargs = dict (linestyle = '-', color = 'r', marker = 'o', linewidth = 0.8,               markersize = 5)

sns.lineplot(x = 'Department', y = 'Sales % Change', data = mid_atl_merge,
                   **kwargs, sort = False)

plt.ylim (-8,20)

plt.xticks(rotation = 60)


# In[485]:


sales_annual = mid_atl_merge['SalesAnnual']
n_1 = ((sales_annual/1000000).round(1)).astype(str) + str('M')

fig, ax = plt.subplots(figsize = (20,15))
ax.grid(False)

sns.barplot(x = 'Department', y = 'SalesAnnual', palette = "coolwarm",
           data = mid_atl_merge)

for item, num in enumerate(n_1) :
    plt.annotate(num, (department[item], sales_annual[item]))


ax.set(ylim= (0,500000000))
ax.set_xticklabels(ax.get_xticklabels(), rotation = 45,
                  horizontalalignment = 'right')

ax.set_yticklabels(np.linspace(0,100000000,num = 6, dtype=int))

ax2 = ax.twinx()


sns.lineplot(x = 'Department', y = 'Sales % Change', data = mid_atl_merge,
                   **kwargs, sort = False)

for i, txt in enumerate(n) :
    plt.annotate(txt, (department[i], sales_change[i]))

ax.set_ylabel('Annual Sales, USD (millions)', size = 20)
ax2.set_ylabel('Sales % Change (%)', size = 20)
ax.set_xlabel('Department', size= 20)
ax.set_title("Mid Atlantic 10K Data by Department -- Annual Sales vs Annual % Change", size = 20)


# In[496]:


# Annual Sales vs. Annual % Change (Selected Data)

select_1 = final_select_list.replace([np.inf, -np.inf, np.nan], 0)

select_1 = select_1[["UPC", "Department", "SalesAnnual", "Sales, Yago Annual"]]

select_1["Sales % Change"] = (select_1["SalesAnnual"] - select_1["Sales, Yago Annual"]) / select_1["SalesAnnual"] * 100


# count mid selected data by department

count_dept = select_1.groupby("Department")["SalesAnnual"].sum().reset_index(name = "SalesAnnual").sort_values("SalesAnnual", ascending = False)


select_perc_pre = select_1.groupby("Department")["Sales % Change"].mean().reset_index(name = "Sales % Change").sort_values("Sales % Change", ascending = False)


select_merge = pd.merge(count_dept, select_perc_pre, how = "left", on = "Department")


fig, ax = plt.subplots(figsize=(12, 10))
sns.set_style(style = None, rc = None)
ax.grid(False)

sales_change = select_merge['Sales % Change']
department = select_merge['Department']
n = (sales_change.round(2)).astype(str) + str('%')

plt.scatter(department, sales_change)

for i, txt in enumerate(n) :
    plt.annotate(txt, (department[i], sales_change[i]))    
    

kwargs = dict (linestyle = '-', color = 'r', marker = 'o', linewidth = 0.8,               markersize = 5)

sns.lineplot(x = 'Department', y = 'Sales % Change', data = select_merge,
                   **kwargs, sort = False)

plt.ylim (0,38)

plt.xticks(rotation = 60)


# In[500]:


sales_annual = select_merge['SalesAnnual']
n_1 = ((sales_annual/1000000).round(1)).astype(str) + str('M')

fig, ax = plt.subplots(figsize = (20,15))
ax.grid(False)

sns.barplot(x = 'Department', y = 'SalesAnnual', palette = "coolwarm",
           data = select_merge)

for item, num in enumerate(n_1) :
    plt.annotate(num, (department[item], sales_annual[item]))


ax.set(ylim= (0,300000000))
ax.set_xticklabels(ax.get_xticklabels(), rotation = 45,
                  horizontalalignment = 'right')

ax.set_yticklabels(np.linspace(0,100000000,num = 6, dtype=int))

ax2 = ax.twinx()


sns.lineplot(x = 'Department', y = 'Sales % Change', data = select_merge,
                   **kwargs, sort = False)

for i, txt in enumerate(n) :
    plt.annotate(txt, (department[i], sales_change[i]))

ax.set_ylabel('Annual Sales, USD (millions)', size = 20)
ax2.set_ylabel('Sales % Change (%)', size = 20)
ax.set_xlabel('Department', size= 20)
ax.set_title("Selected UPC 5K Data by Department -- Annual Sales vs Annual % Change", size = 20)

