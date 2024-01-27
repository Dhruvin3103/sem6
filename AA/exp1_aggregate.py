arr = [5,7,9,2,6,1,8,3]

stack = []
stack_len = 8

unit = []
op_count = 0

def popstack():
    if len(stack) == 0:
        return 
    else:
        top_element = stack[-1]
        stack.pop()
        # print(stack)
    
def pushstack(element):
    global op_count
    if len(stack) < stack_len:
        op_count +=1
        stack.append(element)
        print(f"push - 1 unit stack is {stack}")
        unit.append(1)
    else:
        return
    
def multipop(k):
    global op_count
    count = 0
    for i in range(k):
        if len(stack) != 0:
            popstack()
            op_count +=1
            count +=1
    return count

for i in arr:
    count = 0
    flag = 0
    print(f"for element {i}")
    if i<=len(stack):
        count = multipop(i)
        unit.append(count)
        print(f"multipop - {count} unit stack is {stack}")
    pushstack(i)

print(f"T(n) = {sum(unit)} and n = {op_count}")
print(f"amortized aggregate asymtotic notaion has complexity as o({sum(unit)//op_count})")
# print(unit,sum(unit),op_count)
    
