# Bai 1) 1047. Remove All Adjacent Duplicates In String
class Solution(object):
    def removeDuplicates(self, S):
        ls = list(S)
        stack = [ls[0]]   
        
        for i in range(1,len(ls)):
            if len(stack )!= 0 and stack[-1] == ls[i] :
                stack.pop()
            else:
                stack.append(ls[i])
        return ''.join(stack)

# Bai 2) 1021. Remove Outermost Parentheses
class Solution(object):
    def removeOuterParentheses(self, S):
        balance = 0
        rs = []
        j = 0
        for i in range(len(S)):
            if S[i] =='(':
                balance += 1
            elif S[i] ==')':
                balance -= 1
            if balance == 0:
                rs += S[j+1:i]
                j = i+ 1
        return "".join(rs)
class Solution(object):
    def removeOuterParentheses(self, S):
        rs, opened = [],0
        for i in S:
            if i =='(' and opened > 0: rs.append(i)
            if i ==')' and opened > 1: rs.append(i)
            opened += 1 if i =='(' else -1
        return ''.join(rs)
                
                