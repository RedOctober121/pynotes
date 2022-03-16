run = True

while run is True:
    L = input("\n You: ")
    
    file1 = open('savdata.txt', 'a')
    file1.writelines(L)
    file1.writelines("\n")
    file1.close()

    file1 = open('savdata.txt', 'r')
    print("\nOutput of Readlines after appending\n\n")
    print(file1.read())
    print()
    file1.close()
    run = False
