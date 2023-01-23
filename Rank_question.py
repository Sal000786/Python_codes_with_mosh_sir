# python_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
n=int(input(">"))
for i in range(n):
    name=input("Enter your name ")
    score=float(input("Enter your grade "))
    # for k in range(n):
    #     list=list[name],[score]
    # for j in score:
    #     list=list[name,score]
# print(list)
# list1=[]
# for i in range(n+1):
#     for j in  range(n+1):
#         list1=list1[name,score]
# print(list)
        

# out=list([x,y] for x in name for y in int(score) )
# print(out)

for i in range(n):
    list.append(name)
    for j in range(n):
        list.append(score)
print(list)