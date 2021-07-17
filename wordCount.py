def countWordsFromFile():
    fileName = input("Please enter file name:")
    numberOfWords = 0
    f=open(fileName,'r')

    for line in f:
        words = line.split()
        numberOfWords = numberOfWords + len(words)
    print("number of words:")
    print(numberOfWords)

countWordsFromFile()
