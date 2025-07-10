n = 5
l = []
for i in range(n):
    a = int(input("Enter a Number:"))
    l.append(a)
print(l[::-1])
s = sum(l)
print("sum and avarage of list:",s,(s/n))
