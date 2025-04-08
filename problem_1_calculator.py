from testhelper import test

input1 = int(input("Give me a number: "))
operator = input("Give me an operator: ")
input2 = int(input("Give me a number: "))

if operator == "+":
    output = input1 + input2
if operator == "-":
    output = input1 + input2
if operator == "*":
    output = input1 * input2
if operator == "/":
    output = input1 / input2

print(output)