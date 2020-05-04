#Python quiz

q1 = """\n1.What is the output of the following code?
print(var[2::-1])

Options Are:

1.Jam
2.dno
3.maJ
4.dnoB semaJ
*************************************************"""

q2 = """\n2.What is the output of the following code

sampleSet = {"Jodi", "Eric", "Garry"}
sampleSet.add(1, "Vicki")
print(sampleSet)

Options Are:

1.{‘Vicki’, ‘Jodi’, ‘Garry’, ‘Eric’}
2.{‘Jodi’, ‘Vicki’, ‘Garry’, ‘Eric’}
3.{‘1’, ‘Vicki’, ‘Garry’, ‘Eric’}
4.The program executed with error

*************************************************"""

q3 = """\n3.Which operator has higher precedence in the following list

Options Are:

1.% Modulus
2.& BitWise AND
3.**, Exponent
4.> Comparison

*************************************************"""

q4 = """\n4.What is the output of the following code?
var1 = 1
var2 = 2
var3 = "3"

print(var + var2 + var3)

1.6
2.33
3.123
4.Error. Mixing operators between numbers and strings are not supported

*************************************************"""

q5 = """\n5.What is the output of the following code

salary = 8000

def printSalary():
  salary = 12000
  print("Salary:", salary)
  
printSalary()
print("Salary:", salary)

1.Salary: 12000 Salary: 8000
2.Salary: 8000 Salary: 12000
3.The program failed with errors
4.None

*************************************************"""

print("************************************************************")
print("*                    WELCOME TO PYTHON QUIZ                *")
print("************************************************************")

questions = {q1:"3",q2:"4",q3:"3",q4:"4",q5:"1"}

score = 0

Your_Name = input("\nEnter youtr name :")
for i in questions:
    print(i)       #It gives the questions with options
    answer = int(input("enter the answer(1/2/3/4):"))

    if answer==questions[i]: #compares user input answer with valus() of questions
        print("It is correct option")
        print("************************************************")
        score= score + 1
    elif answer!=questions[i]:
        print("it is not a correct option")
        print("************************************************")
    else:
        print("Given input is wrong, pls provide proper input")
        
print("Final Score is :",score)
    

        
    

    





