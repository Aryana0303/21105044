#Assignment 1

      #1st program
print("1st program")
numb1=int(input("enter first number"))
numb2=int(input("enter second number"))
numb3=int(input("enter third number"))
avg=(numb1+numb2+numb3)/3
print("avg is:",avg)

     #2nd program
print("2nd program")
rate = 0.20
standard_deduction = 10000
dependent_deduction = 3000
gross_income = float(input("\nEnter your gross income : "))
number_of_dependents = int(input("Enter number of dependents : "))
taxable_income = round(gross_income-standard_deduction-(dependent_deduction*number_of_dependents), 1)
tax = taxable_income*rate
if tax <0 :
    tax = 0
print("Your tax is $",tax,"\n")


     #3rd program
print(" 3rd program ")
print("Student=(SID, Name, Gender, Dept. name, CGPA")
student=(21105044, 'Aryana', 'F','ECE',8.5)
print("student=",student)

    #4th program
print(" 4th program" )
print("Marks of five students")
Marks= [89,53,18,45,56]
print("List before sorting",Marks)
Marks.sort()
print("List after sorting",Marks) 
   
   #5th program
print(" 5th program" )
color=['Red','Green','White','Black','Pink','Yellow']
color.pop(3)
print(color)
color.pop(3)
print(color)
color.insert(3,'Purple')
print(color)



