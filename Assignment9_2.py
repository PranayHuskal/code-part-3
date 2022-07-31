# Q.2. Write a program which accept file name from user and open that file and display the contents of that file on screen.
#  Input : Demo.txt
#  Display contents of Demo.txt on console.

import os
def Check(fn):
    f=open(fn,mode='r')
    a=f.read()
    print(a)
    
def main():
    file_name= input('Enter File name: ')
    Check(file_name)

if __name__ == "__main__":
    main()

