from os import listdir
from sys import argv

def main(dir):
	files = listFiles(dir)
	counter=0
	for file in files:
		if testLine(dir+file,4):
			counter +=fixLine(dir+file,4)
	print counter, "files edited"

def listFiles(dir):
    return listdir(dir)

def testLine(file,line):
    f = open(file,'r')
    text=f.readlines()
    f.close()
    if text[line] == 'Sex: N\n':
        return True
    return False

def fixLine(file,line):
    f=open(file)
    text=f.readlines()
    f.close()
    text[line] = 'Sex: M\n'
    g=open(file,'w')
    for inf in text:
        g.write(inf)
    g.close()
    return 1

main(argv[1])
