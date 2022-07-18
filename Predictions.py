'''
----------------------------------------
[ALgorithm to predict hypothesis results]
Anastasia & Kiran
----------------------------------------
__updated__= "2022-07-17"
----------------------------------------
'''

import pandas as pd 
import matplotlib.pyplot as matplot

data=pd.read_excel('CarInfo.xlsx',sheet_name='Sheet1') 
print("________")
#______Average price of full dataset____
avg_price=data.loc[:,['Price']]
avg_p=0
print(avg_price.values().type())

print("__________")
for x in avg_price.values():
    avg_p+=x 
avg_p=avg_p/len(avg_price.values())
print("Average price:"+str(avg_p))

#______Average horsepower of full dataset______
avg_horsepower=data.loc[:,["HP"]]
avg_hp=0
for x in avg_horsepower.values():
    avg_hp+=x 
avg_hp=avg_hp/len(avg_horsepower.values()) 

#____Average price of each body style_____
avg_bodystyle=[] #array of all averages 
avg=0
for x in data['Body Style'].unique():
    temp=data[data['Body Style']==x]
    for y in temp.values():
        avg+=y 
    avg=avg/len(temp.values()) 
    temp1=[]
    temp1.append(x) #name of body stule
    temp1.appenc(avg) #average price within bodystyle
    avg_bodystyle.append(temp1)

#percentage difference compared to price average
percents=[]
for x in avg_bodystyle:
    temp1=[]
    per=x[1]/avg_p 
    temp1.append(x[0])
    temp1.append(per)
    percents.append(temp1)

#______Average price according to specific HP range______
hp=data['HP'].unique()
min=0
max=hp.max()
interval=max/8
interval_temp=interval
while interval_temp<=max:#loop through interval
    #loop through all cars within current interval
    model=data[data['HP']<interval_temp]
    model=model[model['HP']>interval_temp-interval]