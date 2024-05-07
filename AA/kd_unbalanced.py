def insert(root, point, axis=0): 
    # agar root nhi hai to return the following ye tabhi aa sakta when root is initally na diya ho ya fir leaf nodes pe poch gye ho tab 
    if root is None: 
        return {"point": point, "axis": axis, "left": None, "right": None}
    # unbalanced me hum current point ko har level se compare krte hai aur jaha condition match hoti waha attach kr dete wo yaha ho rha 
    if point[axis] < root["point"][axis]: 
        root["left"] = insert(root["left"], point, (axis + 1) % len(point)) 
    else: 
        root["right"] = insert(root["right"], point, (axis + 1) % len(point)) 
    return root 
 
def print_tree(node, level=0, side=None): 
    # print kr rha hai balanced me jaise kr rha waise hi idar bhi ho rha 
    if node is not None: 
        prefix = "" 
        if side is not None: 
            prefix = side + "---- " 
        print("   " * level + prefix + str(node["point"])) 
        print_tree(node["left"], level + 1, "L") 
        print_tree(node["right"], level + 1, "R") 

points = [[3, 6], [17, 15], [13, 15], [6, 12], [9, 1], [2, 7], [10, 19]]

root = None 
for point in points: 
    root = insert(root, point) 

print_tree(root)
