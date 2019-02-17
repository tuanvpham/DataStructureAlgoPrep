# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/copy-from/99201341?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''


def height(root):
    # print('this is root: ')
    # print(root)
    # print('left: ')
    # print(root.left)
    # print('end')
    left_height = 0
    right_height = 0
    if root.left:
        left_height = recursive(root.left)
    if root.right:
        right_height = recursive(root.right)
    # print('right height: ', right_height)
    # print('left height: ', left_height)
    if left_height + right_height == 0:
        return 0
    return max(left_height, right_height) + 1
    # return right_height + 1


def recursive(node):
    if node.right is None and node.left is None:
        # print('node has no left or right: ', node)
        return 0
    if node.left is None and node.right:
        # print('node has no left, has right: ', node)
        return recursive(node.right) + 1
    if node.right is None and node.left:
        # print('node has no right, has left: ', node)
        return recursive(node.left) + 1

    # print('node has both left and right: ', node)
    # print('node.left: ', node.left)
    # print('node.right: ', node.right)
    return recursive(node.left) + recursive(node.right) + 1
