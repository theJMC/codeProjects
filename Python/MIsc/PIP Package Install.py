import pip

def packageInstall():
    selection = input("What PIP Package would you like to install? ")
    pip.main(['install', selection])

if __name__ == "__main__":
    packageInstall()