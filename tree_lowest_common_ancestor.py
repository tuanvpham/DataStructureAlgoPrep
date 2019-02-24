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


def lca(root, v1, v2):
    list_v1 = []
    list_v2 = []

    def get_next_node(node, value, path):
        path.append(node)
        if value > node.info:
            get_next_node(node.right, value, path)

        if value < node.info:
            get_next_node(node.left, value, path)

    get_next_node(root, v1, list_v1)
    get_next_node(root, v2, list_v2)

    length = min(len(list_v1), len(list_v2))
    ans = None
    for i in range(length):
        if length == 1:
            # print('length==1: ')
            # print(list_v1[0].info)
            ans = list_v1[0]
            break
        if list_v1[i] != list_v2[i]:
            # print('v1 != v2: ')
            # print(list_v1[i-1].info)
            ans = list_v1[i-1]
            break
        if i == length-1:
            ans = list_v1[i]

    # print(list(map(lambda a : a.info, list_v1)))
    # print(list(map(lambda a : a.info, list_v2)))
    return ans


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print(ans.info)
