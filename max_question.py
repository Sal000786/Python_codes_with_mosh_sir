# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     list1=[]
#     for i in range(n+1):
#         list1.append(i)
#     # print(list)
#     max=list1[0]
#     for j in list1:
#         if max<j:
#             max=j

# print("max is",max)
n=int(input("enter a number "))        
list=[]
new_list=[]
for i in range(n):
    n=int(input('>'))
    list.append(n)
for j in list:
    if j not in new_list:
        new_list.append(j)
print(new_list)
    
    

new_list.sort()
# print(list)
new_list.pop()
print(new_list)
print(f'max of the list is {new_list[-1]}')

# max=list[0]
# for i in list:
#     if i>max:
#         max=i
# print(max)

    