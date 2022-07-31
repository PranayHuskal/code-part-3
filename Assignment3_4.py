
#Q.4 Write aprogram which accept N numbers from user & store it into list, return addition of all elements of list,accept another
#    number from user & return frequency of that number from list.

a=[]
n=int(input("Enter number of elements: "))
for i in range(n):
	a.append(int(input("enter element: ")))
f=int(input("enter number: "))
count=0
for i in range(n):
	if (a[i])==f:
		count+=1
print("Frequency=", count)

