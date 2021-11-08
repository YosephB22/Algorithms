class Item:
    """An item to (maybe) put in a knapsack"""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        
    def __repr__(self):
        return f"Item({self.value}, {self.weight})"
        
        
def max_value(items, capacity):
    """The maximum value achievable with a given list of items and a given
       knapsack capacity."""
    table = [[0] * (capacity + 1) for _ in range(len(items) + 1)]
    for item in range(len(items)):
        for i in range(capacity+1):
            if items[item].weight <= i:
                table[item][i] = max(table[item-1][i-items[item].weight] + items[item].value, table[item-1][i])
            else:
                table[item][i] = table[item-1][i]
    return table[item][-1]
# -------------test1-------------
# The example in the lecture notes
items = [Item(45, 3),
         Item(45, 3),
         Item(80, 4),
         Item(80, 5),
         Item(100, 8)]
print(max_value(items, 10))
# -----------------------------------