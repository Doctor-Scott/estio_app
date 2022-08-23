from calculator import calculate
from flask import Flask, request, render_template
from re import search
app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'] )
def main():
  numOne = int(request.form.get('numOne',0))
  numTwo = int(request.form.get('numTwo',0))
  operator = request.form.get('operator','')
  result = ''
  
  if operator != '':
    result = calculate(numOne, numTwo, operator)
  
  return render_template('main.html', result = result)

  