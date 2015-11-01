'''
Given a binary tree

struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
'''

# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
        self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        self.processNode(root)

    def processNode(self, node):
        if(node is None):
          return

        nextSiblingsChild = None
        sib = node.next
        while(sib != None):
          nextSiblingsChild = sib.left or sib.right
          if(nextSiblingsChild):
            break
          sib = sib.next

        if(node.left):
          next = node.right or nextSiblingsChild
          node.left.next = next

        if(node.right != None):
          next = nextSiblingsChild
          node.right.next = next

        self.processNode(node.right)
        self.processNode(node.left)

def prettyPrint(node):
  if(node is None):
    return

  if(node.next):
    print "%s next: %s" % (node.val, node.next.val)
  else:
    print "%s next: %s" % (node.val, node.next)
  prettyPrint(node.left)
  prettyPrint(node.right)

if __name__ == '__main__':
  # Construct test binary tree
  node8 = TreeLinkNode(8)
  node9 = TreeLinkNode(9)
  node4 = TreeLinkNode(4)
  node5 = TreeLinkNode(5, None, node8)
  node6 = TreeLinkNode(6)
  node7 = TreeLinkNode(7, node9, None)
  node2 = TreeLinkNode(2, node4, node5)
  node3 = TreeLinkNode(3, node6, node7)
  node1 = TreeLinkNode(1, node2, node3)

  s = Solution()
  s.connect(node1)

  prettyPrint(node1)
