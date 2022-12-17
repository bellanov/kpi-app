"""Generator Example.

    Seems ideally:
    
    1) Generators first, as they are the most memory efficient means of iterating data.
    2) List comprehensions if code can't be optimized / converted to Generators
    3) Stream data or obtain the payload from a cache if there are too may items to handle.

"""
import tracemalloc


# Sum via List Comprehension
# The ENTIRE list is generated at once THEN summed
tracemalloc.start()
sum_list = sum([x for x in range(0,1000)])
print(f'Sum (comprehension): {sum_list}, RAM: {tracemalloc.get_traced_memory()}')
tracemalloc.stop()

# Sum via Generator
# Only ONE number is in memory at a given time.
tracemalloc.start()
sum_gen = sum(x for x in range(0,1000))
print(f'Sum (generator): {sum_gen}, RAM: {tracemalloc.get_traced_memory()}')
tracemalloc.start()

# Output => RAM: (current, peak)
# Sum (comprehension): 499500, RAM: (659, 29948)
# Sum (generator): 499500, RAM: (83, 296)
