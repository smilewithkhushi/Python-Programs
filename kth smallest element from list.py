list=[5,83,23,45,23,54,12,2]

k=int(input("Enter the value of k :"))

print("the list : ", list)
list.sort()
print("Kth smallest element from list :", list[k-1])