import random


file = open("name.txt", "a+")
nameList = []

try:
    while True:
        randomName= ''
        for i in range(6):
            word=random.randrange(97,123)
            randomName = randomName+chr(word)
        if not randomName in nameList:
            print (randomName)
            file.write(randomName+"\n")
except:
    file.close()

file.close()
