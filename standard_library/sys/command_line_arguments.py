"""
command_line_arguments.py
"""
import sys

# Print all command line arguments except the script name
for arg in sys.argv[1:]:
    print(arg)
