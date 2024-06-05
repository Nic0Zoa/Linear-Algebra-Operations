import os
import math as mt
import numpy as np
from fractions import Fraction

while True:
    dimension = int(input("Type the dimension of the space we are working on: "))
    numberofvectors = int(input("Type the numbers of vectors you will use: "))
    print("")

    ARRAYOFNUMBERS = []
    AUXARRAY = []
    SUM = []

    iterations = dimension*numberofvectors
    vectorcounter = 0


    for i in range(iterations):
        value = Fraction(input("Type the value of the {} element of the {} vector: ".format(
            i % dimension + 1, vectorcounter + 1)))
        ARRAYOFNUMBERS.append(value)
        AUXARRAY.append(0)

        if i%dimension == (dimension - 1):
            vectorcounter += 1
            print("")

    ARRAYOFVECTORS_NO_ORTOGONAL = np.array_split(ARRAYOFNUMBERS, numberofvectors)
    ARRAYOFVECTORS_ORTOGONAL = np.array_split(AUXARRAY, numberofvectors)

    ARRAYOFVECTORS_ORTOGONAL[0] = ARRAYOFVECTORS_NO_ORTOGONAL[0]

    for i in range(numberofvectors):

        SUM = []

        for j in range(dimension):
            SUM.append(0)
        
        for j in range(dimension):
            SUM[j] = 0

        for j in range(i):
            numerator = np.dot(ARRAYOFVECTORS_NO_ORTOGONAL[i], ARRAYOFVECTORS_ORTOGONAL[j])
            denominator = np.dot(ARRAYOFVECTORS_ORTOGONAL[j], ARRAYOFVECTORS_ORTOGONAL[j])

            if denominator == 0:
                scalar = 0
            else:
                scalar = numerator/denominator
            
            SUM = SUM + scalar*ARRAYOFVECTORS_ORTOGONAL[j]

        if i != 0:
            ARRAYOFVECTORS_ORTOGONAL[i] = ARRAYOFVECTORS_NO_ORTOGONAL[i] - SUM

    os.system('cls')
    os.system('cls')
    print("Now this is your new set of ortogonal vectors\n")
    for i in range(numberofvectors):
        print("Your {} vector is the following: ".format(i+1))
        print(ARRAYOFVECTORS_ORTOGONAL[i])
        print("")


    print("If you'd like a ortonormal base, there you go: \n")
    for i in range(numberofvectors):
        norm = mt.sqrt(np.dot(ARRAYOFVECTORS_ORTOGONAL[i], ARRAYOFVECTORS_ORTOGONAL[i]))

        if norm != 0:
            ARRAYOFVECTORS_ORTOGONAL[i] = ARRAYOFVECTORS_ORTOGONAL[i] / norm

    for i in range(numberofvectors):
        print("Your {} vector is the following: ".format(i+1))
        print(ARRAYOFVECTORS_ORTOGONAL[i])
        print("")

    tocontinue = input("Press enter to reload the program ")
    os.system('cls')
 
 
 
 
 
 
 
 
 
 
 
 



        





