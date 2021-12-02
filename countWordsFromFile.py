def countWordFromFile():
  fileName=input("Enter the file name: ")
  numberOfWords = 0
  file = open(fileName,'r')
  for line in file:
    words=line.split()
    print(words)
  print("Nunber of Words: ")
  print(numberOfWords)

countWordFromFile()

