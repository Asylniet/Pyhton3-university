import os
path = '/Users/asylniet/Documents/Python/lab6/files/1.py'
print("Existence test: ")
print(os.path.exists(path))
print("-"*10)
print("Filename:")
print(os.path.basename(path))
print("-"*10)
print("Directory portion:")
print(os.path.dirname(path))