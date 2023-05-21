class dcseries:
    def __init__(self,Voltage,Poles,Conductors,Output_power,Current,Flux,Armature_resistance,Winding):
        self.Voltage=voltage
        self.Poles=Poles
        self.Conductors=Conductors
        self.Output_power=Output_power
        self.Current=Current
        self.Flux=Flux
        self.Armature_resistance=Armature_resistance
        self.Winding=Winding
    def armature_torque(self):
        return ((self.Flux*self.Current*self.Poles*self.Conductors)/self.Winding)*0.159
    def backemf(self):
        return self.Voltage-(self.Current*self.Armature_resistance)
    def speed(self):
        return (self.backemf()*60*self.Winding)/(self.Poles*self.Flux*self.Conductors)
    def shaft_torque(self):
        return (9.55*self.Output_power)/self.speed()
    def torque_lost(self):
        return self.armature_torque()-self.shaft_torque()
print("Enter the value of the supply voltage,V:")
voltage=float(input())
print("Enter the value of No of poles,P:")
poles=float(input())
print("Enter the no of conductors,Z:")
conductors=float(input())
print("Enter the value of output Power in watts,Pout:")
outputpower=float(input())
print("Enter the value of current, Ia:")
current=float(input())
print("Enter the value of flux per pole,Φ:")
flux=float(input())
print("Enter the value of Armature resistance, Ra:")
armatureresistance=float(input())
print("For Wave winding press 1")
print("For lap winding press 2")
type=int(input())
if(type==1):
    winding=2
if(type==2):
    winding=poles
series=dcseries(voltage,poles,conductors,outputpower,current,flux,armatureresistance,winding)
armaturetorque=series.armature_torque()
speed=series.speed()
shafttorque=series.shaft_torque()
losttorque=series.torque_lost()
print("Armature Torque, Ta:%.3f Nm"%(armaturetorque))
print("speed, N:%.3f Rpm"%(speed))
print("Shaft Torque, Tsh:%.3f Nm"%(shafttorque))
print("Torque Lost, Tf:%.3f Nm"%(losttorque))
