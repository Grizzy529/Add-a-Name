import os

def add_name_to_files(name):
  """Adds the given name to the beginning of all files in the current directory.

  Args:
    name: The name to add to the beginning of all file names.
  """

  for filename in os.listdir():
    new_filename = name + "_" + filename
    os.rename(filename, new_filename)

if __name__ == "__main__":
  name = input("Enter the name to add to all files: ")
  add_name_to_files(name)
