from collections import deque

def max_levels(arr):
    levels = (len(arr) - 1).bit_length()
    levels = levels if levels <= 10 else 10 
    return levels

class Node:
    def __init__(self, key):
        if key == "null":
            self.data = None
        else:
            self.data = key
        self.left = None
        self.right = None

def find_maximals(root):
    if not root:
        return []

    maximals = []
    queue = deque([root])

    while queue:
        level_max = float('-inf')
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            if node.data is not None and node.data > level_max:
                level_max = node.data

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        maximals.append(level_max)

    return maximals

def main():
    # Example array representing a BST
    bst_array = [1, 2, 3, 4, 5, 6, 7]

    # Calculate the number of levels
    levels = max_levels(bst_array)
    print("Number of Levels:", levels)

    # Create the BST manually (for demonstration)
    root = Node(bst_array[0])
    root.left = Node(bst_array[1])
    root.right = Node(bst_array[2])
    root.left.left = Node(bst_array[3])
    root.left.right = Node(bst_array[4])
    root.right.left = Node(bst_array[5])
    root.right.right = Node(bst_array[6])

    # Find maximal elements in each level using BFS
    maximals = find_maximals(root)
    print("Maximal Elements in Each Level:", maximals)

if __name__ == "__main__":
    main()
