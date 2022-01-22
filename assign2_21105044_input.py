#Assignment2

      #1st program
print('1st program')
#[a] (length of string)
string=str(input("Enter the string: "))
print("(a) Length of string is: ", len(string))

#[b] (reverse string)
newString=string[::-1]
print("(b) The reversed string is: ", newString)

#[c] (slicing string)
S=slice(10, 26)
print("(c) New string after slicing: ", string[S])

#[d] (replace substring)
a=string.replace('a case sensitive', 'object oriented')
print("(d) Replacing substring: ", a)
#[e] (finding index of substring)
i=string.index('a')
print("(e) The index of 'a' is: ", i)

#[f] (removing spaces from the string)
r=string.replace(' ','')
print("(f) Removing white spaces: ", r)

     #2nd program
print('2nd program')
Name='Aryana'
SID=21105044
Department='ECE'
CGPA=10
print('Hey, %s Here! \nMy SID is %d \nI am from %s department and my CGPA is %d.' %(Name,SID,Department,CGPA))

    #3rd program
print('3rd program')
a=56
b=10
print('a. a & b=%d' % (a & b))
print('b. a | b=%d' % (a | b))
print('c. a ^ b=%d' % (a ^ b))
print('d. Left shift both a and b with 2 bits : a = %d, b = %d' % (a << 2,b << 2))
print('e. Right shift a with 2 bits and b with 4 bits : a = %d, b = %d'% (a >> 2,b>>4))

    #4th program
print('4th program')
num1=int(input("Enter the 1st number: "))
num2=int(input("Enter the 2nd number: "))
num3=int(input("Enter the 3rd number: "))
if (num1 >= num2) and (num1 >= num3):
 largest = num1
elif (num2 >= num1) and (num2 >= num3):
 largest = num2 
else:
 largest = num3
print('The largest number is',largest)

   #5th program
print('5th program')
string=str(input("Enter the string: "))
if "name" in string:
 print('Yes')
else:
 print('No')

   #6th program
print('6th program')
side_1=int(input("Enter the 1st side of the triangle: "))
side_2=int(input("Enter the 2nd side of the triangle: "))
side_3=int(input("Enter the 3rd side of the triangle: "))
if side_1 < side_2 + side_3 and side_2 < side_1 + side_3 and side_3 < side_2 + side_1:
 print('Yes')
else:
 print('No')

