
import sys
sys.setrecursionlimit(2000)
class Item:
    """An item to (maybe) put in a knapsack. Weight must be an int."""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        """The representation of an item"""
        return f"Item({self.value}, {self.weight})"
def max_value(items, capacity, cache=None):
    """top down knapsack"""
    if cache is None:
        cache = dict()
    if len(items) == 0 or capacity == 0:
        return 0
        
    elif items[-1].weight > capacity:
        return max_value(items[:-1], capacity, cache)
    else:
        if (len(items), capacity) not in cache:
            cache[(len(items), capacity)] = max(max_value(items[:-1], 
                                                          capacity, cache), 
                                                (items[-1].value) + 
                                                max_value(items[:-1], 
                                                          capacity - 
                                                          (items[-1].weight), cache))
        return cache[(len(items), capacity)]

# ------------test1----------------------
# The example from the lecture notes
items = [
    Item(45, 3),
    Item(45, 3),
    Item(80, 4),
    Item(80, 5),
    Item(100, 8)]

print(max_value(items, 10))
# ----------------------------------------