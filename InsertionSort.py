# name : Samir , @samiro0on , mail: mahmoudsamir109@gmail.com
# insertion Sort 13/1/2019
# select , swap and shift , set the element in the right place

def InsertionSort(unSortedList):
    flag = True
    # this flag to make sure not to have index in list out of range when i compare
    while flag:
        for nTimes in range(len(unSortedList)):
            temp = 0
            if nTimes < len(unSortedList) - 1:
                if unSortedList[nTimes] > unSortedList[nTimes + 1]:
                    temp = unSortedList[nTimes + 1]
                    unSortedList[nTimes + 1] = unSortedList[nTimes]
                    unSortedList[nTimes] = temp
                    break
            else:
                flag = False
                # raise flag mean now i have sorted list and no more swaps
    return unSortedList

testCase = [5,9,2,6,44,1,-0.32184,99,5,525,100,45,77,3,88,264,8.4,47.4,98.144,-23.1473,62]
sortedList = InsertionSort(testCase)
print("the final output is : ", sortedList)
print("Thank you \nSamir.")