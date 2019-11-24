class Array2D:
    def __init__(self):
        self.array=[]

    def add_in_2D(self,num_of_row,num_of_col):

        i=0
        for i in range(num_of_row):
            sub_arr = []
            print(f"enter values in {i}th row ")
            for j in range(num_of_col):
                sub_arr.append(int(input(f"enter value {i}th row and {j}th col: ")))
            self.array.append(sub_arr)
        return self.array

arr=Array2D()
r,c=map(int,input("enter number of rows and columns: ").split())
print(arr.add_in_2D(r,c))