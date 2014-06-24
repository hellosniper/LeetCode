#LRU Cache.py 
# Question: Design and implement a data structure for Least Recently Used (LRU) cache. #
# It should support the following operations: get and set.
# Question from: https://oj.leetcode.com/problems/lru-cache/
# Author: DongDing 
# Date: 2014/06/23
# Time complexity: 
# space complexity:  
# Tag: Hash Table,   
# Comment: OJ Time Limit Exceeded
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def setbeforehead(self,x):
        node = ListNode(x)
        node.next = self
        return node
    
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.table = {}
        self.capacity = capacity
        self.usinglist = ListNode(-1)#pre node
    # @return an integer
    def get(self, key):
        if self.table.has_key(key):
            self.putToFront(key)
            return self.table.get(key)
        
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self.table.has_key(key):
            self.putToFront(key)
            self.table.update({key:value})
        else:
            if len(self.table) >= self.capacity:
                #self.table.update({key:value})
                deletekey = self.deleteTheLast(key)
                self.table.pop(deletekey)
                self.addToFront(key)
            else:
                
                self.addToFront(key)
                
            self.table.update({key:value})
    def putToFront(self,key):
        #find the Node
        head = self.usinglist.next
        prehead = self.usinglist
        while head != None:
            if head.val == key:
                #take it out
                if head.next != None:
                    temp = head.next
                    prehead.next = temp
                    head.next = None
                else:
                    prehead.next = None
                break
            else:
                head = head.next
                prehead = prehead.next
        #add head to the front
        if head == None:
            pass
        if self.usinglist.next == None:
            self.usinglist.next = head
        else:
            temp1 = self.usinglist.next
            self.usinglist.next = head
            head.next = temp1        
    def deleteTheLast(self, key):
        #Delete the last node
        temp = self.usinglist
        #capacity >= 1
        #self.printlist(self.usinglist)
        while temp.next!= None:
            if temp.next.next != None:
                temp = temp.next
            else:
                deletkey = temp.next.val
                temp.next = None
        #print "after"        
        #self.printlist(self.usinglist)
        return deletkey        

    def printlist(self, head):
        temphead = head
        while (temphead != None):
            print temphead.val
            temphead = temphead.next    
    def addToFront(self, key):
        #add to the front
        temp = ListNode(key)
        if self.usinglist.next == None:
            self.usinglist.next = temp
        else:
            temp1 = self.usinglist.next
            self.usinglist.next = temp
            temp.next = temp1
                
            
a = LRUCache(9)
for i in range(15):
    a.set(i, i+100)
    a.set(i+1, i+100+1)
    #print a.get(5)
print a.get(15)
print a.get(3),a.get(4),a.get(5),a.get(6),a.get(13),a.get(14),

for i in range(17):
    print a.get(i)
