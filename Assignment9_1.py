#Q.1.Write a program which accepts file name from user and check whether that file exists in current directory or not.
# Input : Demo.txt
# Check whether Demo.txt exists or not.

import os
def Check(fn):
    if os.path.exists(fn):
        f=open(fn)
        print('File Exists')
        f.close()
    else:
        print('File not Exists')
        
        
def main():
    file_name= input('Enter File name: ')
    Check(file_name)

if __name__ == "__main__":
    main()

