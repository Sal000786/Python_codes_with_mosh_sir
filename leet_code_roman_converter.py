roman={
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "M":1000
}
inp=input("Enter roman number")
out=0
for i in range(len(inp)):
    if inp[i] in roman:
            out+=roman.get(inp[i])
print(out)
    