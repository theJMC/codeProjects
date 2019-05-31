import pip

def install(package):
    if hasattr(pip, 'main'):
        #pip.main(['install', package])
        pass
    else:
        pip._internal.main(['install', package])

def main():
    print("Installing required modules...")
    try:
        install("columnar")
    except Exception as e:
        print("An error has occured installing Columnar. Program now quitting...\nError: " + e)
        input("Press enter to continue...")
    try:
        install("requests")
    except Exception as e:
        print("An error has occured installing Requests. Program now quitting...\nError: " + e)

if __name__ == "__main__":
    main()