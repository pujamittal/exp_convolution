import numpy as np

#get user input
#user input has two fields
#which array it should be added to (1 or 2)
#value to add
#continuously print the convolved value of the two arrays

a1 = []
a2 = []

while True:
    arr = raw_input("which array are you inserting into? ")
    val = input("what value? ")

    # print(arr)
    # print(val)

    if arr == "a1":
        a1.append(val)
    if arr == "a2":
        a2.append(val)

    # print(a1)
    # print(a2)

    if a1 and a2:
        c = np.convolve(a1,a2,'valid')
        print(c)


    #change a2 to generate a random number from 0-255 every time we insert into a1 to convolve with
    #in the operational code, we would read one number at a time from the data set then loop back once we hit the size