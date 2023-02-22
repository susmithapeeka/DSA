def SelectionSort(arr):
  for i in range(len(arr)):
    minIndex=i
    for j in range(i+1,len(arr)):
      if arr[minIndex]>arr[j]:
        minIndex=j 
    arr[i],arr[minIndex]=arr[minIndex],arr[i]
  print(arr)
  
arr=[5,6,1,3,2]
SelectionSort(arr)
