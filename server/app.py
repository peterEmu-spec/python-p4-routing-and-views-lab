#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# 1️⃣ Index route
@app.route("/")
def index():
    # Displays title in h1 for browser and test
    return "<h1>Python Operations with Flask Routing and Views</h1>"

# 2️⃣ Print string route
@app.route("/print/<string:param>")
def print_string(param):
    print(param)  # prints to console
    return param  # plain text for test compatibility

# 3️⃣ Count route
@app.route("/count/<int:number>")
def count(number):
    # Numbers separated by newline, include trailing newline
    numbers = "\n".join(str(i) for i in range(number)) + "\n"
    return numbers

# 4️⃣ Math route
@app.route("/math/<num1>/<operation>/<num2>")
def math(num1, operation, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)

        if operation == "+":
            result = num1 + num2
            if result.is_integer():
                result = int(result)
        elif operation == "-":
            result = num1 - num2
            if result.is_integer():
                result = int(result)
        elif operation == "*":
            result = num1 * num2
            if result.is_integer():
                result = int(result)
        elif operation == "div":
            if num2 == 0:
                return "Error: Division by zero"
            result = num1 / num2  # always float
        elif operation == "%":
            if num2 == 0:
                return "Error: Modulo by zero"
            result = num1 % num2
            if result.is_integer():
                result = int(result)
        else:
            return "Invalid operation. Use +, -, *, div, or %."

        return str(result)

    except ValueError:
        return "Error: num1 and num2 must be numbers"
