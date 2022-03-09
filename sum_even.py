#A four-digit integer is given. Find the sum of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_even" and assign it 0.

#Find the sum of the even digits in the variable "var_int".

x=int(input())
a=round((x%10)+1)
b=((x//10)%10+1)%2
c=((x//100)%10+1)%2
d=((x//1000)+1)%2
print(a+b+c+d)