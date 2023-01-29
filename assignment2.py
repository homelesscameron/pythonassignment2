import os
os.system('cls')

password = "1234"

for i in range (3, 0, -1):
    attempt = input ("enter password: ")
    if attempt == password:
        break
    else:
        print ("incorrect password")
if i == 1:
    print ("denied access")
else:
    print("accepted")

print("********************************")
print("********maths calculator********")
print("********************************")

num = int(input("first number: "))
secondnum = int(input("second number: "))

print(f"your first number is {num}")
print(f"your second number is {secondnum}")

x = pow(num, secondnum)

print()
print(x, "is the power of both numbers")
print()
print(max(num, secondnum), "is greater")
print()
print(min(num, secondnum), "is lesser")
print()
print("thank you for this maths calculator")
print()