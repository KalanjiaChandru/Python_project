menu=[{'id':1,'name':'chicken rice','price':100},{'id':2,'name':' rice','price':200},{'id':3,'name':'Grill','price':450},{'id':4,'name':'limeon juice','price':40}]
orderdetails=[]

  
try:
 order=input('Enter the order id in the input what you want,If no need press esc example(1,2,5,8)')
 
 seperation=set(order.split(','))
 print(seperation)
 for val in menu:

   
   if val.id in seperation :
    orderdetails.append(val)
 
   
   
   pass
   
 
 

except TypeError:
  print('The input type is different')
except:
  print('Kindly enter the number what are listed in the menu ')
print(orderdetails,'orderDetails')