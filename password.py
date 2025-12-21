# '''User is given 3 chances to enter correct password. If more than 3 than tell the user that account blocked'''

attempts = 0
while True:
    pwd = input("Enter password: ")
    attempts += 1
    if pwd == "admin123":
        print("Access Granted")
        break
    if attempts >= 3:
        print("Too many attempts. Try later.")
        break
