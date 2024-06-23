import sys

firstLine = True
if (len(sys.argv)) == 1:
    #file = input("No file provided. Please provide a text file pulled from PokeFinder. ")
    print("A file was not provided. Please provide a text file pulled from PokeFinder as an argument. ")
    sys.exit()
else:
    file = sys.argv[1]

f = open(file, "r")
print("Advances     EC      EC in Decimal")

for x in f:
    if firstLine:
        firstLine = False
        continue
    y = x.split()
    EC = int(y[1], 16)
    if EC % 100 == 0:
        z = y[0] + "    " + y[1] + "    " + str(EC)
        print(z)

f.close