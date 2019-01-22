# name : Samir , @samiro0on , mail: mahmoudsamir109@gmail.com
# Selection Sort 12/1/2019
# select , swap , counter shift # select the smallest element

def SelectionSort(unSortedList):
    # sortedList = []
    temp = 99999
    for xTimes in range(len(unSortedList)):

        temp = 99999

        for elements in range(len(unSortedList)):

            if (elements + xTimes) < len(unSortedList):
                # break before get list out of index error
                if unSortedList[elements + xTimes] < temp:
                    # get the smallest element
                    temp = unSortedList[elements + xTimes]
                    index = elements + xTimes

            else:
                break
        # swap values
        var = unSortedList[xTimes]
        unSortedList[xTimes] = unSortedList[index]
        unSortedList[index] = var
        # show output of each step
        # print(unSortedList)
    # sortedList = unSortedList
    return unSortedList
# test case :
testCase = [5,9,2,6,44,1,99,5,45,77,3,88,5,8.4,47.4,98.144,-23.1473,62]
sortedList = SelectionSort(testCase)
print("the final output is : ", sortedList)
print("Thank you \nSamir.")