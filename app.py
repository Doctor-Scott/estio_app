from flask import Flask, request, render_template
from re import search
app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'] )
def main():
 if(operator == "+"):
    return numOne + numTwo
  
  if(operator == "-"):
    return numOne - numTwo
  
  if(operator == "*"):
    return numOne * numTwo
  
  if(operator == "/"):
    return numOne / numTwo
  
  
  

    return render_template('main.html', )
  
  