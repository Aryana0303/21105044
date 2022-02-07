#Assignment3

   #1st program
print('1st program')
string=str(input("enter the string")).lower()
def word_count(str):
    counts=dict()
    words=str.split()

    for word in words:
        if word in counts:
            counts[word]+=1
        else:
            counts[word]=1

    return counts

print(word_count(string))

    #2nd program
print('2nd program')
def year():                                                                                
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
while True:
    date = int(input("Date - "))
    month = int(input("Month - "))
    year = int(input("Year - "))
    if (date < 1) or (date > 31) or (month < 1) or (month > 12) or (year < 1800) or (year > 2025):                  
        print("Please use the given conditions for entering the date\nC1 : 1<=month<=12\nC2 : 1<=date<=31\nC3 : 1800<=year<=2025")
        continue
    if month in (1, 3, 5, 7, 8, 10, 12):
      month_length = 31
    elif month == 2:
        if leap_year:
           month_length = 29
        else:
           month_length = 28
    else:
       month_length = 30
    if date < month_length:
      date += 1
    else:
      date = 1
    if month == 12:
        month = 1
        year += 1
    break
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, date))


   #3rd program
print('3rd program')
List= [5,34,21,37,68,11]
print('The list is')
print(List)
print('The resultant tuple is :')
Tuple = [(val, pow(val, 2)) for val in List]
print(Tuple)

   #4th program
print('4th program')
grade_point=int(input('enter grade point:'))
x='Error'
if grade_point==10:
  x='Your grade is A+ and Outstanding performance'
elif grade_point==9:
  x='Your grade is A and Excellent performance'
elif grade_point==8:
  x='Your grade is B+ and Very Good performance'
elif grade_point==7:
  x='Your grade is B and Good performance'
elif grade_point==6:
  x='Your grade is C+ and Average performance'
elif grade_point==5:
  x='Your grade is C and Below Average performance'
elif grade_point==4:
  x='Your grade is D and Poor performance'
else:
  x='Out of range'
print(x)

   #5th program
print('5th program')
n = 6
for i in range(n):
    # printing spaces
    for j in range(i):
        print(' ', end='')
    # printing alphabet
    for j in range(2*(n-i)-1):
        print(chr(65 + j), end='')
    print()

   #6th program
print('6th program')
dict1 = {}
while True:                                                                                                         
    name = input("Enter the name of the student: ")
    SID = int(input("Enter the SID of %s: " % name))
    dict1[SID] = name
    more_data = input("Do you want to enter more data? ")
    if more_data in ("N","n","No","no","NO"):
        break
print("\na. Student Details:")                                                                                      
for i in dict1:
    print("The SID of %s is %d" % (dict1[i],i))
dict2 = {}
for sorted_value in sorted(dict1.values()):                                                                         
    for key,value in dict1.items():
        if value == sorted_value:
            dict2[key] = value
print("\nb. Student Details sorted with respect to names:")                                                       
for i in dict2:
    print("The SID of %s is %d" % (dict2[i],i))
dict3 = {}
for sorted_key in sorted(dict1):                                                                                    
    for key,value in dict1.items():
        if key == sorted_key:
            dict3[key] = value
print("\nc. Student Details sorted with respect to SIDs:")                                                        
for i in dict3:
    print("The SID of %s is %d" % (dict3[i],i))
print("\nd. ", end="")                                                                                              
while True:
    search_SID = int(input("Enter the SID of the student: "))
    if search_SID in dict1:
        print("The name of student whose SID is %d is %s" % (search_SID,dict1[search_SID]))
        break
    else:
        print("The SID you entered isn't entered\nPlease enter a valid SID to be searched\nList of valid SIDs: %s\n" % list((dict1.keys())))
        continue

   #7th program
print('7th program')
Number = int(input("Enter the number of terms of the Fibonacci sequence:"))
def fib_iter(Number):
    a=1
    b=1
    if Number==1:
        print('0')
    elif Number==2:
        print('0','1')
    else:
        print("Iterative Approach: ", end=' ')
        print('0',a,b,end=' ')
        for i in range(Number-3):
            total = a + b
            b=a
            a= total
            print(total,end=' ')
        print()
        return b
         
fib_iter(Number)
First = 0
Second = 1
Sum = 0

for Num in range(0, Number):
    print(First, end = '  ')
    Sum = Sum + First
    Next = First + Second
    First = Second
    Second = Next
print("\nThe Sum of Fibonacci Series = %d" %Sum)
average=Sum/Number
print('Average is:',average)

   #8th program
print('8th program')
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}

symm_diff=Set1^Set2                        
print("a. Set with elements not common in both is:",symm_diff)

setonlyinone=Set1^Set2^Set3
print("b. Set of elements that is only present in one set is:",setonlyinone)

setonlyintwo=(Set1|Set2|Set3)- (Set1^Set2^Set3)-(Set1&Set2&Set3)               
print("c. Set of elements that is only present in two set is:",setonlyintwo)

new_set1=set()                                          
for n in range(1,11):
    new_set1.add(n)
notcommon=new_set1- Set1
print("d. Set of all integers in the range 1 to 10 that are not in Set1:",notcommon)

new_set2=set()                                               
for n in range(1,11):
    new_set2.add(n)
notcommon2=new_set2 - (Set1|Set2|Set3)
print("e. Set of all integers in the range 1 to 10 that are not in Set1 and Set2 and Set3:",notcommon2)

