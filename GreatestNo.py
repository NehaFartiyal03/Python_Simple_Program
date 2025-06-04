# WAP to find the greatest of 3 Numbers entered by the user.

#a  = int(input("enter first no:"))

#b = int(input("enter second no:"))
#c  = int(input("enter third no:"))

a = "34"
b = "54"
c = "23"
d = "56"

if(a >= b and a >= c and a >= d):
    print("first  is greater", a)
elif(b  >= c and b >=d):
    print("second is greater", b)
elif(c >= d):
    print("third is greater", c)
else:
    print("fourth is greater",d)
