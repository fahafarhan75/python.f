number=input("enter a number")
number=int(number)
print(f"the square of {number} is {number**2}")

age=12
print(type(age))
name="faha"
print(type(name))
height=5.5
print(type(height))
is_greater=5>9
print(type(is_greater)) 

number1=int(input("enter a number"))
number2=int(input("enter a number"))
addition=(number1+number2)
print(f"addition:{addition}")
subtraction=(number1-number2)
print(f"subtraction:{subtraction}")
multiplication=(number1*number2)
print(f"multiplication:{multiplication}")
division=(number1/number2)
print(f"division:{division}")

celsius=float(input("enter the temperatue in celsius"))
fehrenheit=(celsius *9/5) + 32
print(f"{celsius}°C is equal to {fehrenheit}°F")