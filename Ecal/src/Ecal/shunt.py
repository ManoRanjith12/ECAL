class dcshunt:
    def __init__(self,Power,Voltage,ArmatureResistance,ShuntResistance):
        self.Power=Power
        self.Voltage=Voltage
        self.ArmatureResistance=ArmatureResistance
        self.ShuntResistance=ShuntResistance
    def linecurrent(self):
        return self.Power/self.Voltage
    def fieldcurrent(self):
        return self.Voltage/self.ShuntResistance
    def armaturecurrent(self):
        return self.linecurrent()-self.fieldcurrent()
    def backemf(self):
        return self.Voltage-(self.armaturecurrent()*self.ArmatureResistance)
    def power(self):
        return self.backemf()*self.armaturecurrent()
class dcshuntline:
    def __init__(self,Voltage,LineCurrent,ArmatureResistance,ShuntResistance):
        self.Voltage=Voltage
        self.LineCurrent=LineCurrent
        self.ArmatureResistance=ArmatureResistance
        self.ShuntResistance=ShuntResistance
    def fieldcurrent(self):
        return self.Voltage/self.ShuntResistance
    def armaturecurrent(self):
        return self.LineCurrent-self.fieldcurrent()
    def backemf(self):
        return self.Voltage-(self.armaturecurrent()*self.ArmatureResistance)
print("To calculate Line Current,Field Current,back emf, Armature Power using Power Press 1")
print("To calculate back emf using Line Current, Voltage, press 2 ")
print("------------------------------------------------------------------------------------")
n=int(input())
if(n==1):
    print("Enter the value of Power in Watts:")
    power=(int(input()))
    print("Enter the value of Voltage in volts:")
    voltage=(int(input()))
    print("Enter the value of Armature Resiatance(Ra):")
    armatureresistance=(float(input()))
    print("Enter the value of ShuntResistance(Rsh):")
    shuntresistance=(float(input()))
    shunt=dcshunt(power,voltage,armatureresistance,shuntresistance)
    Iline=shunt.linecurrent()
    Ifield=shunt.fieldcurrent()
    Iarmature=shunt.armaturecurrent()
    Vback=shunt.backemf()
    powerdeveloped=shunt.power()
    print("Line Current(IL): %.3f A"%(Iline))
    print("Shunt field current(Ish): %.3f A"%(Ifield))
    print("Armature Current(Ia): %.3f A"%(Iarmature))
    print("Back emf(Eb): %.3f V"%(Vback))
    print("Power developed in armature= %.3f W"%(powerdeveloped))
if(n==2):
    print("Enter the value of Voltage in volts:")
    voltage=(int(input()))
    print("Enter the value of line current(Il):")
    linecurrent=(int(input()))
    print("Enter the value of Armature Resiatance(Ra):")
    armatureresistance=(float(input()))
    print("Enter the value of ShuntResistance(Rsh):")
    shuntresistance=(float(input()))
    shunt=dcshuntline(voltage,linecurrent,armatureresistance,shuntresistance)
    Vback=shunt.backemf()
    print("Back emf(Eb): %.3f V"%(Vback))
