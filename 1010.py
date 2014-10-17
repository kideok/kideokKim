
# def bubbleSort(a) :
# 	count = 1;
# 	for i in range(0,len(a)):
# 		for j in range(i+1,len(a)):
			
# 			if(count % 10 == 1 and count % 100 != 11) :
# 				print count,"(st comparison)"
# 			elif(count % 10 == 2 and count % 100 != 12) :
# 				print count,"(nd comparison)"
# 			else :
# 				print count,"(th comparison)"

# 			print a[i],"(",i,") and ",a[j],"(",j,") comparison";	

# 			if(a[i] > a[j]) : 
# 				temp = a[i];
# 				a[i] = a[j];
# 				a[j] = temp;
# 			count= count +1;	

			
# 	return a;

# A = [53,15,3,55,91,28,47,66,78,29,55,88,40,43,69];
# B = bubbleSort(A);

# for i in range(0,len(B)):
# 	print B[i];


count = 0

def quickSort(a) :
	global count
	print count, a, len(a)
	count = count +1
	if len(a) > 1 :
		left = list()
		right = list()
		pivotList = list()
		pivot = a[0]
		for i in range(0,len(a)):
			if(pivot > a[i]) :
				left.append(a[i])
			elif(pivot < a[i]) :
				right.append(a[i])
			else :
				pivotList.append(a[i])

		return quickSort(left)+pivotList+quickSort(right)	
	else : 
		return a

#A = [6,2,3,9,7,8,1,4,5]
A = [1,2,3,4]
B = quickSort(A)
print count,"Call!"
for i in range(0,len(B)):
 	print B[i]

 	