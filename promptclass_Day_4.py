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