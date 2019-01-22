# name : Samir , @samiro0on , mail: mahmoudsamir109@gmail.com
# insertion Sort 15/1/2019  , divide and conquer
# find the pivot is a key for this algo
import random
# create a random list function which takes the length of the list and the max size the element can take
def randomList (size = 10, max = 100):
    unsortedList = []
    for xTimes in range(0,size):
        unsortedList.append(random.randrange(0,max,1))
    return unsortedList

# print(unsortedList)
# print(randomList())
# print(randomList())
# print(unsortedList)

def generalQuickSort (unsortedList):
    if len(unsortedList) <= 1:
        return unsortedList
    liftList,equalList,rightList = [],[],[]
    pivotIndex = int(len(unsortedList)/2)
    pivot = unsortedList[pivotIndex]

    for elements in range(len(unsortedList)):
        if unsortedList[elements] < pivot:
            liftList.append(unsortedList[elements])
        elif unsortedList[elements] == pivot:
            equalList.append(unsortedList[elements])
        else:
            rightList.append(unsortedList[elements])
    return generalQuickSort(liftList) + equalList + generalQuickSort(rightList)

unsortedList = randomList()
sortedList = generalQuickSort(unsortedList)
print("unsorted random list of numbers = ", unsortedList)
print("the sorted list after the quick sort algo =  ", sortedList)

# benchmark quick sort

samples = [10,100,1000,10000,100000]
times = 5
algo = {"Quick Sort": []}
from time import time
totalTime = []
for xTimes in range(0,times):
    r1 = randomList(samples[xTimes],samples[xTimes])
    t0 = time()
    s1 = generalQuickSort(r1)
    t1 = time()
    t = t1-t0
    totalTime.append(round(t,9))
print("Samples = ", samples)
print("benchmark for quick sort = ", totalTime)
# algo["Quick Sort"].append(totalTime)
print("thank you")


