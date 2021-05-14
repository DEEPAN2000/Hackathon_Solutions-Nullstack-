def even_odd_func(n):
    if( n % 2)== 0:
        return 1
    else:
        return 0

n=int(input("ENTER A NUMBER")) 
a=even_odd_func(n) 
if (a == 1):
    print("EVEN NUMBER")
else:
    print("ODD NUMBER")           


    