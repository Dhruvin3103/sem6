def initialize_dynamic_table():
    capacity = 1
    size = 0
    table = [None] * capacity
    return table, capacity, size
def insert(table, value, capacity, size):
    if size == capacity:
        table, capacity = resize(table, capacity)
    table[size] = value
    size += 1
    return table, capacity, size
def resize(table, capacity):
    new_capacity = capacity * 2
    new_table = [None] * new_capacity
    for i in range(len(table)):
        new_table[i] = table[i]
    return new_table, new_capacity
def cost_calculation(size):
    insertion_cost = 1
    amortized_cost = 3
    doubling_copying = 0
    total_cost = insertion_cost + doubling_copying
    bank_balance = amortized_cost - total_cost
    current_size = 1
    previous_size = 1
    print("i\tP.S\tS\tD.C\tI\tT.C\tAm.C\tBank")
    for i in range(1, size + 1):
        print(f"{i}\t{previous_size}\t{current_size}\t{doubling_copying}\t{insertion_cost}\t{total_cost}\t{amortized_cost}\t{bank_balance}")
        previous_size = current_size
        if i==current_size:
            current_size*= 2
            doubling_copying = current_size - previous_size
        else:
            doubling_copying=0      
        total_cost = insertion_cost + doubling_copying
        bank_balance = amortized_cost - total_cost + bank_balance
table, capacity, size = initialize_dynamic_table()
for i in range(1, 16):
    table, capacity, size = insert(table, i, capacity, size)
    print(f"Inserted {i}. Table:")
    print(table)
print("Cost Calculation:")
cost_calculation(size)
