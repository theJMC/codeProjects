import login as l  

usernames = ["root", "James", "User"]
passwords = ["toor", "123456", "Password"]

result = l.Login(usernames, passwords)

if result == 1:
    print("\nHaha It Works It Actually Works!!")
else:
    print("\nWASNT THAT EASY HAHAHAHAH")