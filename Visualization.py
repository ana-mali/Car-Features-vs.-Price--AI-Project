'''
----------------------------------------
[Modeling Module]
Anastasia & Kiran
----------------------------------------
__updated__= "2022-07-15"
----------------------------------------
'''
import pandas as pd #pip install pandas in command prompt
#also install openpyxl 
import matplotlib.pyplot as matplot
data=pd.read_excel('CarInfo.xlsx',sheet_name='Sheet1') #read file into Dataframe

#MODELING
#_____________Year vs. Price___________________
model1=data[data['Model']=='Jetta'] 
model1=model1.sort_values(by=['Year'])
model1=model1.loc[:,['Year','HP','Engine Size','Price']]
bargraph=model1.plot.bar(x='Year',y='Price',color='red',fontsize='10')
print('Sub-Dataframe including all Volkswagen Jetta')
print(model1) #print sub-dataframe from main Dataframe
matplot.show() #show first model regarding year vs. price of the Jetta
#must close this graph in order to see the next one 
#_____________Year vs. HorsePower_______________
bargraph=model1.plot.bar(x='Year',y='HP')
matplot.show()

#_____________Vintage cars_______________________
#CAMARO
model2=data[data['Model']=='Camaro ZL1']
model2=model2.sort_values(by=["Year"])
model2=model2.loc[:,["Year",'HP','Engine Size','Seats','Price','Cylinders']]
print('Sub-Dataframe including all Chevrolet Camaro ZL1')
bargraph=model2.plot.bar(x='Year',y='Price')
matplot.show()
print(model2)
#FERRARI
model3=data[data['Make']=='Ferrari']
model3=model3.sort_values(by='Year')
model3=model3.loc[:,['Model',"Year",'HP','Engine Size','Price','Cylinders','Transmission']]
print("Sub-Dataframe including all Ferrari's")
print(model3) 
#______________Electric Cars______________
model4=data[data['Electric']=='Yes']
model4=model4.sort_values(by='Price')
model4=model4.loc[:,['Model','HP','Price','Transmission','Body Style']]
print("Sub-Dataframe including all electric cars")
print(model4)

#_____________Price vs. Body Styles__________
for x in data['Body Style'].unique():
    print('Sub-Dataframe including all '+x+' cars')
    model=data[data['Body Style']==x]
    model=model.sort_values(by='Price')
    model=model.loc[:,['Model','Price','HP','Doors','Seats','Year']]
    print(model)

#___________Horsepower vs. Engine Size________
hp=data['HP'].unique()
min=0
max=hp.max()
interval=max/8
interval_temp=interval
while interval_temp<=max:
    print('Sub-Dataframe including '+str(interval_temp-interval)+'to '+str(interval_temp)
          +' horsepower')
    model=data[data['HP']<interval_temp]
    model=model[model['HP']>interval_temp-interval]
    model=model[model['Fuel Type']!='Electric'] #electric vehicles do not have engine size
    model=model.sort_values(by='Price')
    model=model.loc[:,['Model','HP','Engine Size','Price']]
    model['HP'].plot()
    model['Engine Size'].plot(secondary_y=True,style='g')
    matplot.show()
    print(model)
    interval_temp+=interval

