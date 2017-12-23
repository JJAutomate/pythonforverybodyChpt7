fhand = open('mbox-short.txt') #to find a string begining with 
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
