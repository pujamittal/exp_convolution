import numpy as np
import random

#get user input
#user input has two fields
#which array it should be added to (1 or 2)
#value to add
#continuously print the convolved value of the two arrays

a1 = []
a2 = []
data = range(1,100)
index = 0


while True:
    val = input("what value? ")
    a1.append(val)

    #v1: convolving with random integer
    #   need to append a number to the second array as well. both need to be the same size in order to produce a single value
    #a2.append(random.randint(0,100)) #in the operational code, we would read one number at a time from the data set then loop back once we hit the size

    #v2: convolving with 1 - 100
    a2.append(data[index])
    index += 1
    if index == 99: #loop back to the start
        index = 1;

    # print(a1)
    # print(a2)

    if a1 and a2:
        c = np.convolve(a1,a2,'valid') #look at https://docs.scipy.org/doc/numpy/reference/generated/numpy.convolve.html
        print(c)

    