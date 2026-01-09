# Aidan Anderson 1/8/26

import pytest
import sys

# Driver program






# Sorting algorithms

# Bubble sort
def bubbleSort(sortlist):
    lastindex=len(sortlist)-1
    while lastindex >= 0:
        for i in range(lastindex):
            if sortlist[i] > sortlist[i+1]:
                temp = sortlist[i+1]
                sortlist[i+1] = sortlist[i]
                sortlist[i] = temp 
        lastindex -= 1

# Selection sort
def selectionSort(sortlist):
    lastindex=len(sortlist)-1
    while lastindex > 0:
        largestIndex = 0
        for i in range(1, lastindex+1):
            if sortlist[i] > sortlist[largestIndex]:
                largestIndex = i
        temp = sortlist[lastindex]
        sortlist[lastindex] = sortlist[largestIndex]
        sortlist[largestIndex] = temp 
        lastindex -= 1

# Insertionsort but a swapping version not a fancy one
def insertionSort(sortList):
    # start at [-2], look at end is it smaller, swap
    # start at [-3], look forward until smaller
    for i in range(1, len(sortList)):
        for j in range(len(sortList)-1-i, len(sortList)-1):
            if sortList[j] > sortList[j+1]:
                temp = sortList[j]
                sortList[j] = sortList[j+1]
                sortList[j+1] = temp
            else:
                # we are sorted
                break

def rec_mergesort(sortList):
    # print(sortList)

    # base case single thing
    if len(sortList) == 1:
        # print ("returning because single elem " + str(sortList[0]))
        return sortList
    
    # split
    halfpoint = int(len(sortList)/2)
    left = rec_mergesort(sortList[:halfpoint])
    right = rec_mergesort(sortList[halfpoint:])

    # print(left)
    # print(right)
    

    

    # merge left and right
    # print("merging " + str(left) + " and " + str(right))
    newlist = []
    total = len(left)+len(right)
    indexleft = 0
    indexright = 0
    count = 0
    while count < total:
        if indexleft > len(left)-1:
            if indexright > len(right)-1:
                break
            else:
                newlist.append(right[indexright])
                indexright += 1
                count += 1
                continue
                
        if indexright > len(right)-1:
            if indexleft > len(left)-1:
                break
            else:
                newlist.append(left[indexleft])
                indexleft += 1
                count += 1
                continue

        if left[indexleft] < right[indexright]:
            newlist.append(left[indexleft])
            indexleft += 1
            count += 1
            continue

        else:
            newlist.append(right[indexright])
            indexright += 1
            count += 1
            continue
    
    # for some reason this isn't changing the initiallist, so the test is failing.
    sortList = newlist
    # print("returning " + str(sortList))
    return sortList
    
def countingsort(sortList):
    countlist = [None] * 100
    for i in sortList:
        if countlist[i] == None:
            countlist[i] = 0
        countlist[i] += 1
    
    newlist = []
    for i in range(len(countlist)):
        if countlist[i] != None:
            for j in range(countlist[i]):
                newlist.append(i)
    
    sortList = newlist


# Tests
# Design decision - The sorting algorithms will sort in place.
def sortTester(initialList, expected, func):
    func(initialList)
    assert initialList == expected

def simple_list_case(func):
    sortTester([3,2,1],[1,2,3],func)

def complex_list_case(func):
    sortTester([8,1,3,9,5,7,6],[1,3,5,6,7,8,9],func)

def repeats_list_case(func):
    sortTester([1,1,4,3,3,5,5,9,2,2,2],[1,1,2,2,2,3,3,4,5,5,9],func)

def all_cases_test(func):
    simple_list_case(func)
    complex_list_case(func)
    repeats_list_case(func)

def test_bubbleSort():
    all_cases_test(bubbleSort)

def test_selectionSort():
    all_cases_test(selectionSort)

def test_insertionSort():
    all_cases_test(insertionSort)

def test_rec_mergesort():
    all_cases_test(rec_mergesort)

def test_countingsort():
    all_cases_test(countingsort)