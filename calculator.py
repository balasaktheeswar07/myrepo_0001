print("add and subract numbers:")
print("addition",13+424)
print("subraction",32-23)
print("multiply",23*3)
print("division",34/2)
print("floor division",34//5)                                       
print("modulus",23%4)
print("exponent",2**3)
print("operator precedence",3+4*5)
print("using parenthesis to change precedence",(3+4)*5)

print("calculate the area of a rectangle with length 5 and width 3:")
length = 5
width = 3
area = length * width                           
print("area =", area)
print("-----------------------------------------------------------------")
print("calculate the perimeter of a rectangle with length 5 and width 3:")
perimeter = 2 * (length + width)        
print("perimeter =", perimeter) 

print("calculate the area of a circle with radius 7:")      
import math
radius = 7      
area_circle = math.pi * radius**2
print("area of circle =", area_circle)
print("______________________________________________________________________")
print("calculate the circumference of a circle with radius 7:")

circumference = 2 * math.pi * radius
print("circumference =", circumference)
print("calculate the average of three numbers 10, 20, and 30:")
num1 = 10   
num2 = 20   
num3 = 30       
average = (num1 + num2 + num3) / 3
print("average =", average)
print("calculate the simple interest for a principal of 1000, rate of 5%, and time of 3 years:")
principal = 1000
rate = 5
time = 3
simple_interest = (principal * rate * time) / 100
print("simple interest =", simple_interest)
print("calculate the compound interest for a principal of 1000, rate of 5%, time of 3 years, compounded annually:")
principal = 1000
rate = 5 / 100
time = 3
compound_interest = principal * (1 + rate)**time - principal
print("compound interest =", compound_interest)     
print("calculate the factorial of 5:")
factorial = 1
for i in range(1, 6):
    factorial *= i
print("factorial of 5 =", factorial)
print("calculate the power of 2 raised to 8:")
power = 2**8
print("2 raised to 8 =", power)
print("calculate the square root of 144:")
square_root = math.sqrt(144)
print("square root of 144 =", square_root)  
print("calculate the distance between two points (3,4) and (7,1):")
x1, y1 = 3, 4
x2, y2 = 7, 1
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("distance =", distance)
