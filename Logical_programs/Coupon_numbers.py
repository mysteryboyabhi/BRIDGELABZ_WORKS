"""a. Desc -> Given N distinct Coupon Numbers, how many random numbers do you
need to generate distinct coupon number? This program simulates this random
process.
b. I/P -> N Distinct Coupon Number
c. Logic -> repeatedly choose a random number and check whether it's a new one.
d. O/P -> total random number needed to have all distinct numbers.
e. Functions => Write Class Static Functions to generate random number and to
process distinct coupons."""
import random
def generate_coupon():
    chr_arr="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    permission=True
    while permission:
        coupon = ''
        grant=input("Grant me a permission 'Yes' or 'No': ").lower()
        if grant=="yes":
            while len(coupon)<5:
                new_rand=random.choice(chr_arr)
                if new_rand in coupon:
                    continue
                coupon+=new_rand
            print(coupon)
        else:
            permission=False
            print("permission granted FAIL !")
            return


generate_coupon()