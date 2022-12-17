"""Generators Example."""
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