import math 
def structure(p, q, r): 
    v = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1]) # cross product of vectors hai
    if v == 0: 
        return 0 # 0 hai to parallel i.e collinear
    return 1 if v > 0 else 2  # 1 -> counterclockwise, 2 -> clockwise 

def gs(points): 
    n = len(points) 
    if n < 3: # min 4 points chahiye convex hull bnaa ne ke liye 
        return [] 
    min_pt = min(points, key=lambda x: (x[1], x[0])) # idar sabse lowest point nikalte hai, plot the graph aur sabse lowest point hai wo milega idar 
    print(min_pt)
    sort_pts = sorted(points, key=lambda x: (math.atan2(x[1] - min_pt[1], x[0] - min_pt[0]), x)) # fir ye sorting kiya hai w.r.t min_pt on the basis of angle, formula yaad rakhna
    print(sort_pts)
    stack = [sort_pts[0], sort_pts[1], sort_pts[2]] 
    print(f"After addition 3 points , stack : {stack}") 
    # algo chalu ho rha idar se 
    for i in range(3, n): 
        # algo bolta hai agar current point from stack and the coming point makes a counterclockwise turn pop karte jao 
        while len(stack) > 1 and structure(stack[-2], stack[-1], sort_pts[i]) != 2: 
            stack.pop() 
        # but agar wo counterclockwise na ho to push kar do stack me 
        stack.append(sort_pts[i]) 
        print(f"adding {sort_pts[i]} --> stack : {stack}") 
    return stack 
points =[(0, 0), (3, 1), (1, 4), (3, 3), (5, 2), (5, 5), (9, 6), (7, 0)]
print(f"Convex hull will be : {gs(points)}") 