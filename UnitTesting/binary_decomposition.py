def to_bin(num):
    temp=num
    bin_str=""
    while num:
        rem=num%2
        num=num//2
        bin_str+=str(rem)
    rev_bin=bin_str[::-1]
    n=len(bin_str)-1
    print(f"binary repersentation of {temp} is : { rev_bin}")
    for i in rev_bin:
        if i!="0":
            print(str(int(i)*(2**n))+" ",end="")
        n-=1
to_bin(106)