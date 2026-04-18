# # Expense calculator
# monthlyamount=int(input('Enter the montly expense to calculate '))
# Travel=[]
# Food=[]
# Rent=[]
# Games=[]
# def ExpenseCalculator():
    
#     findtype=input('You want  to Status 1.Create | 2.Summary | 3.View | 4.Exit ')
#     listmapping={'1':'Create','2':'Summary','3':'View','4':'Exit'}
#     find=listmapping.get(findtype,'unKnown')
   
#     if find == 'Exit':
#         print('Take you time and be happy ')
#         return
#     elif find == 'Create':
#         category=input('Select the category 1.Travel | 2.Food | 3.Rent | 4.Games')
#         findCat={'1':'Travel','2':'Food','3':'Rent','4':'Games'}
#         fixcat=findCat.get(category,'No Category')
#         if fixcat == 'Travel':
#             travelplace=input('Enter the place where you have travelled')
#             travelamount=int(input('Enter the amount you have spend'))
#             travelexp={'place':travelplace,'Amount':travelamount}
#             Travel.append(travelexp)
#         elif fixcat=='Food':
#             Foodplace=input('Enter the food you have tasetd')
#             Foodamount=int(input('Enter the amount you have spend'))
#             foodexp={'Food':Foodplace,'Amount':Foodamount}
#             Food.append(foodexp)
#         elif fixcat=='Rent':
#             Rentplace=input('Enter the Rent you have payed')
#             Rentamount=int(input('Enter the amount you have spend'))
#             rentExp={'Rent':Rentplace,'Amount':Rentamount}
#             Rent.append(rentExp)
#         elif fixcat=='Games':
#             Sportplayed=input('Enter the Sport  you have played')
#             sportamount=int(input('Enter the amount you have spend'))
#             sportexp={'Sport':Sportplayed,'Amount':sportamount}
#             Rent.append(sportexp)
#         else:
#             print('Enter the correct category || in futhure we can create new category feature will be add')
       
#     elif find=='Summary':
#         combained=Travel+Food+Rent+Games
#         total=sum(item['Amount'] for item in combained)
#         finalamount = monthlyamount-total
#         if finalamount>0:
#             print('Finally amount in you montly expense is ', finalamount)
#         else:
#             print('Final amount in expense is over you have negative amount',finalamount)
#         print('Initial amount',monthlyamount)
#         print('Total expense of the monthy is ',total)
#         expcount=len(combained)
#         findaverage=total/expcount
#         print('Average amount spend ',findaverage)

#     elif find == 'View':
#         combained=Travel+Food+Rent+Games
#         for item in combained:
#             print(item)

#     else:
#         print('only the selected status action only present. Kindly select from that')
#     ExpenseCalculator()
        
    


# ExpenseCalculator()        
# print('Travel = ',Travel,'Food = ',Food,'Games = ',Games,'Rent = ',Rent)



        
            

#Expense Calculatore --AI Answer--

MonthlyExpense=int(input('Enter the montly amount need for expense '))
Expense=[]
def MonthlyExpenseCalculator():
    while True :
     with open("storage.json","r") as save:
        store=save.readlines()
        Expense=store
        print(Expense)
     selectMode=input('Select what you want 1.Creat | 2.Summary | 3.View | 4.Exit ' )
     if selectMode=='4':
        print('Good Bye')
        break
     elif selectMode=='1':
        try:
            cate=input('Enter the expense category 1.Travel | 2.Food | 3.Rent | 4.Games')
            catemap={'1':'Travel','2':'Food','3':'Rent','4':'Games'}
            find=catemap.get(cate,'Others')
            name=input('What do you buy ')
            amount=int(input('How much it coast '))
            obj={'name':name,'amount':amount,'category':find}
            #Storing to the external json formate 
            with open("storage.json","a")as save:
             convert=str(obj)
             save.write(convert)
            
            Expense.append(obj)
        except Exception as e:
            print(f"An error occurred: {e}")
     
     elif selectMode == '2':
        if not Expense:
            print("No expenses recorded.")
            continue
        total = sum(item['amount'] for item in Expense)
        avg=total/len(Expense)
        print('Total amount you have spend ' , total)
        print('Average for one expense ' , avg)
     elif selectMode=='3':
        for item in Expense:
           print(f"[{item['category']}] {item['name']}: ${item['amount']}")

MonthlyExpenseCalculator()

    
          
     
    
