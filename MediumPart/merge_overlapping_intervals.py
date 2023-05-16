# Helper function to check 
# if the two intervals overlaps
def is_overlaping(a, b):
  if b[0] > a[0] and b[0] < a[1]:
    return True
  else:
    return False


# merge the intervals
def merge(arr):
  #sort the intervals by its first value
  arr.sort(key = lambda x: x[0])

  merged_list= []
  merged_list.append(arr[0])
  for i in range(1, len(arr)):
    pop_element = merged_list.pop()
    if is_overlaping(pop_element, arr[i]):
      new_element = pop_element[0], max(pop_element[1], arr[i][1])
      merged_list.append(new_element)
    else:
      merged_list.append(pop_element)
      merged_list.append(arr[i])
  return merged_list


# test the code
arr = [[1,3], [2,6], [8,10]]
print(merge(arr))