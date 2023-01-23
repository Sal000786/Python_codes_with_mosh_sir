import math as m
I1=float(input("Enter the input values of I1"))
print("value of I1",I1)

I2=float(input("Enter the input values of I2"))
print("value of I2",I2)


w1=float(input("Enter the weight w1 "))
w2=float(input("Enter the weight w2 "))
w3=float(input("Enter the weight w3 "))
w4=float(input("Enter the weight w4 "))
w5=float(input("Enter the weight w5 "))
w6=float(input("Enter the weight w6 "))
w7=float(input("Enter the weight w7 "))
w8=float(input("Enter the weight w8 "))
print("Weights are",w1,w2,w3,w4,w5,w6,w7,w8) 

print("Please enter the values for the bias")
b1=float(input("Enter the weight b1 "))
b2=float(input("Enter the weight b2 "))
print("bias values are= ",b1,b2)


print("Expected values please")
ex1=float(input("Enter the weight ex1 "))
ex2=float(input("Enter the weight ex2 "))
print("expected values are= ", ex1,ex2)

print("Input of h1")

inp_h1=(w1*I1)+(w2*I2)+(b1*1)
print("input of h1",inp_h1)

Out_h1=1/(1+m.exp(-inp_h1))
print("output of H1",Out_h1)




print("input of h2")

inp_h2=(w3*I1)+(w4*I2)+(b1*1)
print("input of h2",inp_h2)

Out_h2=1/(1+m.exp(-inp_h2))
print("output of H2",Out_h2)


print("input of O1")

inp_O1=(Out_h1*w5)+(Out_h2*w6)+(b2*1)
print("input of O1",inp_O1)

Out_O1=1/(1+m.exp(-inp_O1))
print("Output of O1",Out_O1)


print("input of O2")

inp_O2=(Out_h1*w7)+(Out_h2*w8)+(b2*1)
print("input of O2",inp_O2)

Out_O2=1/(1+m.exp(-inp_O2))
print("Output of O2",Out_O2)

print("calculating error of O1")
error_o1=((ex1-Out_O1)*(ex1-Out_O1))/2
print("error of O1 is=",error_o1)


print("calculating error of O2")
error_o2=((ex2-Out_O2)*(ex2-Out_O2))/2
print("error of O2 is=",error_o2)

print("Calculating total erro")
total_error=error_o1+error_o2

print("total error is= ",total_error)




