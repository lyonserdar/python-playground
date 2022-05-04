"""
files_and_directories.py
"""
import os

# Get the path of the current working directory
path = os.getcwd()
print(path)

# Get a list of file and directory names in the working directory
files = os.listdir()
print(files)

# Get a list of file and directory names in the working directory that starts with "o"
# and sorted alphabetically
files = os.listdir()
filtered_files = sorted(file for file in files if file.startswith("o"))
print(filtered_files)

# Get a list of file and directory names in the working directory that ends with ".py"
# and sorted alphabetically
files = os.listdir()
filtered_files = sorted(file for file in files if file.endswith(".py"))
print(filtered_files)

# Create images directory in the working directory. Then go to the images directory
# and print the current path to the working directory
os.mkdir("images")
os.chdir("images")
print(os.getcwd())

# Cleanup
os.chdir("..")  # Go to parent directory
os.rmdir("images")


# Create a directory called sales in the working directory and create 12 directories
# for each month with the names <month_number>_sales
os.mkdir("sales")
for month in range(1, 13):
    path = os.path.join("sales", f"{month:02}_sales")
    print(path)
    os.mkdir(path)

directories = sorted(os.listdir("sales"))
print(directories)

# Cleanup
os.chdir("sales")
for directory in directories:
    os.rmdir(directory)
os.chdir("..")
os.rmdir("sales")

# Create a directory called images. Then in this directory create two directories called
# png and jpg. Before creating each directory, check if such directory exists.
if not os.path.exists("images"):
    os.mkdir("images")

path = os.path.join("images", "png")
if not os.path.exists(path):
    os.mkdir(path)

path = os.path.join("images", "jpg")
if not os.path.exists(path):
    os.mkdir(path)

for root, dirs, files in os.walk("images"):
    print(root, dirs, files)

# Cleanup
os.rmdir("images/png")
os.rmdir("images/jpg")
os.rmdir("images")
