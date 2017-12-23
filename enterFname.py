#entering file name
fname=input('eneter filename')
try:
    fhand= open(fname)
except:
    print('no file with such name exist,please try again',fname)
    exit()
count=0
for line in fhand:
    if line.startswith('Subject:'):
        count=count+1
print('there are subjects,',count,'in,',fname)
