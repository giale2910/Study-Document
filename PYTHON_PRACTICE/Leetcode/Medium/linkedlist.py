#Bai 1) 1669. Merge In Between Linked Lists
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        step = 0
        cur1, cur2 = list1, list2
        for i in range(a-1):
            cur1 = cur1.next
        node1 = cur1
       
        for j in range(b-a+1):
            cur1 = cur1.next
        print(cur1.val)
        node2 = cur1.next
        
        node1.next = cur2
        while(cur2.next):
            cur2 = cur2.next
            
        cur2.next = node2
        
        return list1

class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        start , end = None , list1
        
        for i in range(b):
            if i == a-1:
                start =end 
            end = end.next
        start.next = list2
        
        while list2.next:
            list2 = list2.next
            
        list2.next = end.next
        
        return list1

#Bai 2) 1721. Swapping Nodes in a Linked List
class Solution(object):
    def swapNodes(self, head, k):
        slow, fast = head,head
        
        for i in range(k-1):
            fast = fast.next
        first = fast
        
        while(fast.next):
            slow = slow.next
            fast = fast.next
        
        slow.val, first.val = first.val , slow.val
        return head

class Solution(object):
    def swapNodes(self, head, k):
        curr=  head
        len = 0  
        while(curr):
            curr = curr.next
            len+=1
        node1 , node2 = head, head
        for i in range(k-1):
            node1 = node1.next
        for i in range(len-k):
            node2 = node2.next
        node1.val , node2.val =  node2.val, node1.val
        return head
#BAi3 )1019. Next Greater Node In Linked List
class Solution(object):
    def nextLargerNodes(self, head):
        ptr1  = head
        arr = []
        cnt = 0
        while(ptr1):
            cnt +=1
            ptr2 = ptr1.next
            while(ptr2):
                boolean = True
                if (ptr1.val < ptr2.val): 
                    boolean = False
                    arr.append(ptr2.val)
                    break  
                ptr2 = ptr2.next
            if cnt != len(arr):
                arr.append(0)
            ptr1 = ptr1.next
        return arr

class Solution(object):
    def nextLargerNodes(self, head):
        rs, stack = [], []
        while head:
            # stack = (index, val)
            while stack and stack[-1][1] < head.val:
                rs[stack.pop()[0]] =  head.val
            stack.append([len(rs)-1, head.val])
            rs.append(0)
            head = head.next
        return rs

# Bai 4) 817. Linked List Components
class Solution(object):
    def numComponents(self, head, G):
        cnt = 0
        while(head):
            if ( head.val in G ) and (not head.next or head.next.val not in G):
                cnt +=1
            head = head.next
        return cnt
#Bai 5) 328. Odd Even Linked List
#Nayf la sap xep gias trij odd , even nhung ko theo order
# class Solution(object):
#     def oddEvenList(self, head):
#         odd = even =  head     
#         while(even  and odd):
#             while(odd.next and odd.val % 2 == 1): 
#                 odd = odd.next
#             while(even.next and  even.val % 2 == 0) : 
#                 even = even.next
#             odd.val, even.val =even.val,odd.val
#             odd = odd.next
#             even = even.next
#         return head



class Solution(object):
    def oddEvenList(self, head):
        if not head: return None
        odd =  head     
        even = head.next
        evenHead = even
        while(even and even.next):
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head

#Bai 6) 445. Add Two Numbers II
#Cai nay se sai TH 99 + 1
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         cur1, cur2 = l1,l2
#         len1, len2 =0,0
#         while(cur1):
#             cur1 = cur1.next
#             len1 += 1
#         while(cur2):
#             cur2 = cur2.next
#             len2 += 1
        
#         cur1, cur2 = l1,l2 
#         len2GThanlen1 = False
#         if len1 < len2 :
#             cur1 , cur2 = cur2, cur1
#             len2GThanlen1  =True
                

#         save = ListNode(0,cur1)
#         saveeee = save
        
#         for i in range(abs(len1-len2)):
#             save = save.next
#             cur1 = cur1.next
#         while(cur1):
#             if cur1.val + cur2.val >=10:
#                 cur1.val = cur1.val + cur2.val -10
#                 save.val += 1
#             else:
#                 print(cur1.val)
#                 cur1.val = cur1.val + cur2.val
#                 print(cur1.val)
                
#             cur1 = cur1.next
#             cur2 = cur2.next
#             save = save.next
            
#         return l2 if len2GThanlen1 else l1 if saveeee.val == 0 else saveeee
        
class Solution(object):
    #use stack
    def addTwoNumbers(self, l1, l2):
        stack1 = []
        stack2 = []
        
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        carry ,head = 0, None
        while(stack1 or stack2 or carry):
            d1, d2 = 0,0
            d1 = stack1.pop() if stack1 else 0
            d2 = stack2.pop() if stack2 else 0
            
            sum2 = d1 + d2 + carry
            digit = sum2 % 10
            carry = sum2//10
            
            head_new = ListNode(digit)
            head_new.next = head
            head =  head_new
        return head
            
        
class Solution(object):
    #use stack
    def addTwoNumbers(self, l1, l2):
        s1 ,s2 = 0,0
        
        while l1:
            s1 = s1*10 + l1.val
            l1 = l1.next
        
        while l2:
            s2 = s2*10 + l2.val
            l2 = l2.next
            
        cur = prev = ListNode(0)
        for i in str(s1+s2):
            cur.next = ListNode(i)
            cur = cur.next 
            
            
        return prev.next   
#Bai 7) 2.Add Two Numbers 
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = node = ListNode(0)
        while(l1 or l2 or carry):
            v1 = v2 = 0
            if l1:
                v1 =l1.val
                l1 =l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, value = divmod(v1+v2+carry,10)
            node.next = ListNode(value)
            node =  node.next
        return root.next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head  = ListNode()
        cur = head
        carry = 0
        while(l1 and l2):
            sumD = l1.val + l2.val + carry
            carry = sumD //10
            value = sumD % 10
            newNode = ListNode(value)
            cur.next = newNode
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            sumD = l1.val + carry
            carry = sumD //10
            value = sumD % 10
            newNode = ListNode(value)
            cur.next = newNode
            cur = cur.next
            l1 = l1.next
        while l2:
            sumD = l2.val + carry
            carry = sumD //10
            value = sumD % 10
            newNode = ListNode(value)
            cur.next = newNode
            cur = cur.next
            l2 = l2.next
        if carry:
            newNode = ListNode(carry)
            cur.next = newNode
            cur = cur.next
        return head.next
        

        
        
               
# Bai 8) 24. Swap Nodes in Pairs
#Swap value
class Solution(object):
    def swapPairs(self, head):
       
        if (not head or not head.next):
            return head
        
        slow ,  fast =head, head.next
        while(fast):
            slow.val, fast.val = fast.val, slow.val
            slow = fast.next
            if not slow: break
            fast = slow.next
            if not fast: break
#Swap node
class Solution(object):
    def swapPairs(self, head):
        pre, pre.next = self, head
        while pre.next and pre.next.next :
            a = pre.next
            b = pre.next.next
            
            pre.next = b
            a.next = b.next
            b.next = a
            
            # pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next
            
# Recursively    
def swapPairs(self, head):
    if head and head.next:
        tmp = head.next
        head.next = self.swapPairs(tmp.next)
        tmp.next = head
        return tmp
    return head

# Bai 9) 61. Rotate List
class Solution(object):
    def rotateRight(self, head, k):
        while not head or not head.next: return head
        cur =head
        lenarr = 0
        while cur:
            lenarr+=1
            cur = cur.next

        inter = k - k//lenarr * lenarr
      
        for i in range(inter):
            cur = head
            while(cur.next.next):
                cur = cur.next
            prev = cur.next     
            cur.next = None
            prev.next = head
            head = prev
        return head

class Solution(object):
    def rotateRight(self, head, k):
        while not head or not head.next: return head
        
        cur =head
        lenarr = 0
        while cur:
            lenarr+=1
            cur = cur.next
        
        rotateTime = k % lenarr
        
        if k == 0 or rotateTime == 0:
            return head
      
        slow = fast = head
        for i in range(rotateTime):
            fast = fast.next
        while(fast.next):
            slow = slow.next
            fast = fast.next
        
        
        temp = slow.next
        slow.next = None
        fast.next= head
        head = temp
            
            
        return head
        
 
#Bai 10) 707. Design Linked List
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index >= self.size or index <0:
            return -1
        if self.head is None:
            return -1
        
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.val


    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        
        newNode = ListNode(val)
        newNode.next = self.head
        self.head=newNode
        
        self.size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        
        newNode = ListNode(val)
        if self.head == None:
            self.head = newNode
        else:
            cur =self.head
            while(cur.next):
                cur = cur.next
            cur.next = newNode
            
        
        self.size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size or index <0:
            return
        
        newNode = ListNode(val)
        if index == 0:
            self.addAtHead(val)
        else:
            cur = self.head
            for i in range(index-1):
                cur = cur.next
            newNode.next = cur.next
            cur.next = newNode
            self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index >= self.size or index <0:
            return

        if index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            for i in range(index-1):
                cur = cur.next
            removeNode = cur.next 
            cur.next  = removeNode.next
            removeNode.next = None
        
        self.size -= 1


#Bai 11) 19. Remove Nth Node From End of List
class Solution(object):
    def removeNthFromEnd(self, head, n):
        cur = prev = head           
        for i in range(n):
            cur = cur.next
        if not cur:
            return head.next
        while(cur.next):
            cur = cur.next
            prev = prev.next
        
        # removeNode = prev.next    
        # prev.next = removeNode.next
        # removeNode.next = None
        prev.next =prev.next.next
        return head
#use dummy
def removeNthFromEnd(self, head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy
    for _ in xrange(n):
        fast = fast.next
    while fast and fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next

#Bai 12) 82. Remove Duplicates from Sorted List II
#Cai nay laf tim set()
# class Solution(object):
#     def deleteDuplicates(self, head):
#         dummy = ListNode(0)
#         dummy.next = head
#         slow = fast = dummy
        
#         while(slow):
#             while fast  and slow.val == fast.val:
#                 fast = fast.next
#                 slow.next = fast
#             slow = slow.next
        
#         return dummy.next
class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        slow , fast = dummy, head

        while(fast):
            while fast.next  and fast.val == fast.next.val:
                fast = fast.next
            if slow.next == fast:
                slow , fast= slow.next , fast.next
            else:
                slow.next = fast.next
                fast= slow.next 
        
        return dummy.next
            
#Bai 13) 142. Linked List Cycle II
#, return the node where the cycle begins. If there is no cycle,


# This is very classical problem for two pointers approach: we use slow and fast pointers:
#  which moves one step at a time and fast, which moves two times at a time. 
#  To find the place where loop started, we need to do it in two iterations: 
#  first we wait until fast pointer gains slow pointer and then we move slow pointer 
#  to the start and run them with the same speed and wait until they concide.

###
class Solution(object):
    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: break
                
        if not fast or not fast.next: return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

#Bai 14) 92. Reverse Linked List II

#Bai 15) 143. Reorder List
data1 = generator.choice(PT['T'].tolist(), N ,p=PT['P'].tolist())
T, PT = np.unique(data1, return_counts=True)
print(T)
print(PT)
PT = np.array(PT)
print(PT/PT.sum())

data2 = generator.choice(PT['W'].tolist(), N ,p=PT['P'].tolist())
W, PW = np.unique(data2, return_counts=True)
print(W)
print(PW)
PW = np.array(PW)
print(PW/PW.sum())



            