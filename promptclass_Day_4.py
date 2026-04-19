class PromptTemplate:
    def __init__(self,template,model):
        self.template=template
        self.model=model
    def prompgenerator(self,name):
        return self.template.replace("{name}",name)
        
        