"""
sys_basics.py
"""
import sys

# Print the Python version
print(sys.version.split()[0])

# Print the absolute path to the executable binary file for the Python interpreter
path = sys.executable
print(path)

# Print the path list where Python looks for modules
module_paths = sys.path
print(module_paths)
