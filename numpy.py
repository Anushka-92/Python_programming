n = input("enter value of n : ")
print(n)
o = int(n%2 == 1)
e = int(n%2 == 0)
if n == o :
  print("Weird")
elif n== e and (2<n<5 ):
    print("Not Weird")
elif n== e and 6<n<20:    
    print("Weird")
elif n== e and n>20:
    print("Not Weird")
    

