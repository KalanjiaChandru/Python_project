#Vip tech conference
# Event_info=("12/06/2026","Chennai cherpak stadium",120000) #This is tuple we cannot add/append/remove/update
# def event():
#  audiencename=set()
#  while True:
#   print(Event_info)
#   Name=input("Enter your Name for the Dance event || EXIT ")
#   if Name.upper() =='EXIT':
#    a,b,c=Event_info
#    finalcapacity=c-len(audiencename)
#    print(f"Balance seat capacity : {finalcapacity}")
#    print('Good bye')
#    break
# #   audiencename.add(Name)
#   name_to_upper=(lambda data : data.upper())(Name)
#   audiencename.add(name_to_upper)
#   print(name_to_upper)

# event()

#Job Match tool 

# def jobmatch():
#  jRequirements=("python","sql","linux","vectoreDB","RAG")
#  skills=set()
#  for i in range(5):
#   userskills=input("Enter the skills you have ")
#   skills.add(userskills)
#  convertion=set(jRequirements)
#  matching=convertion&skills
#  notMatching=convertion-skills
#  findpercentage=(lambda data:len(data)/len(jRequirements)*100 )(matching)
#  print(f"Candate match for the job percentage {findpercentage}")
# jobmatch()

from promptclass_Day_4 import PromptTemplate

myai=PromptTemplate("Hello {name}, how can i help you today",'Claude 4.5')
print(myai.prompgenerator('chandru'))


