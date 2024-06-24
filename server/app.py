#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_string(text):
    print(text)
    return f'<h1>hello {text}</h1>'
    
@app.route('/count/<int:integer>') 
def count(integer):
    numberRange = []
    for i in range(integer):
        i + 1
        numberRange.append(i)
    return numberRange
        
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
     total = num1 + num2
    elif operation == '-':
     total = num1 - num2 
    elif operation == '*':
     total = num1 * num2
    elif operation == 'div':
          total = num1 / num2
    elif operation == '%':
     total = num1 % num2
    else:
     total = ''
    
    return str(total)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
