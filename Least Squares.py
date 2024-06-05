import math as mt
import numpy as np
from fractions import Fraction

print("")

while True:

    polynomialDegree = int(input("Type the degree of the polynomial you want to work with: "))
    dataValues = int(input("How many values do you have: "))

    if polynomialDegree < dataValues:
        break
    else:
        print("Please, keep in minad that a polynomial of n degree is only possible to find if the amount of data is greater than the degree of the polynomial")

        print("")

    
print("")

matrixOfEntryData = np.ones((dataValues, polynomialDegree + 1))
matrixOfExitData = np.ones((dataValues, 1))
matrixOfEntryDataTraspose = np.ones((polynomialDegree + 1, dataValues))

valuesCounter = 0

while True:

    domainValue = float(input("Plese type the {} x value. ".format(valuesCounter + 1)))
    rangeValue = float(input("Plese type the {} y value. ".format(valuesCounter + 1)))
    
    matrixOfEntryData[valuesCounter][1] = domainValue
    matrixOfExitData[valuesCounter][0] = rangeValue

    if valuesCounter == (dataValues-1):
        break

    valuesCounter += 1
    print("")

print("")

for Columns in range(polynomialDegree + 1):
    for Rows in range(dataValues):
        matrixOfEntryData[Rows][Columns] = pow(matrixOfEntryData[Rows][1], Columns)

for rows in range(dataValues):
    for columns in range(polynomialDegree+1):
        matrixOfEntryDataTraspose[columns][rows] = matrixOfEntryData[rows][columns]

# Here's where the magic happens

tranposeTimesTheOriginal = np.matmul(matrixOfEntryDataTraspose, matrixOfEntryData)
trasposeTimesDataResults = np.matmul(matrixOfEntryDataTraspose, matrixOfExitData)

inverseThatMatters = np.linalg.inv(tranposeTimesTheOriginal)

coefficientVector = np.matmul(inverseThatMatters, trasposeTimesDataResults)

print("Now you will find the coefficients of yout polynomial in the following vector. Where the first position corresponds with the constant, the second with the linear term and so on")

print("")

print(coefficientVector)

print("")

print("Now you will see information about the error in the calculations")
print("")

projectionVector = np.matmul(matrixOfEntryData, coefficientVector)

distanceProjectionData = projectionVector - matrixOfExitData

print("The max error is: {}".format(max(distanceProjectionData)))

meanAbsoluteError = 0
normOfVector = 0

for i in range(dataValues):
    meanAbsoluteError = meanAbsoluteError + abs(distanceProjectionData[i])
    normOfVector = normOfVector + pow(distanceProjectionData[i], 2)

print("The mean absolute error is: {}".format(meanAbsoluteError/dataValues))

meanCuadraticError = mt.sqrt(normOfVector)/mt.sqrt(dataValues)
print("The mean cuadratic error is: {}".format(meanCuadraticError))

print("")


