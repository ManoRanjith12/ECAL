import math
from math import sin
from math import sqrt
class OC_test:
    def __init__(self,V1,Io,Po):
        self.V1=V1
        self.Io=Io
        self.Po=Po
    def opencircuittest(self):
        coso=self.Po/(self.V1*self.Io)
        O=math.acos(coso)
        sino=sin(O)
        Im=self.Io*coso
        Ro=(self.V1/Im)
        Iu=self.Io*sino
        Xo=self.V1/Iu
        print("R0=%.2f ohm"%(Ro))
        print("X0=%.2f ohm"%(Xo))
class SC_test:
    def __init__(self,Vsc,Isc,Wsc,K):
        self.Vsc=Vsc
        self.Isc=Isc
        self.Wsc=Wsc
        self.K=K
    def shortcircuittest(self):
        Zo2=self.Vsc/self.Isc
        Ro2=self.Wsc/(self.Isc**2)
        Zo1=Zo2/(self.K**2)
        Ro1=Ro2/(self.K**2)
        Xo1=sqrt((Zo1*Zo1)-(Ro1*Ro1))
        print("R01=%.4f"%(Ro1))
        print("X01=%.4f"%(Xo1))
        print("Z01=%.4f"%(Zo1))
print("Enter the value of primary voltage")
primaryvoltage=float(input())
print("Enter the value of secondary voltage")
secondaryvoltage=float(input())
print("Enter the values for OC Test")
print("Enter the value of no load current Io")
noloadcurrent=float(input())
print("Enter the value of no load input power Po")
inputpower=float(input())
print("Enter the values for SC test")
print("Enter the short circuit voltage Vsc")
vsc=float(input())
print("Enter the short circuit current Isc")
isc=float(input())
print("Enter the full load copper loss Wsc")
wsc=float(input())
k=secondaryvoltage/primaryvoltage
octest=OC_test(primaryvoltage,noloadcurrent,inputpower)
octest.opencircuittest()
sctest=SC_test(vsc,isc,wsc,k)
sctest.shortcircuittest()
