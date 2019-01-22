# name : Samir , @samiro0on , mail: mahmoudsamir109@gmail.com
# insertion Sort 15/1/2019  , divide and conquer

import random
# create a random list function which takes the length of the list and the max size the element can take
def randomList (size = 10, max = 100):
    unsortedList = []
    for xTimes in range(0,size):
        unsortedList.append(random.randrange(0,max,1))
    return unsortedList

def Merge(leftList,rightList):
    sortedList = []
    i,j = 0,0
    while i < len(leftList) and j < len(rightList):
        if leftList[i] < rightList[j]:
            sortedList.append(leftList[i])
            i = i + 1
        else:
            sortedList.append(rightList[j])
            j = j + 1
# the next lines is the key magic
    sortedList = sortedList + leftList[i:]
    sortedList = sortedList + rightList[j:]

    return sortedList

def MergeSort(unsortedList):

    if len(unsortedList) <= 1:
        return unsortedList

    middle = int(len(unsortedList)/2)
    leftList = MergeSort(unsortedList[:middle])
    rightList = MergeSort(unsortedList[middle:])

    return Merge(leftList,rightList)


k = randomList(15,100)
print("unsorted list = ", k)
s = MergeSort(k)
print("sorted list by merge sort algo = ", s)

samples = [10,100,1000,10000,100000]
times = 5
algo = {"Merge Sort": []}
from time import time
totalTime = []
for xTimes in range(0,times):
    r1 = randomList(samples[xTimes],samples[xTimes])
    t0 = time()
    s1 = MergeSort(r1)  
    t1 = time()
    t = t1-t0
    totalTime.append(round(t,7))
print("Samples = ", samples)
print("benchmark for merge sort = ", totalTime)
# algo["Merge Sort"].append(totalTime)
print("thank you")
