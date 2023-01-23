n=input("Enter your name\n")
if len(n)<3:
    print("name must be atleast 3 character")
elif len(n)>20:
    print("name can be maximum 20 character long")
else:
    print("name looks good!")
