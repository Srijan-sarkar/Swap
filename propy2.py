def swapFile():
    f1 = input("Enter Name of first file")
    f2 = input("Enter Name of second file")


    with open(f1, 'r') as a:
        dataOfFile1= a.read()

    with open(f2, 'r') as b:
        dataOfFile2= b.read()

    with open(f1, 'w') as a:
        a.write(dataOfFile2)

    with open(f2, 'w') as b:
        b.write(dataOfFile1)


swapFile()