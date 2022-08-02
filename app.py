#app idea?
numOne = int(input("Enter number one: "))
operator = input("Enter Operator: ")
numTwo = int(input("Enter number two: "))




def calculator(numOne, numTwo, operator):
  if(operator == "+"):
    return numOne + numTwo
  
  if(operator == "-"):
    return numOne - numTwo
  
  if(operator == "*"):
    return numOne * numTwo
  
  if(operator == "/"):
    return numOne / numTwo
  
print(calculator(numOne,numTwo,operator))  
  






#hello