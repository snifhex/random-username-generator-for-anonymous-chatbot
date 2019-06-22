import os
import csv
import random

def generatorCore():
    nameList = []
    while True:
        randomName = ''
        randomName = ''.join([randomName+chr(random.randrange(97,123)) for i in range(6)])
        if not randomName in nameList:
            print(randomName)
            csv_writer(randomName)
            

def csv_writer(name):
        if os.path.isfile('names.csv'):
            with open('names.csv', 'a') as doc:
                writer = csv.writer(doc)
                writer.writerow((name,))
        else:
            with open('names.csv', 'w') as doc:
                writer = csv.writer(doc)
                writer.writerow(('name',))

def main():
    generatorCore()

if __name__ == '__main__':
    main()


