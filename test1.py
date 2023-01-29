password = "1234"

login = True

def myfunction():
    for i in range (3, 0, -1):
        attempt = input ("enter password: ")
        if attempt == password:
            break
        else:
            print ("incorrect password")
    if login == 1:
        print ("denied access")
    else:
        print("accepted")