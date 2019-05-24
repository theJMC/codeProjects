
attempt = 0
while attempt < 3:
    code = input("Please enter the product code: > ")
    if code == "abcdef":
        print("Grey Socks")
        break
    else:
        print("Product Code Incorrect")
        attempt += 1

        