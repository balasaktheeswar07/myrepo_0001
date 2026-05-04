def addition(a,b):
    return a+b
def subraction(a,b):
    return a-b
def division(a,b):
    if b==0:
        return "Error: cannot divide by zero."
    return a/b
def multiplicaation(a,b):
    return a*b
def modulo(a,b):
    return a%b
def power(a,b):
    return a**b
def getnum(prompt):
    while 1:
        try:
            return float(input(prompt))
        except ValueError:
            print ("Please enter a valid number")

def calculator():
    operations={
        "1" : ("addition",addition),

        "2" : ("Subract",subraction),
        "3" : ("Multiply",multiplicaation),
        "4" : ("modulo",modulo),
        "5" : ("Divide",division),
        "6" : ("power",power),
        }
    while 1:
        print("calculator")
        for key, (name,_) in operations.items():
            print(f"{key}.{name}")
        print("7.EXIT")
        choice=input("choose an operation")
        if(choice =="7"):
           print("exiting :) .........")
           break
        if choice not in operations:
            print("Invalid choice, thank you dont try again,")
            continue

        fn=getnum("enter first number")
        sn=getnum("enter second number")
        operation_name, operation = operations[choice]
        result = operation(fn, sn)
        print(f"{operation_name} result: {result}")


if __name__ == "__main__":
          calculator()
