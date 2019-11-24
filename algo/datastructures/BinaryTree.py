from collections import deque


class BTNode:
    """Binary is so dame easy!"""

    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data


class BTree:
    def __init__(self):
        self.root = None

    # def insert(self, val):
    #     if self.root is None:
    #         self.root = BTNode(val)
    #     else:
    #         cur = self.root
    #         while cur:
    #             if val < cur.data and cur.left is None:
    #                 cur.left = BTNode(val)
    #             elif val > cur.data and cur.right is None:
    #                 cur.right = BTNode(val)
    #             else:
    #                 if val < cur.data:
    #                     cur = cur.left
    #                 else:
    #                     cur = cur.right

    def insert(self, temp, key):

            q = []
            q.append(temp)

            # Do level order traversal until we find
            # an empty place.
            while (len(q)):
                temp = q[0]
                q.pop(0)

                if (not temp.left):
                    temp.left = BTNode(key)
                    break
                else:
                    q.append(temp.left)

                if (not temp.right):
                    temp.right = BTNode(key)
                    break
                else:
                    q.append(temp.right)


    def display(self):
        lines, _, _, _ = self._display_aux(self.root)
        for line in lines:
            print(line)

    def _display_aux(self, node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if node.right is None and node.left is None:
            line = '%s' % node.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            s = '%s' % node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            s = '%s' % node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        s = '%s' % node.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '' + s + y * '' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def levelOrderTraversal(self):
        """Level by level print out output"""
        if self.root == None:
            return None
        s = deque()
        result = []
        s.append(self.root)
        while len(s) != 0:
            cur = s.popleft()
            result.append(cur.val)
            if cur.left:  s.append(cur.left)
            if cur.right: s.append(cur.right)
        print(result)
        return result

    def get_height(self):
        def Height(root):
            if not root: return 0
            HL = Height(root.left)
            HR = Height(root.right)
            return 1 + HL if HL > HR else 1 + HR

        return Height(self.root)

n = BTree()
n.insert(n.root,3)
n.insert(n.root,4)
n.insert(n.root,5)
n.insert(n.root,1)
n.insert(n.root,2)

# n.insert(1)
# n.insert(0)
# n.insert(7)
# n.insert(7)
# n.insert(15)
# n.insert(10)
# n.insert(20)
# n.insert(9)
# n.insert(11)
# n.insert(17)
# n.insert(26)

n.display()