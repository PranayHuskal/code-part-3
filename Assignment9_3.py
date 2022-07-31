# Q.3.Write a program which accept file name from user and create new file named as Demo.txt and
# copy all contents from existing file into new file. Accept file name through command line
# arguments.
# Input : ABC.txt
# Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt
import sys
def file(f):
    f1=open(f,mode='r')
    f2=open('student.txt',mode='a')
    
    for i in f1:
        f2.write(i)
    f1.close()
    f2.close()
    print('Print Successfully')
def main():
    FileName = sys.argv[1]
    file(FileName)
if __name__ == "__main__":
    main()
