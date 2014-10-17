
file = open('a.txt','r')
lines = file.readlines()
newList = []

for i in lines:
	newList.append(int(i))

for j in newList:
	print j

file.close()
