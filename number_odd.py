#A four-digit integer is given. Find the number of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of odd digits in the variable "var_int".
x=int(input())
a=(x%10)%2
b=((x//10)%10)%2
c=((x//100)%10)%2
d=((x//1000))%2
print(a+b+c+d)