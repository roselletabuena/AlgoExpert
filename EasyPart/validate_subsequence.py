# O(n) time | 0(1)

# def validateSubsequence(array, sequence):
#     arrIdx = 0
#     seqIdx = 0
#     while arrIdx < len(array) and seqIdx < len(sequence):
#         if array[arrIdx] == sequence[seqIdx]:
#             seqIdx += 1
#         arrIdx += 1
#     return seqIdx == len(sequence)

def validateSubsequence(array, sequence):
    counter = 0 

    for i, value in enumerate(array):

        if value == sequence[counter]: 
            counter += 1
        
        if counter == len(sequence):
            break

    return counter == len(sequence)


print(validateSubsequence([1, 1, 1, 1, 1], [1,1,1]))