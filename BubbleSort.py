# name : Samir , @samiro0on , mail: mahmoudsamir109@gmail.com
# Bubble Sort 13/1/2019
# compare , swap , list -1  # the greatest element will bubble to the end of the list

def BubbleSort (unSortedList):
    sortedList = []
    for elements in range(len(unSortedList)):

        for nTimes in range(len(unSortedList)):

            if nTimes < len(unSortedList) - 1:
                temp = 0
                if unSortedList[nTimes] > unSortedList[nTimes + 1]:

                    temp = unSortedList[nTimes]
                    unSortedList[nTimes] = unSortedList[nTimes + 1]
                    unSortedList[nTimes + 1] = temp

            else:
                break

        sortedList.insert(0, unSortedList.pop(-1))
    return sortedList

# modification instead of having a new list and pop and insert we should in the 2nd loop look for list -1
# test case :
testCase = [-3,6,27,5,9,2,6,-44,1,99,5,45,77,3,88,101,842,-23.87,5,8.4,47.4,98.144,-23.1473,62]
sortedArray = BubbleSort(testCase)
print("the final output is : ", sortedArray)
print("Thank you \nSamir.")