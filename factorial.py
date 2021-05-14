def fact_num(n):
    f=1
    for i in range(1,n+1):
        f=f*i 
    return f

n=int(input("Enter the number"))
result=fact_num(n)
print(result)