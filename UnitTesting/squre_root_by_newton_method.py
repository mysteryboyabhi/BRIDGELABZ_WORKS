#Write a static function sqrt to compute the square root of a nonnegative number c given in the input using Newton's method:
#- initialize t = c
#- replace t with the average of c/t and t
#- repeat until desired accuracy reached using condition Math.abs(t - c/t) > epsilon*t where epsilon = 1e-15;
def find_root(num):
    try:
        num = float(num)
        if num < 0:
            return " Please enter positive number"

        eps=1e-15
        temp=num
        while abs(temp - (num / temp)) > (1e-15) * temp:
            temp = (num / temp + temp) / 2
        return round(temp,4)
    except ValueError:
        print(f"{type(num)} can not converted into int or float")

number_to_find_root=input("Enter the number you want to find to find the root: ")
print(find_root(number_to_find_root))