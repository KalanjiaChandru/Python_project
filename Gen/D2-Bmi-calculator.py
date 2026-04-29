class Bmi:

    def __init__(self,height,weight):
        self.height=height
        self.weight=weight

        pass
     
    def metricCalculation(self):
        cm_to_m=self.height/100
        cal=self.weight/(cm_to_m*cm_to_m)
       
        return cal
        pass



def FindBmiCal():
    height=input('Enter your height in cm ')
    weight=input('Enter your weight in kg ')
    try:
     convertheight=float(height.strip())
     convertweight=float(weight.strip())
     if height <= 0 or weight <= 0:
            print("Height and weight must be positive numbers.")
            return
    except ValueError:
        print("Please enter valid numbers.")
        return
    cal=Bmi(convertheight,convertweight)

    outputvalue=cal.metricCalculation()
    if outputvalue < 18.5:
            print(f"your Bmi value is {outputvalue} so you are underweight")
    elif outputvalue <25:
            print(f"your Bmi value is {outputvalue}, so you are in Healthy weight")
    elif outputvalue<29.9:
             print(f"your Bmi value is {outputvalue}, so you are over Weight")
    else:
             print(f"your Bmi value is {outputvalue}, so you are obesity")


      
        
    
FindBmiCal()