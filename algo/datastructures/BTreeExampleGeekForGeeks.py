# class newNode:
#
#     # Constructor to create a newNode
#     def __init__(self, data):
#         self.val = data
#         self.left = None
#         self.right = None
from collections import deque
import copy

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        r = inorder(root)
        if r == sorted(r) and len(set(r)) == len(r):
            return True
        else:
            return False

def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


class BinaryTree(object):
    # A utility function to insert a new
    # Node with given key in BST
    def __init__(self):
        self.root = None

    def maxDepth(self, root: TreeNode) -> int:
        def height(root):

            if not root:
                return 0

            LH = height(root.left)
            RH = height(root.right)

            if LH > RH:
                return LH + 1
            else:
                return RH + 1

        return height(root)

    def insert(self, val):
        # Create a new Node containing
        # the new element
        newnode = TreeNode(val)
        if self.root == None:
            self.root = newnode
            return
            # Pointer to start traversing from root
        # and traverses downward path to search
        # where the new node to be inserted
        x = self.root

        # Pointer y maintains the trailing
        # pointer of x
        y = None

        while (x != None):
            y = x
            if (val < x.val):
                x = x.left
            else:
                x = x.right

                # If the root is None i.e the tree is
        # empty. The new node is the root node
        if (y == None):
            y = newnode

            # If the new key is less then the leaf node key
        # Assign the new node to be its left child
        elif (val < y.val):
            y.left = newnode

            # else assign the new node its
        # right child
        else:
            y.right = newnode

            # Returns the pointer where the
        # new node is inserted
        return y

    # A utility function to do inorder
    # traversal of BST
    def Inorder(self, root):
        if (root == None):
            return
        else:
            self.Inorder(root.left)
            print(root.val)
            self.Inorder(root.right)



    def Postorder(self,root):
        if root == None:
            return
        else:
            self.Postorder(root.left)
            self.Postorder(root.right)
            print(root.val)

    def Preorder(self, root):
        if (root == None):
            return
        else:
            print(root.val)
            self.Preorder(root.left)
            self.Preorder(root.right)

    def print_set(self,root, p):

        if not root:
            return

        else:
            if not root.left and not root.right:
                p.append(root.val)
                return p
            self.print_set(root.left, p)
            self.print_set(root.right, p)


    def display(self):
        lines, _, _, _ = self._display_aux(self.root)
        for line in lines:
            print(line)

    def _display_aux(self, node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if node.right is None and node.left is None:
            line = '%s' % node.val
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
            s = '%s' % node.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        s = '%s' % node.val
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


if __name__ == '__main__':
    """ Let us create following BST
      
           50  
          /   \  
        30     70  
       /  \   /  \  
      20  40 60   80 
    
    """

    root = None
    BTree = BinaryTree(TreeNode(50))
    #BTree.insert(50)
    BTree.insert(30)
    BTree.insert(20)
    BTree.insert(40)
    BTree.insert(70)
    BTree.insert(60)
    # BTree.insert(80)
    # leafs_left=[]
    # leafs_right = []
    # BTree.print_set(BTree.root.left, leafs_left)
    # BTree.print_set(BTree.root.right, leafs_right)
    # print("LEAFS left: {}".format(leafs_left))
    # print("LEAFS right: {}".format(leafs_right))
    #
    # BTree = BinaryTree()
    # # [1,0,1,0,1,0,1]
    # BTree.root=TreeNode(1)
    # BTree.root.left=TreeNode(0)
    # BTree.root.right=TreeNode(1)
    # BTree.root.left.left=TreeNode(0)
    # BTree.root.left.right=TreeNode(1)
    # BTree.root.right.left=TreeNode(0)
    # BTree.root.right.right=TreeNode(1)
    # buffer = []
    # items = []
    #
    # def root_path(root, item, stack):
    #
    #     if (root == None):
    #         return
    #     else:
    #
    #         items.append(root.val)
    #         if not root.left and not root.right:
    #             buffer.append(copy.copy(items))
    #
    #         root_path(root.left, item, stack)
    #         root_path(root.right, item, stack)
    #         items.pop()
    #
    #
    #
    #
    # root_path(BTree.root, items, buffer)
    # total =0
    # for a in buffer:
    #     total+= int(f'0b{a[0]}{a[1]}{a[2]}', 2)
    #
    # def bin_base10(a):
    #     return int(f'0b{a[0]}{a[1]}{a[2]}', 2)
    #
    # print(buffer),
    # items=[3,4,5,1,2]
    # for i in items:
    #     BTree.insert(i)
# [3,4,5,1,2]
    # Prinoder traversal of the BST
    # print("InOrder:")
    # BTree.Inorder(BTree.root)
    # print("-------")
    # print("PreOrder:")
    # BTree.Preorder(BTree.root)
    # print("-------")
    # print("PostOrder:")
    # BTree.Preorder(BTree.root)
    # print("-------")
    # print(""" Let us create following BST
    #
    #        50
    #       /   \
    #     30     70
    #    /  \   /  \
    #   20  40 60   80
    #
    # """)
    BTree.display()
    #s=Solution()
    #print("IsValid: {}".format(s.isValidBST(BTree.root)))
    #BTree.display()

