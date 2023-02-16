def mergesort(l,m,r,arr):
  n1=m-l+1
  n2=r-m
  L=[0]*n1
  R=[0]*n2
  for x in range(n1):
    L[x]=arr[l+x]
  for y in range(0,n2):
    R[y]=arr[m+1+y]
  i=0
  j=0
  k=l 
  while(i<n1 and j<n2):
    if L[i]<=R[j]:
      arr[k]=L[i]
      i+=1 
    elif R[j]<=L[i]:
      arr[k]=R[j]
      j+=1 
    k+=1
  while(i<n1):
    arr[k]=L[i]
    i+=1
    k+=1 
  while(j<n2):
    arr[k]=R[j]
    j+=1 
    k+=1 
def merging(list1,l,r):
  if l<r:
    m=l+(r-l)//2
    merging(list1,l,m)
    merging(list1,m+1,r)
    mergesort(l,m,r,list1)
  


list1=[4,5,1,9,3,7,8]
merging(list1,0,len(list1)-1)
print(list1)
