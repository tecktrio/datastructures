import numpy as np

# Define a function that allocates a large array
def allocate_memory():
    arr = np.zeros((100000000,), dtype=np.float64)

# Call the function repeatedly to allocate more memory
while True:
    allocate_memory()