

# Function to add two number
def add(num1,num2):
    return num1+num2  

#function to substract 2 number
def substract(num1,num2):
    return num1-num2

# function to multiply 2 numbers
def multiply(num1,num2):
    return num1*num2

# function to divide 2 numbers
def division(num1,num2):
    return num1/num2

# 3function  for average of two numbers
def avg(num1,num2):
    return (num1+num2)/2

# step 2 :user input

print("plesase select a operation:\n"
      "1.addition\n"\
      "2.substraact\n"\
      "3.multiply\n"\
      "4.division\n"\
      "5.average\n")

select =int( input("select a operation from 1,2,3,4,5:"))

number1 = int(input("enter 1st number:"))
number2 = int(input("enter number 2:"))  

# step 3 : print the result

if select ==1:
    print(number1,"+",number2,"=",\
          add(number1,number2))
    
elif select ==2:
    print(number1,"-",number2,"=",\
          substract(number1,number2))
        
elif  select ==3:
    print(number1,"*",number2,"=",\
          multiply(number1,number2))   
     
elif select ==4:
    print(number1,"/",number2,"=",\
          division(number1,number2))    

elif    select ==5:
    print(number1,"+",number2,"=",\
          avg(number1,number2))   
else:
    print("invalid operations pls select again!")    