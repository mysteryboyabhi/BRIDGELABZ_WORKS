import random
def flipcoin(number_of_time_to_flip):
    if number_of_time_to_flip<0:
        return "Please Enter positive number"
    h=0
    t=0
    for i in range(number_of_time_to_flip):
        occur=random.uniform(0,1)
        if occur<=0.5:
            print(f"tail: {occur}")
            t+=1
        else:
            print(f"head: {occur}")
            h+=1
    return f"number of head: {h}",f"number of tail: {t}",f"percentage of head vs tail is : {(abs(h-t))/t}"

print(flipcoin(int(input("Enter the number of times to flip the coin: "))))
