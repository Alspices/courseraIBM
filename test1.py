while True:
    try:
        var = input("what is the file name?")
        with open(var) as fob:
            var = fob.read()
            print(var)
            break
    except FileNotFoundError:
        print("Sorry")
