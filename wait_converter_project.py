
x=input(" enter press P for ponds and K kg")
# weight=input("Enter your weight")K
if x=="P":
    pond=int(input("Enter weight"))
    kg=pond/2.205
    print("Weight in kilograms= ",kg)
elif x=="K":
    kilo=int(input("Enter weight pls"))
    pond1=kilo*2.205
    print("Weight in pond is= ",pond1)
else:
    print("Some error occured")



weight=int(input("Enter weight: "))
unit=input("enter P for pounds and K for kilograms\n")
if unit.upper()=="P":
    converted=weight*0.45
    print(f'you are {converted} pounds')
else:
    converted=weight/0.45
    print(f'you are {converted} kilograms')
