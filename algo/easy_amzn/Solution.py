from collections import Counter


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        if not paragraph:
            return None
        for b in banned:
            paragraph = paragraph.lower().replace(b, "")

        c = Counter(
            paragraph.replace("'", " ").replace(";", " ").replace(",", " ").replace("?", "").replace("!", "").replace(
                ".", "").lower().split(" "))

        del c['']

        return c.most_common(1)[0][0]

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 1->2->3->4->5->NULL
        s = []
        cur = head
        while cur:
            s.append(cur.val)
            cur = cur.next
        copy_head = head
        cur = copy_head
        while cur:
            val = s.pop()
            cur.val = val
            cur = cur.next

        return copy_head



    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        i = 0
        j = len(A) - 1
        _max = -1
        while i < j:
            target = A[i] + A[j]
            if target > K:
                j -= 1
            else:
                """This is where you missed. You should increment i if you find the min_target"""
                if target > _max and target != K:
                    _max = target
                i += 1
        return _max

    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digit_logs = [log for log in logs if log[-1].isdigit()]
        letter_logs = [log for log in logs if log[-1].isalpha()]

        letter_logs.sort(key=lambda x: ' '.join(x.split()[1:]) + x.split()[0])

        return letter_logs + digit_logs



    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        stack = []
        if l1: # O( n )
            cur = l1
            stack.append(cur.val)
            while cur.next:
                cur = cur.next
                stack.append(cur.val)
        if l2: # O(n)
            cur = l2
            stack.append(cur.val)
            while cur.next:
                cur = cur.next
                stack.append(cur.val)
        stack.sort() # O(n log n)

        new_list = ListNode(stack[0])
        cur = new_list
        for s in stack[1:]:  # O (n)
            node = ListNode(s)
            cur.next = node
            cur = cur.next

        return new_list
