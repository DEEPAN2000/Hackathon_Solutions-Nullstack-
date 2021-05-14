def fibonnaci_recursive(n):
   if n<=1:
      return n 
   return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)

n=int(input("Enter the no of elements"))
for i in range(n):
   print(fibonnaci_recursive(i))

