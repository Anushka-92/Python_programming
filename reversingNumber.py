# num=int(input("Enter the no. for reversing is"))
# rev=0
# while(num>0):
#     n = num %10
#     rev=(rev* 10) + n
#     print("reverce number is :"+str(rev))    
#     num=num//10
num=int(input("Enter 4 digit number:"))
r=num%10
print("last number in given is",r)
a=num//1000
print("First number is :",a)
print("Sum of first and last number is:",a+r)