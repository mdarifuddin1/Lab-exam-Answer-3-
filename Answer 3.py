
# My id 193027042



# Answer 3

def find(list1, list2, n, m):


	s = dict()
	for i in range(m):
		s[list2[i]] = 1


	for i in range(n):
		if list1[i] not in s.keys():
			print(list1[i], end = " ")

list1 = [ 1, 5, 6, 7 ]
list2 = [ 4,5,6 ]
n = len(list1)
m = len(list2)
find(list1, list2, n, m)
def kthlargest(arr, n, k):
 
   
    arr.sort()
 
    return arr[k]


if __name__=='__main__':
    arr = [5, 1, 7, 3, 9, 11, 10, 4]
    n = len(arr)
    k = 4
    print("K'th k-th largest number is",
         kthlargest(arr, n, k))
 

NA = -1

def moveToEnd(mPlusN, size):

	i = 0
	j = size - 1
	for i in range(size-1, -1, -1):
		if (mPlusN[i] != NA):

			mPlusN[j] = mPlusN[i]
			j -= 1




def merge(mPlusN, N, m, n):

	i = n
	j = 0
	k = 0
	while (k < (m+n)):

		
		if ((j == n) or (i < (m+n) and mPlusN[i] <= N[j])):

			mPlusN[k] = mPlusN[i]
			k += 1
			i += 1

		else: 

			mPlusN[k] = N[j]
			k += 1
			j += 1




def printArray(arr, size):

	for i in range(size):
		print(arr[i], " ", end="")

	print()



mPlusN = [2, 8, NA, NA, NA, 13, NA, 15, 20]
N = [5, 7, 9, 25]
n = len(N)

m = len(mPlusN) - n


moveToEnd(mPlusN, m+n)


merge(mPlusN, N, m, n)


printArray(mPlusN, m+n)


