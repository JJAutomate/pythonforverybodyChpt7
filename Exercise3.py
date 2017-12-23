fname=input('enter filename:')
if fname=='na na boo boo':
    print('NA NA BOO BOO TO YOU- YOU HAVE BEEN PUNKED!')
    exit()
try:
    fhand= open(fname)
except:
    print('no file with such name exist,please try again',fname)
    exit()
count=0
#avrg=0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        #avrg=
        count=count+1
        print(line)
print('there are subjects,',count,'in,',fname)
