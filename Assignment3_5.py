
#Q.5 Write a program which accept N numbers from user & store it into list. return addition of all prime numbers from list. 
#    main python file aaccepts N numbers from user and pass each number of primeadd() function which is part of our user defined module
#    named as 'p'.name of the function from main python file should be listPrime().

import p                                                 # module import p.py file.
def main():
	ls = []
	size = int(input("Enter number of elements:"))
	for i in range(size):
		element = int(input(f"Enter {i+1}element:"))
		ls.append(element)
	print(ls)

	print(f"Addition of prime numbers is:",p.primeadd(ls))

main()