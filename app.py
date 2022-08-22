from flask import Flask, request, render_template
from re import search
app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'] )
def main():
  numOne = request.form.get('numOne',0)
  numTwo = request.form.get('numTwo',0)
  operator = request.form.get('operator','')
  result = ''
  if(operator == "+"):
    result =  numOne + numTwo
  
  if(operator == "-"):
    result = numOne - numTwo
  
  if(operator == "*"):
    result = numOne * numTwo
  
  if(operator == "/"):
    result = numOne / numTwo
  
  
  

  return render_template('main.html', result = result)
  
  