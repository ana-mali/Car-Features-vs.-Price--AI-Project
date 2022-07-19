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
def average_price():
    #______Average price of full dataset____
    avg_price=data.loc[:,['Price']]
    avg_p=0
    for x in avg_price.iterrows():#iterate through rows
        avg_p+=x[1]
        
    avg_p=avg_p/ROWS
#    print("Average price:"+str(avg_p))
    return avg_p

def averageprice_body():
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
    
#    print('list of average bodystyle prices:')

    return avg_bodystyle

def body_percent(avg_bodystyle,avg_p):
    #percentage difference compared to price average
    percents=[]
    for x in avg_bodystyle:
        temp1=[]
        per=x[1]/avg_p 
        temp1.append(x[0])
        temp1.append(per)
        percents.append(temp1)
    
#    print('percent difference within each bodystyle:')
#    print(percents)
    return percents
def average_horsepower():
    #______Average Horsepower______
    avg_hp=0
    horsepower=data.loc[:,['HP','Price']]
    for x in horsepower.iterrows():
        avg_hp+=x[1] 
#    print(avg_hp)
    avg_hp=avg_hp/ROWS #calculate average horsepower of whole data set
#    print("Average horsepower: "+str(avg_hp))
    return avg_hp

def averageprice_hp():
    #______Average price within horsepower interval________
    avg_horsepower=[]
    hp=data['HP'].unique()
    max=hp.max()
    interval=max/8
    interval_temp=interval
    while interval_temp<=max:#loop through interval
        #loop through all cars within current interval
        model=data.loc[:,['HP','Price']]
        model=model[model['HP']<interval_temp]
        model=model[model['HP']>interval_temp-interval]
        avg_hpp=0 #average price for interval
        for x in model.iterrows():#loop through all rows in subdataframe
            avg_hpp+=x[1] #sum prices
    #    print('index 0 :' +str(avg_hpp[0])) #prints horsepower
    #    print('index 1 :'+str(avg_hpp[1])) #prints price
        avg_hpp=avg_hpp/len(model.index) #average price according to sub frame
        temp=[]
        temp.append(interval_temp) 
        temp.append(avg_hpp)
        avg_horsepower.append(temp)
        interval_temp+=interval
    
#    print("Average price according to horsepower ranges:")
#    print(avg_horsepower)
    return avg_horsepower,interval
def car_depreciationrate(num,predicted_price):
    row=data.iloc[[num]] #get row information
    row=row.loc[:,['Year',"Price"]]
    current_year=2022
    car_productionyear=row.at[num,'Year']
    new_price=predicted_price
    
    if (row.at[num,"Year"]!=current_year):
        new_price=new_price*0.75
        n=current_year-car_productionyear #how many times to depreciate price
        for x in range(n):
            new_price=new_price*0.825
    return new_price
def depreciation(num,predicted_price):
    row=data.iloc[[num]] #get row information
    row=row.loc[:,['Year',"Price",'Model']]
    current_year=2022
    car_productionyear=row.at[num,'Year']
    all_car=data[data['Model']==row.at[num,'Model']]
    all_car.sort_values(by='Price')
    price_list=[]
    n=len(all_car.index)
    for x in range(n): 
        val=all_car.at[0,'Price']
        price_list.append(val)
    print(price_list)
    return predicted_price
    
def predict_price(num):
    """
    Parameters:
        num - integer row number representing a specific car from dataset
    Returns:
        predicted_price - prediction of price
        actual_price - real price from data set
    """
    #first calculate all necessary averages from above functions
    avg_p=average_price()#returns average price of full data set
    avg_bodystyle=averageprice_body() #returns avg price from each body style 
    percents=body_percent(avg_bodystyle, avg_p) #returns percentage difference
    avg_hp,interval=average_horsepower()#returns average hp from whole data set
    avg_horsepower=averageprice_hp()#returns list of avg prices within interval
    row=data.iloc[[num]] 
    row=row.loc[:,['Price','Year','HP','Body Style']]
    actual_price=row.at[num,'Price'] 
    predicted_price=avg_p #start at general average price 
    #reduce price according to depreciation (production year)
    print(row)
    predicted_price=car_depreciationrate(num,predicted_price) 
    
    #adjust price according to body style
    for x in percents:
        if (x[0]==row.at[num,'Body Style']):
            predicted_price=predicted_price+(predicted_price*x[1]) #adjust price
            break;
    
    #adjust price according to horsepower
    hp=row.at[num,'HP']
    print(avg_horsepower)
    for x in avg_horsepower: 
        if (hp<=x[0] and hp>x[0]-interval):
            difference=x[1]/avg_p #calculate percent difference from total average price
            predicted_price=predicted_price+(predicted_price*difference) #adjust predicted price
    #adjust price according to car depreciation
#MAIN EXECUTION
row_num=int(input("Please enter row# to predict price: "))
predict_price(row_num)
