import numpy as np

def calculate():
    try:
        num_input = input("Please enter the 9 digits separated by spaces: ")
        num_list = [int(num) for num in num_input.split()]
        if len(num_list) == 9:
            # print("List of numbers entered:", num_list)
            matrix = np.array(num_list).reshape(3,3)
    
            mean = [list(matrix.mean(axis=0)), list(matrix.mean(axis=1)), matrix.mean()]
            variance = [list(matrix.var(axis=0)), list(matrix.var(axis=1)), matrix.var()]
            std_dev = [list(matrix.std(axis=0)), list(matrix.std(axis=1)), matrix.std()]
            max_val = [list(matrix.max(axis=0)), list(matrix.max(axis=1)), matrix.max()]
            min_val = [list(matrix.min(axis=0)), list(matrix.min(axis=1)), matrix.min()]
            sum_val = [list(matrix.sum(axis=0)), list(matrix.sum(axis=1)), matrix.sum()]

            result = {
                'mean' : mean,
                'variance': variance,
                'standard deviation' : std_dev,
                'max_val': max_val,
                'min_val': min_val,
                'sum':sum_val
            }
            return result

        else:
            print("Please enter exactly 9 numbers.")
    except ValueError:
        print("Please enter valid digits.")

        

print(calculate())   