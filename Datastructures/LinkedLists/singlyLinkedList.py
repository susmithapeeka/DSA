class Node:
  def __init__(self,value):
    self.value=value
    self.next=None
class SLinkedList:
  def __init__(self):
    self.head=None
    self.tail=None
  def insertSLL(self,newvalue,position):
    newnode=Node(newvalue)
    if self.head==None:
      self.head=newnode
      self.tail=newnode
    else:
      if position==0:
        newnode.next=self.head
        self.head=newnode
      if position==-1:
        self.tail.next=newnode
        newnode.next=None
        self.tail=newnode
      else:
        location=0
        temp=self.head
        while location<position-1 and temp.next is not None:
          location+=1 
          temp=temp.next
        nextnode=temp.next
        temp.next=newnode
        newnode.next=nextnode
        if temp == self.tail:
          self.tail=newnode
  def traverseSLL(self):
    if self.head is None:
      print("The Singly Linked List does not exist")
    else:
      node = self.head
      while node is not None:
        print(node.value)
        node = node.next
      
    
    

singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(8, 3)
singlyLinkedList.insertSLL(4, 4)
singlyLinkedList.insertSLL(0, 5)
singlyLinkedList.insertSLL(7, -1)
singlyLinkedList.insertSLL(5, 7)
singlyLinkedList.traverseSLL()
