
def quickSort(q):
    if len(q) == 1:
        return q;
    elif len(q) >= 2:
        less = list();
        greater = list();

        if len(q) % 2 == 0:
            pivot = q[len(q)/2 - 1];
        else:
            pivot = q[len(q)/2];

        for i in q:
            if i < pivot:
                less.append(i);
            elif i > pivot:
                greater.append(i);


        return merge(quickSort(less),pivot,quickSort(greater))

def merge(list1,mid,list2):
    newlist = list()
    if not list1 and list2:
        newlist.append(mid)
        newlist.extend(list2)
    if not list2 and list1:
        newlist.extend(list1)
        newlist.append(mid)
    if list1 and list2 :
        newlist.extend(list1)
        newlist.append(mid)
        newlist.extend(list2)
    return newlist


A = [45,20,21,50,10,8,9,7,10];
B = quickSort(A);


for i in range(0,len(B)):
	print B[i];



# number = 0;

# if(number == 0):
# 	print "Zero"
# elif(number % 2 ) == 1:
# 	print "Odd"
# else:
# 	print "Even"
# def bubbleSort(a) :
# 	for i in range(0,len(a)):
# 		for j in range(i+1,len(a)):
# 			if(a[i] > a[j]) :
# 				temp = a[i];
# 				a[i] = a[j];
# 				a[j] = temp;
# 	return a;

# A = [45,20,21,50,10,8,9,7,10];
# B = bubbleSort(A);

# for i in range(0,len(B)):
# 	print B[i];