# Aidan Anderson 1/8/26

import pytest
import sys
import random
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
    
    # this makes it so that each element gets splayed and changed. I have no idea why sortList = newList doesn't work, but this does.
    sortList[:] = newlist 
    # print("returning " + str(sortList))
    return sortList
    
def countingsort(sortList):
    countlist = [None] * 1024
    for i in sortList:
        if countlist[i] == None:
            countlist[i] = 0
        countlist[i] += 1
    
    newlist = []
    for i in range(len(countlist)):
        if countlist[i] != None:
            for j in range(countlist[i]):
                newlist.append(i)
    
    sortList[:] = newlist

def inPlace_quicksort(sortList):
    
    def quicksortIndexes(start, end):
        # random pivot
        random_index = random.randint(start,end)

        # shift it to the start
        temp = sortList[start]
        sortList[start] = sortList[random_index]
        sortList[random_index] = temp

        smalls_index = start+1
        for i in range(start+1, end+1):
            if sortList[i] < sortList[start]:
                # if smalls_index == i:
                #     smalls_index += 1
                # else:
                temp = sortList[smalls_index]
                sortList[smalls_index] = sortList[i]
                sortList[i] = temp
                smalls_index += 1
        
        # swap pivot to the right place
        temp = sortList[start]
        sortList[start] = sortList[smalls_index-1]
        sortList[smalls_index-1] = temp

        # recall with the two sides
        # if it is a valid range...
        if (smalls_index-2-start >= 1):
            quicksortIndexes(start,smalls_index-2)
        if (end-smalls_index >= 1):
            quicksortIndexes(smalls_index,end)

    quicksortIndexes(0,len(sortList)-1)



# Tests
# Design decision - The sorting algorithms will sort in place. (except mergesort and countsort :|)
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
    
def test_inPlace_quicksort():
    all_cases_test(inPlace_quicksort)



# Driver program

if __name__ == '__main__':
    random.seed = 4567

    list1 = [0] * 10000
    list2 = [0] * 10000
    list3 = [0] * 10000

    for i in range(0,len(list1)):
        list1[i] = random.randint(0,1023)

    for i in range(0,len(list2)):
        list2[i] = random.randint(0,1023)

    for i in range(0,len(list3)):
        list3[i] = random.randint(0,1023)

    originals = [list1,list2,list3]
    sorteds = [list(sorted(list1[:])),list(sorted(list2[:])),list(sorted(list3[:]))]
    reversesorteds = [list(reversed(sorteds[0][:])),list(reversed(sorteds[1][:])),list(reversed(sorteds[2][:]))]

    max_time = 0.1

    repetitions = 3

    all_lists = {'originals':originals, 'sorteds':sorteds, 'reversesorteds':reversesorteds}
    all_sorting_algorithms = [bubbleSort,selectionSort,insertionSort,rec_mergesort,countingsort,inPlace_quicksort]

    results=[]

    for listgroup in all_lists.keys():
        for currentlist in all_lists[listgroup]:
            currentfactor = 10
            # take a list, then we take a slice going up 10 in factor each time

            # while the algorithm doesn't take too long, try it and then increase the factor.
            max_time_it_took = 0
            while max_time_it_took < max_time:

                # repeat 3 times
                # get the slice
                slice_to_sort = currentlist[0:currentfactor]

                
                for sorting_algorithm in all_sorting_algorithms:
                    print(f'\n\t{sorting_algorithm.__name__}', end='')
                    for rep in range(repetitions):

                        # sort in place makes this a bit goofy
                        slice_copy = slice_to_sort[:]

                        start = time.perf_counter()
                        sorting_algorithm(slice_copy)
                        end = time.perf_counter()

                        if end - start > max_time_it_took:
                            max_time_it_took = end - start

                        results.append(dict(
                            listtype=listgroup,
                            sort=sorting_algorithm.__name__,
                            length=currentfactor,
                            time=end-start))
                        
                        if max_time_it_took > max_time:
                            break

                # increase the factor of elements copied from the list
                currentfactor *= 10
            

    print()
    # print(results)
    
    df = pd.DataFrame(results)

    print(df.head())

    df_mean = (
    df
        .groupby(["listtype", "sort", "length"], as_index=False)
        .agg(mean_time=("time", "mean"))
    )
    
    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(10, 6))

    sns.lineplot(
        data=df_mean,
        x="length",
        y="mean_time",
        hue="sort",
        marker="o"
    )

    plt.xscale("log")
    plt.yscale("log")

    plt.xlabel("Array size (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Sorting Algorithm Runtime vs Input Size")

    plt.show(block=False)


    g = sns.relplot(
        data=df_mean,
        x="length",
        y="mean_time",
        hue="sort",
        col="listtype",
        kind="line",
        marker="o",
        col_wrap=3,          # wrap if many list types
        height=4,
        aspect=1.1
    )

    g.set(
        xscale="log",
        yscale="log",
        xlabel="Array size (log scale)",
        ylabel="Mean time (seconds, log scale)"
    )

    g.figure.suptitle(
        "Sorting Algorithm Runtime by Input List Type",
        y=1.05
    )

    plt.show()

