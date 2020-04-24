import numpy as np

def my_sum_func(arg):
    total = 0
    for val in arg:
        total += val
    return total

if __name__=='__main__':
    data = range(20)
    print('Numpy yields       ', np.sum(data) )
    print('My function yields ', my_sum_func(data))
