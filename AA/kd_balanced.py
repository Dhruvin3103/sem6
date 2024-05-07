def build_kdtree(points, depth=0):
    if not points:# edge case
        return None
    
    k = len(points[0])
    axis = depth % k # axis means konse ke basis pe sort krna hai x ki y aur modulo isliye kiya hai kyu ki wo revolve around krke x,y pe, also z ho sakta agar k =3  
    points.sort(key=lambda x: x[axis]) # sort krna hai based on the axis so agar 1st level hai to x ke basis fir 2nd pe y, 3rd pe x (but agar k=3 to z ke basis pe sort hoga )
    median = len(points) // 2 # middle postion find kr raha 
    
    return (points[median], axis, 
            build_kdtree(points[:median], depth + 1), 
            build_kdtree(points[median + 1:], depth + 1)) # recursive call kr rhaa hai and return kr rha where 1st is the current point, 2nd  is level, 3rd is left wala tree, 4th is right tree, ye aise isliye kiya taki print barabr kr sake print_tree func dekho clear hoga aisa return kyu kiya 

def print_tree(node, level=0, side=None):
    if node is not None:
        prefix = "" 
        if side is not None: # ye side ke saath bata ta 
            prefix = side + "---- " # ye har new level pe hoga 
        print("   " * level + prefix + str(node[0])) # print point with left ki righht hai wo bhi batayega 
        print_tree(node[2], level + 1, "L") 
        print_tree(node[3], level + 1, "R") 

points = [[3, 6], [17, 15], [13, 15], [6, 12], [9, 1], [2, 7], [10, 19]]
root = build_kdtree(points)
# print(root,type(root))
print_tree(root)
