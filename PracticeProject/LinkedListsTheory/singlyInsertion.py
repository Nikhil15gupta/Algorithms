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
    #Linked list starts from index 0
    def insertNode(self, val, pos):
        target = Node(val)
        if pos == 0:
            target.next = self.head
            self.head = target
            return 
        def getPrev():
            temp = self.head
            count = 1
            while count < pos:
                temp = temp.next
                count += 1
            return temp
        prev = getPrev()
        target.next = prev.next
        prev.next = target
        
            

linked_list = LinkedList()
linked_list.head = Node(5)
second_node = Node(1)
third_node = Node(3)
fourth_node = Node(7)
linked_list.head.next = second_node
second_node.next = third_node
third_node.next = fourth_node
linked_list.printList()
linked_list.insertNode(2, 2)
linked_list.printList()
linked_list.insertNode(9, 5)
linked_list.printList()
linked_list.insertNode(4, 0)
linked_list.printList()