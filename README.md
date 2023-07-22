# Add-a-Name

The script first imports the os module, which provides functions for interacting with the operating system. Then, it defines a function called add_name_to_files(), which takes a name as its argument. The function iterates over all the files in the current directory and renames each file by adding the given name to the beginning of the file name.

For example, if the current directory contains the files file1.txt, file2.txt, and file3.txt, and the user enters the name my_name, the add_name_to_files() function will rename the files to my_name_file1.txt, my_name_file2.txt, and my_name_file3.txt.

The script then prompts the user to enter the name to add to all files. The name is then passed to the add_name_to_files() function, which renames all the files in the current directory.

Here is an example of how to run the script:

python add_name_to_files.py
When you run the script, it will prompt you to enter the name to add to all files. After you enter the name, the script will rename all the files in the current directory.

For example, if you enter the name my_name, the script will rename all the files in the current directory to my_name_file1.txt, my_name_file2.txt, and so on.
