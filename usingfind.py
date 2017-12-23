fhand=open('mbox-short.txt') #to find a string in a line or lines
for line in fhand:
    line=line.rstrip()
    if line.find('@uct.ac.za')==-1:  continue
    print(line)
