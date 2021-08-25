cost = int(input("Cost of item: "))
EMIHike = int(input("EMI % hike in cost of item: "))
n = int(input("Number of terms of EMIs: "))
inflation = int(input("Annual inflation %: "))
interest = int(input("Annual ROI %: "))

def calculatePrincipal():
    m = (1 + (interest - inflation) / 100) ** (1 / 12)
    w = cost * (1 + EMIHike / 100) / n

    sumOfROI = 0
    for i in range(n-1):
        sumOfROI += m ** (i + 1)

    principal = (w * (1 + sumOfROI)) / (m ** n - (1 + inflation / 100) ** (1/12))

    print("principal: " + str(principal))

calculatePrincipal()
