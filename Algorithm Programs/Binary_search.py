def bin_search(arr, num):
    n=len(arr)
    arr=sorted(arr)
    print(arr)
    if n==0:
        print("Array is empty: ")
        return
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==num:
            print(f"Number {num} found in array at index: {mid}")
            return
        elif arr[mid]<num:
            low=mid+1
        else:
            high=mid-1
    print("Number not found in array")

n=int(input("enter length of array:"))
arr=[]
for i in range(n):
    arr.append(int(input(f"val at {i}th position: ")))
num=int(input("Enter the number you want to find: "))
bin_search(arr,num)