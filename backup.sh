a = float(input("Enter the first number: "))
c = str(input("Enter the action (+, -, /, *): "))
b = float(input("Enter the second number: "))

if c == "+":
	d = a + b
	print ("Answer is: " + str(int(d)))
elif c == "-": #Compare the variable for further action
	d = a - b
	print ("Answer is: " + str(int(d)))
elif c == "/":
	d = a / b
	print ("Answer is: " + str(d))
elif c =="*":
	d = a * b
	print ("Answer is: " + str(int(d)))