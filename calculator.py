number1=int(input("enter a number1:"))
number2=int(input("enter a number2:"))
operator=input("enter operator:")
if operator=="+":
    answer=number1+number2
    print(f"the answer is: {answer}")
elif operator=="-":
    answer=number1-number2
    print(f"the answer is: {answer}")
elif operator=="*":
    answer=number1*number2
    print(f"the answer is: {answer}")
elif operator=="/":
    answer=number1/number2
    print(f"the answer is: {answer}")
else:
    print("invalid operator")
    print("operators must be '+','-','*','/'")
