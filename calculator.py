logo="""
_____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}

def calculator():
    print(logo)
    num1=float(input("Enter first number:"))
    should_continue=True
    while should_continue:
        for symbol in operations:
            print(symbol)
        operand=input("Enter the operations:")
        num2=float(input("Enter the next number:"))
        answer=operations[operand](num1,num2)
        print(f"{num1} {operand} {num2} = {answer}")

        choice=input(f"Type 'y' to continue calculating {answer},or type 'n' to calculate from start:")
        if choice=="y":
            num1=answer
        
        else:
            should_continue=False
            print("\n"*30)
            calculator()

calculator()





