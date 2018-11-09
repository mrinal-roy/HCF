def factorsOf(n):
    factor = []
    for k in range(1,n+1):   # finding Factors of the Number
        REM = n % k
        if REM == 0:
            factor.append(k)
        else:
            continue
    return factor



print("For how many numbers you want to find the HCF:")
N = int(input())   #user input of the numbers of number for which HCF to be found
num = []
for eachNumber in range(1,N+1):
    print("Enter Number "+str(eachNumber)+" :")
    num.append(int(input()))


factorsOfNum = []
temp_factorsList = []

for i in range(0,N):
    factorsOfNum.append(factorsOf(num[i]))
    temp_factorsList.append(factorsOfNum[i])
    print("Factors of Number "+str(i+1) + " is :"+ str(temp_factorsList[i]))


common = []

hcf = []
numList =[]

for eachList in range(0,N):
    numList.append(set(factorsOfNum[eachList]))
    #print(numList)

common = numList[0]
count = 0
while (count<N):
    common = common.intersection(numList[count])
    count+=1

    
hcf = list(common)
print("HCF is {}".format(max(hcf)))
        
