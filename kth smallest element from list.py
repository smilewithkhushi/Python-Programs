'''
Given an array arr[] and an integer K where K is smaller than size of array,
the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.
Input:
N = 6
arr[] = 7 10 4 3 20 15
K = 3
Output : 7
Explanation :
3rd smallest element in the given 
array is 7.
'''


list=[7,10 ,4, 3,20,15]

k=int(input("Enter the value of k :"))

print("the list : ", list)
list.sort()
print("Kth smallest element from list :", list[k-1])
