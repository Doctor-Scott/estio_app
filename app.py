def calculator(numOne, numTwo, operator):
    if(operator == "+"):
      return numOne + numTwo
    
    if(operator == "-"):
      return numOne - numTwo
    
    if(operator == "*"):
      return numOne * numTwo
    
    if(operator == "/"):
      return numOne / numTwo




while 1 == 1:
  numOne = int(input(':'))
  if numOne == 'x':
    break
  
  operator = input(':')
  if operator == 'x':
    break
  
  numTwo = int(input(':'))
  if numTwo == 'x':
    break

  print(f"{numOne} {operator} {numTwo} = {calculator(numOne,numTwo,operator)}")  
    



#hello