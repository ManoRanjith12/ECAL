class three_phase_IM:
    def __init__(self,Pole,Slip,input_power,Frequency,stator_loss,Torquelost):
        self.Pole=Pole
        self.Slip=Slip
        self.input_power=input_power
        self.Frequency=Frequency
        self.stator_loss=stator_loss
        self.Torquelost=Torquelost
    def speed(self):
        return (1-self.Slip)*((120*self.Frequency)/self.Pole)
    def frictionalloss(self):
        print(self.Torquelost)
        return (((2*3.14*self.speed())/60)*self.Torquelost)/1000
    def rotorpower(self):
        return self.input_power-self.stator_loss
    def mechanicalpower(self):
        return (1-self.Slip)*self.rotorpower()
    def outputpower(self):
        return self.mechanicalpower()-self.frictionalloss()
    def efficiency(self):
        return (self.outputpower()/self.input_power)*100
print("Enter the Number of Poles")
poles=int(input())
print("Enter the slip value in %")
slip=float(input())/100
print("Enter the Value of input Power in KW")
powerin=float(input())
print("Enter the value of Frequency")
frequency=float(input())
print("Enter the Stator loss in KW")
statorloss=float(input())
print("Enter the value of Torque lost")
torquelost=float(input())
threephaseIM=three_phase_IM(poles,slip,powerin,frequency,statorloss,torquelost)
speed=threephaseIM.speed()
Output_power=threephaseIM.outputpower()
efficiency=threephaseIM.efficiency()
print("The Speed of the motor is %d RPM"%(speed))
print("The Output Power is %.4f KW"%(Output_power))
print("The efficiency is %.2f "%(efficiency))
