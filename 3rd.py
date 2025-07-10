#Create a function called divide(a, b) that returns the result of a / b.
#Use try...except to handle divide-by-zero errors and display a user-friendly message.
try:
    a,b = map(int,input("Enter Two numbers here:").split())
    print(a/b)
except:
    print("Zero Division Error")
