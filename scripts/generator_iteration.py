"""Generator Examples.

    Seems ideally:
    
    1) Generators first, as they are the most memory efficient means of iterating data.
    2) List comprehensions if code can't be optimized / converted to Generators
    3) Stream data or obtain the payload from a cache if there are too may items to handle.

"""
import tracemalloc


# Emulate List of Items
items = [x for x in range(0,1000)]

def generator(list):
    index = 0
    while index < len(list):
        # Return only ONE item at a time
        yield list.pop(index)
        if len(list) == 0:
            break


# Generator Iteration
tracemalloc.start()
for i in generator(items):
    pass

print(f'Generator: {tracemalloc.get_traced_memory()}')
tracemalloc.stop()

# List Comprehension Iteration
tracemalloc.start()
for i in [x for x in range(0,1000)]:
    pass
    
print(f'List Comprehension: {tracemalloc.get_traced_memory()}')
tracemalloc.stop()

# Output RAM: (current, peak)
# RAM: (0, 5212)
# RAM: (28, 29948)