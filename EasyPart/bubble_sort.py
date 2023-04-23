#  O(n^2) time | O(1) space 
def bubbleSort(array):
    isSorted = false 
    counter = 0
    while not isSorted:
        isSorted = true 
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                swap(i, i + 1, array)
                isSorted = False
        counter += 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]