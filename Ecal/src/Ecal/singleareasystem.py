class single_area:
    def __init__(self,turbineconstant,governorconstant,speedregulation,frequency,loadchange):
        self.turbineconstant=turbineconstant
        self.governorconstant=governorconstant
        self.speedregulation=speedregulation
        self.frequency=frequency
        self.loadchange=loadchange
    def workdone(self):
        return (-(self.loadchange)*(1/(1/self.speedregulation)))
    def changeinfrequency(self):
        return self.workdone()*self.frequency
    def newsystemfrequency(self):
        return self.changeinfrequency()+self.frequency
print("Enter the turbine time constant")
turbine_constant=float(input())
print("Enter the governor time constant")
governor_constant=float(input())
print("Enter the governor speed regulation")
speed_regulation=float(input())
print("Enter the frequency")
Frequency=int(input())
print("Enter the sudden load change in per unit")
load_change=float(input())
singlearea=single_area(turbine_constant,governor_constant,speed_regulation,Frequency,load_change)
new_frequency=singlearea.newsystemfrequency()
print("The New System Frequency is : %.3f"%(new_frequency))