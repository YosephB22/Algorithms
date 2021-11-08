def fractional_knapsack(capacity, items):
    """constructing the fractional knapsack problem
    capacity = maximum weight we can have.
    items = (name, value, weigh)"""
    new_items = []
    if len(items) == 0:
        return 0.0
    for value in items:
        value = list(value)
        value_over_weight = value[1] / value[2]
        value.append(value_over_weight)
        new_items += [value]
    new_items.sort(key=lambda x:x[3], reverse=True)
    sums = 0
    weight = 0
    for index, v in enumerate(new_items):        
        if weight + v[2] <= capacity:
            sums += v[2]* v[3]
            weight += v[2]
        else:
            num = capacity - weight
            sums += (num / v[2])  * (v[2] * v[3])
            weight += num
            break
            
    return (sums)

# --------------test1-------------------------
# The example from the lecture notes
items = [
    ("Chocolate cookies", 20, 5),
    ("Potato chips", 15, 3),
    ("Pizza", 14, 2),
    ("Popcorn", 12, 4)]
print(fractional_knapsack(9, items))
# ------------------------------------------------