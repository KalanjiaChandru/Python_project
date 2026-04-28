menu=[{'id':1,'name':'chicken rice','price':100},{'id':2,'name':' rice','price':200},{'id':3,'name':'Grill','price':450},{'id':4,'name':'limeon juice','price':40}]
orderdetails=[]

def calculation(x,y):
  amount=0
  for item in orderdetails:
    amount+=item['price']
  value=amount*(x/100)
  totalbill=amount+value
  
  splitforeach=totalbill/y
  return {'TipAmount':value,'TotalBill':totalbill,'Perpersonsplit':splitforeach}

try:
 order=input('Enter the order id in the input what you want,If no need press esc example(1,2,5,8)')
#  print(order)
 
 seperation={int(x) for x in order.split(',')}
 
 for val in menu:
   if val['id'] in seperation: 
    orderdetails.append(val)
    # print(val)

   pass
 tip=input('Enter the tip percentage ')
 person=input('Enter how many person want to split the bill ')
 try:
   con=float(tip)
   pcon=int(person)
   finalvalue=calculation(con,pcon)
   print(finalvalue)

 except ValueError:
    print("❌ Error: Please enter numbers only (don't type letters for prices/people).")
 except ZeroDivisionError as e:
    print(f"❌ Math Error: {e}")
 except Exception as e:
    print(f"❌ Unexpected Error: {e}")


except ZeroDivisionError:
  print('Enter the valued number Zero is not divisable')
except TypeError:
  print('The input type is different')
except:
  print('Kindly enter the number what are listed in the menu ')
# print(orderdetails,'orderDetails')
