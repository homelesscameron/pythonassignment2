password = "1234"

i = 0

def myfunction():
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