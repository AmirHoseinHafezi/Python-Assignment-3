reportThePolice = 4321
password = 1234
numberOfAttempts = 3
while numberOfAttempts > 0:
    userPass = int(input("Enter the password: "))
    if userPass // 10000 != 0 or userPass <= 999:
        continue
    elif userPass == password :
        print("Entered.")
        break
    elif userPass == reportThePolice:
        print("Is the card yours!!!?\nIt was reported to the police.")
        break
    else:
        print("The password is wrong!")
        numberOfAttempts -= 1
if numberOfAttempts == 0:
    print("The account was locked.")