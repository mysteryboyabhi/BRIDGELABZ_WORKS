def number_check(N):
    i=1
    while (2**i)<N:
        i+=1
    n=i-1
    for i in range(n):
        user_input=int(input(f"Hey, enter a number to find that exist in range 0 and  {N-1} or not:  "))
        found=bin_search(range(0, N), user_input)
        if found :
            print(f"Yes, your number found in range 0 to {N}")
            return
        else:
            print(f"Number not found in 0 and {N} try again")
            print()
    print("sorry you exceed your maximum limit")
def bin_search(arr, num):
    n=len(arr)
    arr=sorted(arr)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==num:

            return True
        elif arr[mid]<num:
            low=mid+1
        else:
            high=mid-1
    return False

N=int(input("Enter number to Start game: "))
number_check(N)