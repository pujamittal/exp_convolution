import numpy as np
import random

#get user input
#user input has two fields
#which array it should be added to (1 or 2)
#value to add
#continuously print the convolved value of the two arrays

a1 = []
a2 = []

while True:
    #arr = raw_input("which array are you inserting into? ")
    val = input("what value? ")

    # print(arr)
    # print(val)

    #if arr == "a1":
    a1.append(val)
    # if arr == "a2":
    #     a2.append(val)

    #need to append a number to the second array as well. both need to be the same size in order to produce a single value
    a2.append(random.randint(0,100)) #in the operational code, we would read one number at a time from the data set then loop back once we hit the size

    # print(a1)
    # print(a2)

    if a1 and a2:
        c = np.convolve(a1,a2,'valid') #look at https://docs.scipy.org/doc/numpy/reference/generated/numpy.convolve.html
        print(c)

    