real_pwd = "daxesh1234"
password = ''
while password != real_pwd:
    password = input("Enter the password")
    if password == real_pwd:
        print("you are logged in")
    else:
        print("something wrong")
