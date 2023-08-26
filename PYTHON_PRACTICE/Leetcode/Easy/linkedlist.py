# Bai 1) 1290. Convert Binary Number in a Linked List to Integer
class Solution(object):
    def getDecimalValue(self, head):
        convert = 0
        while(head):
            convert = convert *2 +head.val
            head = head.next
        return convert

# Bai 2) 876. Middle of the Linked List
class Solution(object):
    def middleNode(self, head):
        double = head
        while( double and double.next ):
            head = head.next
            double = double.next.next 
        return head

#Bai 3) 206	Reverse Linked List
class Solution(object):
    def reverseList(self, head, prev=None):   
        if not head: return prev 
        curr = head.next
        head.next = prev
        return self.reverseList(curr,head)

    def reverseList(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev


#Bai 4)21. Merge Two Sorted Lists
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy = mergels = ListNode(0)
        while(l1 and l2):
            if l1.val <= l2.val:
                mergels.next = l1
                l1 = l1.next
            else:
                mergels.next = l2
                l2 = l2.next
            mergels = mergels.next
        mergels.next = l1 or l2
        return dummy.next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

#Bai 5) 83. Remove Duplicates from Sorted List                
class Solution(object):
    def deleteDuplicates(self, head):
        curr = head
        while(curr):
            if curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next            
            else:
                curr = curr.next
                
        return head
                
#Bai 6) 160	Intersection of Two Linked Lists
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        curA, curB = headA, headB
        lenA , lenB = 0 ,0
        while curA:
            lenA += 1
            curA = curA.next
        while curB:
            lenB += 1
            curB = curB.next
        curA, curB = headA, headB
        if lenA < lenB:
            for i in range(lenB-lenA):
                curB = curB.next
        else:
            for i in range(lenA-lenB):
                curA = curA.next
        while(curA != curB):
            curB = curB.next
            curA = curA.next
            
        return curA

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        curA, curB = headA, headB
        while(curA != curB):
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        return curA

#Bai 7) 141. Linked List Cycle

class Solution(object):
    def hasCycle(self, head):
        walker =  runner = head
        while walker and runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                return True
        return False

#Bai 8) 234. Palindrome Linked List

# The algorithm has two steps:
# Find the midpoint of the linked list
# Push the second half values into the stack
# Pop values out from the stack, and compare them to the first half of the linked list
class Solution(object):
    def isPalindrome(self, head):
        #Find midpoint
        #Reverse second half
        #compare
        #1.
        slow = fast = head
        while( fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        #2.
        prev = None
        while(slow):
            curr = slow
            slow = slow.next
            curr.next = prev
            prev = curr
  
        while(prev ):
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
            
#Bai 9) 203. Remove Linked List Elements
class Solution(object):
    def removeElements(self, head, val):
        dummy_head = ListNode(0)
        dummy_head.next = head
        curr = dummy_head
    
        while(curr and curr.next):
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy_head.next

class Solution(object):
    def removeElements(self, head, val):
        if not head:
            return None
        if head.val == val:
            head = self.removeElements(head.next, val)
            return head
        else:
            head.next = self.removeElements(head.next, val)
            return head
