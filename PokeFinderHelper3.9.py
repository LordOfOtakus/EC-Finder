import sys
import os
import math

firstLine = True
dds = False
wurmple = False
columns = []
mark = False
while True:
    print("Are you looking to predict the evolution of Dunsparce (1), Wurmple (2), or just Jumbo / Teensy Marks? (3)")
    pokemon = input("Please input a number for your selection. ")

    if pokemon == "1":
        print("Three-Segment Dudunsparce selected.")
        dds = True
        break
    
    elif pokemon == "2":
        print("Wurmple evolutions selected.")
        wurmple = True
        break
    
    elif pokemon == "3":
        mark = True
        break
    
    else:
        print("Incorrect selection, please try again.")

while mark != True:
    size = input("Are you interested in Jumbo / Teensy Marks for your Dunsparce or Wurmple? (y/n) ")

    if size == "y":
        mark = True
        print(mark)
        break
    elif size == "n":
        break
    else:
        print("That's not yes or no!")

while True:
    file = input("Provide a file exported from PokeFinder to be read. ")
    file = file.strip("'")
    #print(file)

    if os.path.isfile(file):
        print("File found! Proceeding...")
        break
    else:
        print("File not found, please check the path provided and try again.")

f = open(file, "r")

columns += ["Advances"]
#print(columns)
colNum = 1

#print('{:<10s}{:>10s}'.format(columns[0], columns[1]))
index = 0
indexEC = 0
indexHeight = 0
ivIndex = 8
for x in f:
    if firstLine:
        y = x.split()
        #print(y)
        for i in y:
            #print(i)
            if i == "EC":
                if (dds == True or wurmple == True):
                    columns += ["EC"]
                    colNum += 1
                    indexEC = index - 1
  
            elif i == "Height":
                if mark:
                    columns += ["Height"]
                    #print(columns)
                    colNum += 1
                    #print(colNum)
                    indexHeight = index
                    #print(indexHeight)

            index += 1

        if len(columns) == 2:
            print('{:<10s}{:>10s}'.format(columns[0], columns[1]))
        else:
            print('{:<10s}{:>10s}{:>10s}'.format(columns[0], columns[1], columns[2]))
        
        firstLine = False
        continue

    #print(len(y))
    #print(index)

    y = x.split()

    while (y[ivIndex].isdigit() != True):
        #print(y[ivIndex].isdigit())
        indexHeight += 1
        ivIndex += 1

    #print(len(y))

    if dds:
        #print(indexEC)
        EnC = y[indexEC]
        if int(EnC, 16) % 100 != 0:
            continue

    if wurmple:
        EnC = int(y[indexEC], 16)
        #print(math.floor(EnC/65536))
        if (math.floor(EnC/65536) % 10) <= 4:
            EnC = "Silcoon"
        else:
            EnC = "Cascoon"

    if mark:
        #print(indexHeight)
        #print(y[indexHeight])
        Height = int(y[indexHeight])
        if Height % 255 != 0:
            continue
            #z = y[0] + "        " + str(Height)
            #print(z)
        if (dds != True and wurmple != True):
            EnC = Height

    #print('{:<10s}{:>10s}'.format(y[0], str(Height)))
    
    if len(columns) == 2:
        print('{:<10s}{:>10s}'.format(y[0], str(EnC)))
    if len(columns) == 3:
        print('{:<10s}{:>10s}{:>10s}'.format(y[0], str(EnC), str(Height)))

f.close