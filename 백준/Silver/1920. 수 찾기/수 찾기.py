A,B = [x.rsplit() for x in [*open(0)][1::2]]
sortedA = sorted(list(int(x) for x in A))
def find(arr, target, start, end):
  mid = (start + end)//2
  if arr[mid] == target:
    return 1
  if start > end:
    return 0
  if arr[mid] < target:
    return find(arr,target, mid+1, end)
  elif arr[mid] > target:
    return find(arr, target, start, mid-1)
for i in B:
  print(find(sortedA, int(i), 0, len(A)-1))