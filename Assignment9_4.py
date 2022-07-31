# Q.4.Write a program which accept two file names from user and compare contents of both the
# files. If both the files contains same contents then display success otherwise display failure.
# Accept names of both the files from command line.
# Input : Demo.txt Hello.txt
# Compare contents of Demo.txt and Hello.txt
import sys

def FileD(name1,name2):
    with open(name1,'r') as f1:
        with open(name2,'r') as f2:
            d1 = f1.readlines()
            d2 = f2.readlines()
            if d1 == d2:
                return True
            else:
                return False
                            
def main():
    File1 = sys.argv[1]
    File2 = sys.argv[2]
    
    ret = FileD(File1,File2)
    if ret == True:
        print("Success")
    else:
        print("Failure")
        
if __name__ == "__main__":
    main()