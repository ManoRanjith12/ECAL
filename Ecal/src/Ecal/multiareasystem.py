class multi_area:
    def __init__(self,Load_change,B1,B2,F1,F2):
        self.Load_change=Load_change
        self.B1=B1
        self.B2=B2
        self.F1=F1
        self.F2=F2
    def work_done(self):
        return -(self.Load_change/(self.B1+self.B2))
print("Enter the turbine output power of area 1")
tpower1=input()
print("Enter the turbine output power of area 2")
tpower2=input()
print("Enter the Frequency of area 1:")
frequency1=input()
print("Enter the Frequency of area 2:")
frequency2=input()
print("Enter the speed regulation of area 1 in %")
speedreg1=float(input())
speedreg1=speedreg1/100
print("Enter the speed regulation of area 2 in %")
speedreg2=float(input())
speedreg2=speedreg2/100
print("Enter the value of turbine time constant of area 1")
turcon1=input()
print("Enter the value of turbine time constant of area 2")
turcon2=input()
print("Enter the value of governor time constant of area 1")
govcon1=input()
print("Enter the value of governor time constant of area 2")
govcon2=input()
print("Enter the value of D of area 1:")
d1=float(input())
print("Enter the value of D of area 2:")
d2=float(input())
b1=(1/(speedreg1))+d1
b2=(1/(speedreg2))+d2
print("Enter the value of loadchange:")
loadchange=float(input())
multiarea=multi_area(loadchange,b1,b2,frequency1,frequency2)
workdone=multiarea.work_done()
print("The Workdone is : %.5f"%(workdone))
