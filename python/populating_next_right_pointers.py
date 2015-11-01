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
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
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

        if(node.left):
          node.left.next = node.right

        if(node.right != None and node.next != None and node.next.left != None):
          node.right.next = node.next.left

        self.processNode(node.left)
        self.processNode(node.right)

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
  node4 = TreeLinkNode(4)
  node5 = TreeLinkNode(5)
  node6 = TreeLinkNode(6)
  node7 = TreeLinkNode(7)
  node2 = TreeLinkNode(2, node4, node5)
  node3 = TreeLinkNode(3, node6, node7)
  node1 = TreeLinkNode(1, node2, node3)

  s = Solution()
  s.connect(node1)

  prettyPrint(node1)
