class Node: 
    def __init__(self, point, axis): 
        self.point = point 
        self.axis = axis 
        self.left = None 
        self.right = None 
 
def insert(root, point, axis=0): 
    if root is None: 
        return Node(point, axis) 
    if point[axis] < root.point[axis]: 
        root.left = insert(root.left, point, (axis + 1) % len(point)) 
    else: 
        root.right = insert(root.right, point, (axis + 1) % len(point)) 
    return root 
 
def print_tree(node, level=0, side=None): 
    if node is not None: 
        prefix = "" 
        if side is not None: 
            prefix = side + "---- " 
        print("   " * level + prefix + str(node.point)) 
        print_tree(node.left, level + 1, "L") 
        print_tree(node.right, level + 1, "R") 
 

points = [[3, 6], [17, 15], [13, 15], [6, 12], [9, 1], [2, 7], [10, 19]]

root = None 
for point in points: 
    root = insert(root, point) 

print_tree(root)