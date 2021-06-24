'''
Created on 16-Jun-2021

@author: nikhi
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.head = None #sentinel node as pseudo-head
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index >= self.size:
            return -1
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val
            

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        self.size+=1
        to_add = ListNode(val)
        to_add.next = self.head
        self.head = to_add

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        
        self.size+=1
        to_add = ListNode(val)
        if self.size == 1:
            self.head = to_add
            return
            
            
        
        pred = self.head
        while pred.next is not None:
            pred = pred.next
        pred.next = to_add
            
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size:
            return
        
        #if index is negative, the node will be inserted at the head of the list.
        if index < 0:
            index = 0
        
        self.size +=1
        
        #to find predecessor of the node to be added
        pred = self.head
        
        
        for _ in range(index-1):
            pred = pred.next
        
        #node to be added
        to_add = ListNode(val)
        #insertion itself
        if index == 0:
            to_add.next = self.head
            self.head = to_add
            return
        
        to_add.next = pred.next
        pred.next=to_add
        
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
       
        
        if index >= self.size or index < 0:
            return
        
        
        
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        pred = self.head
        
        
        if index == (self.size - 1):
            for _ in range(index -1):
                pred = pred.next
            pred.next = None
            self.size -= 1
            return
        
        for _ in range(index -1):
            pred = pred.next
        pred.next = pred.next.next
        self.size -= 1
        
    def listPrint(self):
        printval = self.head
        while printval is not None:
            print(printval.val)
            printval = printval.next 

# obj = MyLinkedList()
# obj.head = ListNode(10)
# obj.addAtIndex(0, 11)
# obj.addAtIndex(0, 12)
# obj.addAtIndex(0, 13)
# obj.addAtIndex(2, 50)
# # obj.listPrint()
# # print(obj.get(2))
# obj.addAtHead(60)
# obj.addAtTail(70)
# obj.deleteAtIndex(2)
# obj.listPrint()
# print(obj.size)




# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1, 2)
# print(obj.get(1))

obj.deleteAtIndex(1)
obj.listPrint()
obj.get(1)




