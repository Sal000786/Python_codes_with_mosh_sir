#general arithmetic operators in python
print(10+5)
print(10-5)
print(10*5)
print(10/5)
print(10//5)
print(10%5)
print(10**3)

# Augmented Assignment operator
x=10
print(x)
x=x+3
print(x)
x+=3
print(x)

#operator precence

x=10+3*2**6
print(x)
x=(10+3)*2**6
print(x)
# operator precence defines, which part of code or expression will be executed first
"""The precedence of the operaotrs are 
1st parenthesis
2nd exponentiation
3rd multiply or divide
4th add or sub 

if the precedence of the operators are same then the code execution follows left to right or right to left derivation"""