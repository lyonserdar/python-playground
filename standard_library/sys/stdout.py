"""
stdout.py
"""
import sys

# Redirect the standard output to a file called logs.txt
stdout = sys.stdout

with open("logs.txt", "w") as f:
    sys.stdout = f

    print("Logging...")
    print("Connecting...")
    print("Closing...")

sys.stdout = stdout
print("Completed successfully")
