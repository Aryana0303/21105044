#Assignment4

   #1st program
print('1st program')
def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
         
n = 3
TowerOfHanoi(n, 'A', 'C', 'B')

   #2nd program
from math import comb
n = int(input("Enter the number of rows: "))                                          

print("The Pascal's Triangle using recursion is:")
def pascaltriangle(num):
    if num == 1:                                                                                        
        return [[1]]
    else:
        result = pascaltriangle(num-1)                                                                  
        current_row = [1]                                                                               
        previous_row = result[-1]                                                                       
        for i in range(len(previous_row)-1):                                                            
            current_row.append(previous_row[i] + previous_row[i+1])
        current_row += [1]                                                                              
        result.append(current_row)                                                                      
    return result
for i in pascaltriangle(n):
    print((n-len(i))*" ",end="")                                                                        
    for j in i:
        print(j, end =" ")
    print()

print("The Pascal's Triangle using iteration is:")
for i in range(n):                                                                                      
    print((n-i-1)*" ",end="")                                                                           
    for j in range(n):                                                                                  
        if comb(i,j) != 0:                                                                              
            print(comb(i,j),end=" ")                                                                   
    print()   

                
   #3rd program
print('3rd program')
val1 = int(input("Enter first integer value(dividend): "))
while True:                                                                                             
    val2 = int(input("Enter second integer value(divisor): "))
    if val2 != 0:
        break
    else:
        print("\nDivisor must not be 0\nPlease enter the divisor again")
result = divmod(val1,val2)
print("\nQuotient:",result[0],"\nRemainder:",result[1])

print("\na.")                                 
a_part = callable(divmod)
print(a_part, end="")
if a_part == True:
    print(", which means it is callable")
else:
    print(", which means it is not callable")

print("\nb.")                                            
if all(x != 0 for x in result):
    print("All values in result(i.e. quotient and remainder) are non-zero.")
else:
    print("All values in result(i.e. quotient and remainder) are not non-zero(i.e. one of them is 0).")

print("\nc.")                           
c_part = result + (4,5,6)
c_part_output = sorted(list((x for x in c_part if x>4)))
print("Values greater than 4(in list format) are:", c_part_output)

print("\nd.")                                            
d_part = set(c_part_output)
print("The output of previous part in set datatype would be:", d_part)

print("\ne.")                                                                  
e_part = frozenset(d_part)
print("The immutable set would be:", e_part)

print("\nf.")                     
f_part = max(e_part)
print("The maximum value from the set is:", f_part)
print("The hash value of %d(considering it to be integer) is %d and its hash value is %d(if we consider %s as a string)." % (f_part,hash(f_part),hash(str(f_part)),str(f_part)))



   #4th program
print('4th prgram')
class Student:                                                                                          
    def __init__(self,name,rno):
        self.name = name
        self.rno = rno
        print("Object Created")
    def __del__(self):
        print("Object destroyed")
name = input("Enter name of student: ").strip()                                                        
roll_no = int(input("Enter SID of %s: " % (name)))
student1 = Student(name,roll_no)                                                                        
print("The name of the student is %s and his/her roll number is %d" % (student1.name,student1.rno))     
del student1
print("")


   #5th program
print('5th program')
class Employee:                                                                                         
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        print("%s has a salary of %d rupees" % (name,salary))
    def __delete__(self,name):
        if hasattr(Employee,'self.name') == name:
            print(123)
        print("b. Record of %s deleted" % (self.name))

print("Details of Employees:")
employee1 = Employee("Mehak",40000)
employee2 = Employee("Ashok",50000)
employee3 = Employee("Viren",60000)


print("\na. Updated the salary of %s from %d to " % (employee1.name,employee1.salary), end = "")
employee1.salary = 70000
print(employee1.salary)

employee3.__delete__("Viren")
print("")



print("\na. Updated the salary of %s from %d to " % (employee1.name,employee1.salary), end = "")
employee1.salary = 70000
print(employee1.salary)

employee3.__delete__("Viren")
print("")



   #6th program
print('6th program')
word = input("Enter the first word: ")  #input from first friend

testword = input("\nEnter a new meaningful word to test your friendship: ")  #input from second friend

def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count

if count_in_dict(word) != count_in_dict(testword):
    print("The letters are not exact, friendship is fake!")
else:
    print("The letters are exact, friendship is not fake!")

