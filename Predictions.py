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
ROWS=len(data.index)
print('Number of rows: '+str(ROWS))

#______Average price of full dataset____
avg_price=data.loc[:,['Price']]
avg_p=0
for x in avg_price.iterrows():#iterate through rows
    avg_p+=x[1]
    
avg_p=avg_p/ROWS
print("Average price:"+str(avg_p))

#______Average horsepower of full dataset______
avg_horsepower=data.loc[:,["HP"]]
avg_hp=0
for x in avg_horsepower.iterrows():
    avg_hp+=x[1]
avg_hp=avg_hp/ROWS 
print("Average horsepower: "+str(avg_hp))

#____Average price of each body style_____
avg_bodystyle=[] #array of all averages 
avg=0
bodydataframe=data.loc[:,['Body Style','Price']]
for x in data['Body Style'].unique():
    temp=bodydataframe[bodydataframe['Body Style']==x]
    for y in temp.iterrows():
        a=y[1].to_list()
        avg+=a[1]
    avg=avg/ROWS 
    avg=float("{:.2f}".format(avg))
    temp1=[]
    temp1.append(x) #name of body stule
    temp1.append(avg) #average price within bodystyle
    avg_bodystyle.append(temp1)

print('list of average bodystyle prices:')
for x in avg_bodystyle:
    print(x)
#percentage difference compared to price average
percents=[]
for x in avg_bodystyle:
    temp1=[]
    per=x[1]/avg_p 
    temp1.append(x[0])
    temp1.append(per)
    percents.append(temp1)

print('percent difference within each bodystyle:')
print(percents)

#______Average Horsepower______
avg_hp=0
horsepower=data.loc[:,['HP','Price']]
for x in horsepower.iterrows():
    avg_hp+=x[1] 
print(avg_hp)
avg_hp=avg_hp/ROWS #calculate avg horsepower of whole dataset
print("Average horsepower: "+str(avg_hp))

#______Average price within horsepower interval________
avg_horsepower=[]
hp=data['HP'].unique()
max=hp.max()
interval=max/8
interval_temp=interval
while interval_temp<=max:#loop through interval
    #loop through all cars within current interval
    model=data.loc[:,['HP','Price']]
    model=data[data['HP']<interval_temp]
    model=model[model['HP']>interval_temp-interval]
    model=model[model['Fuel Type']!='Electric']
    avg_hpp=0 #average price for interval
    for x in model.iterrorws():#loop through all rows in subdataframe
        print(x)
        avg_hpp+=x[1] 
    avg_hpp=avg_hpp/len(model.index) #average price according to sub frame
    temp=[]
    temp.append(interval_temp) 
    temp.append(avg_hpp)
    avg_horsepower.append(temp)

print("Average horsepower according to ranges:")
print(avg_horsepower)
