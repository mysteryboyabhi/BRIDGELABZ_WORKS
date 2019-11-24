
def insert_sort(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

n=int(input("Enter the length of array: "))
arr=[]
for i in range(n):
    arr.append(int(input(f"Enter the {i}th element: ")))
print(insert_sort(arr))
