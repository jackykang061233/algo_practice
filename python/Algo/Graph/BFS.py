from data_structure.binary_tree import TreeNode
import queue

def bfs(root):
    result = []
    seen = queue.Queue()
    seen.put(root)
    while seen.qsize()>0:
        node = seen.get()
        result.append(node.val)
        if node.left:
            seen.put(node.left)
        if node.right:
            seen.put(node.right)
    return result

def dfs(root):
    result = set()
    seen = []
    seen.append(root)
    while seen:
        node = seen.pop()
        result.append(node.val)
        
    return result

root = TreeNode(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

print(dfs(root))
