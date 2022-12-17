"""Pythonic Gists."""
import tracemalloc
# Generators (Yield)

# Generators (Comprehension)

tracemalloc.start()
sum_list = sum([x for x in range(0,1000)])
print(f'Sum (comprehension): {sum_list}, RAM: {tracemalloc.get_traced_memory()}')
tracemalloc.stop()

tracemalloc.start()
sum_gen = sum(x for x in range(0,1000))
print(f'Sum (generator): {sum_gen}, RAM: {tracemalloc.get_traced_memory()}')
tracemalloc.start()

# stopping the library

# f-strings

# Custom formats with f-strings
