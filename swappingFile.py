def swapfileData () :
    file1 = input("Enter the file name :-")
    file2 = input("Enter the file name :-")
    numberOfWords = 0 
    f = open(file1 , "r")
    f = open(file2 , "r+")
    write1 = open(file1 , "w")
    write1.write(file2)
    write2 = open(file2, "w+" )
    write2.wtite(file1)
    fileLines = f.readlines()
    for line in file1 :
        words = line.split()
        numberOfWords = numberOfWords + len(words)
        print("Number of words :- ")
        print(numberOfWords)
    for line in file2 :
        words = line.split()
        numberOfWords = numberOfWords +len(words)
        print("Number of words :-")
        print(numberOfWords)
swapfileData()