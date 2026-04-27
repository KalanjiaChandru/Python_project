class PromptTemplate:
    def __init__(self,template,model):
        self.template=template
        self.model=model
    def prompgenerator(self,name):
        return self.template.replace("{name}",name)
        
        
class History:
    def __init__(self):
        self.history = []
       
    def sendMessage(self,userInput,user):
        formattingprompt=str(userInput).strip()
        formatted={"user":user,"prompt":formattingprompt}
        self.history.append(formatted)

    def get_history(self):
        for his in self.history:
            print(f"{his['user']}-{his['prompt']}")
     
    
    def clear_history(self):
        self.history=[]

import json

class Aiparson:
    def __init__(self,name,skills,history=None):
        self.name=name
        self.skills=set(skills)
        self.history={}if history is None else history
        self.data=[]

    def addMessage(self,prompt,bot):
        print(prompt,bot)
        data={'user':self.name,'prompt':prompt}
        if bot not in self.history:
            self.history[bot]=[]

        self.history[bot].append(data)
    
    def viewHistory(self,bot):
        if self.history[bot]:
            for him in self.history:
                for bot in self.history[bot]:
                    print(bot)

    def Exit(self,bot):
        with open('storage.json','w')as store:
            json.dump(self.history,store,indent=4)
        print('Good boy')

        

    


            

        
    