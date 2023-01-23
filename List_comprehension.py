if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # list1=[]
    # list2=[]
    # sum=0
    # for i in range(x):
    #     for j in range(y):
    #         for k in range(z):
    #             list1=list[i,j,k]
    #             list2.append(list1)
    # print(list2,end=" ")
    # for m in list2:
    #     # for v in list1:
    #     sum=sum+m
    #     print(sum)


                # for m in list1:
                #     sum=sum+m
                #     print(sum)
# if sum!=n:
#     print(f'the list whoose sum is not equal to n are ',list1)
                # print(sum(list1))
# sum=0
# for m in range(n):
#     sum+=list(m)

                

# list2=[1,2,4,5]
# sum=0
# for i in list2:
#     sum=sum+i
#     print(sum)
#     print(i)
    print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)  if i+j+k !=n))