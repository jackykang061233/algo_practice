class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, data):
        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.val:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.val = data

    def search(self, val):
        if val == self.val:
            return str(val) + ' is found in the BST'
        elif val < self.val:
            if self.left:
                return self.left.search(val)
            else:
                return str(val) + ' is not found in the BST'
        else:
            if self.right:
                return self.right.search(val)
            else:
                return str(val) + ' is not found in the BST'
            
    # def delete(self, root, data):
    #     if root is None:
    #         return root
    #     if data < root.data:
    #         root.left = self.delete(root.left, data)
    #     elif data > root.data:
    #         root.right = self.delete(root.right, data)
    #     else:
    #         if root.left is None:
    #             temp = root.


    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.val)
        if self.right:
            self.right.PrintTree()

    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    def preorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorderTraversal(root.left)
            res = res + self.preorderTraversal(root.right)
        return res
    
    def postorderTraversal(self, root):
        res = []
        if root:
            res = self.postorderTraversal(root.left)
            res = res + self.postorderTraversal(root.right)
            res.append(root.data)
        return res

if __name__ == "__main__":
    root = TreeNode(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
    print(root.search(52))
# print(root.inorderTraversal(root))
# print(root.preorderTraversal(root))
# print(root.postorderTraversal(root))
# root.PrintTree()