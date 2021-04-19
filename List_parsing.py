#You will parse the From line using split() 
fname = input("Enter file name: ")
file = open(fname)
count = 0

for line in file:
    if not line.startswith("From"): continue # Pattern check
    xlist = line.split()
    if not len(xlist[0]) == 4: continue # Pattern check
    print(xlist[1])
    count += 1

print("There were", count, "lines in the file with From as the first word")