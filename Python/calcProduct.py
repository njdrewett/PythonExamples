#!python3

# using time to detemine time taken for calculations.

import time

print("Running at " + time.ctime())
time.sleep(1)
def calculateProduct(rangeLimit):
    print("calculating product")
    product = 1
    for i in range(1, rangeLimit):
        product = product * i
    #end for loop
    return product
#end calculateproduct


startTime = time.time()
product = calculateProduct(100000)
endTime = time.time()

print("The result is %s digits long" % (len(str(product))))
print("It took %s seconds to calculate" % (endTime - startTime))
