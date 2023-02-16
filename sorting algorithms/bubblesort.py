def bubblesort(arr):
  for x in range(len(arr)-1):
    for y in range(len(arr)-1-x):
      if arr[y]>arr[y+1]:
        arr[y],arr[y+1]=arr[y+1],arr[y]
  print(arr)

bubblesort([1,4,5,8,7,9])
