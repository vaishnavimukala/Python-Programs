actual_username="asdf1234"#default username
actual_password="qwer1234"#default password
for i in range(1,4):
    username=input("enter username:")
    password=input("enter password:")
    if username==actual_username and password==actual_password:
             print("Loggin successfull!!")
             break
    else:
        print("Incorrect un and pw")
else:
    print("Account blocked!!!")
    print("Try after 24hours.....")
