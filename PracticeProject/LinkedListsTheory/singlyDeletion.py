'''
Created on 23-Jul-2021

@author: nikhil
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head
        linked_list = ""
        while temp:
            linked_list += str(temp.data) + " "
            temp = temp.next
        print(linked_list)
    def deleteNode(self, key):
        temp = self.head
        if temp is None:
            return
        
        if temp.data == key:
            self.head = self.head.next
            temp = None
            return 
        
        def getPrev():
            temp = self.head     
            while temp.next.data != key:
                temp = temp.next
            return temp
        
        prev = getPrev()
        target_node = prev.next
        prev.next = target_node.next
        target_node.next = None
        
                
        
        

linked_list = LinkedList()
linked_list.head = Node(5)
second_node = Node(1)
third_node = Node(3)
fourth_node = Node(7)
linked_list.head.next = second_node
second_node.next = third_node
third_node.next = fourth_node
linked_list.printList()
linked_list.deleteNode(3)
linked_list.printList()
linked_list.deleteNode(7)
linked_list.printList()
linked_list.deleteNode(5)
linked_list.printList()



