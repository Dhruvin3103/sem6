
# kd tree hai, to hume tree structure bana na padega so node ka structure define kiya hai 
class Node: 
    def __init__(self, point, axis): 
        self.point = point # value of node i.e (x,y) agar k is 2 
        self.axis = axis # konse level pe hai ye node i.e. pata chale konse basis pe sort karna hai x ki y ..
        self.left = None # left tree 
        self.right = None # right tree 
 
def build_kdtree(points, depth=0): 
    
    if not points: # edge cases 
        return None 
    k = len(points[0]) 
    axis = depth % k # axis means konse ke basis pe sort krna hai x ki y aur modulo isliye kiya hai kyu ki wo revolve around x,y hi krna chahiye aur z hai to wo bhi 
    points.sort(key=lambda x: x[axis]) # sort krna hai based on the axis so agar 1st level hai to x ke basis fir 2nd pe y, 3rd pe x (but agar k=3 to z ke basis pe sort hoga )
    median = len(points) // 2 # middle postion find kr raha 
    node = Node(points[median], axis) # node ko define krne ka syntax hai point diya hai or level konsa hai wo 
    node.left = build_kdtree(points[:median], depth + 1) # recursive fun to wo ab left wale fir se wohi sab krega 
    node.right = build_kdtree(points[median + 1:], depth + 1)  # this for right 
    return node 
def print_tree(node, level=0, side=None): 
    # print krne ke liye 
    if node is not None: 
        prefix = "" 
        if side is not None: # ye side ke saath bata ta 
            prefix = side + "---- " 
        print("   " * level + prefix + str(node.point)) 
        print_tree(node.left, level + 1, "L") 
        print_tree(node.right, level + 1, "R") 
points = [[3, 6], [17, 15], [13, 15], [6, 12], [9, 1], [2, 7], [10, 19]]
root = build_kdtree(points)
print_tree(root) 