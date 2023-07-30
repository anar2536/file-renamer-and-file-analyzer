# file-renamer-and-file-analyzer
developed with python
# Python  :snake:

We require you to solve the following tasks. Remember to read the requirements first.

#### Topics you need to know and use to solve tasks

* Python **sys** module
* Python **os** module
* Python **datetime** module


**Final Notes**: *Remember to solve and send assignments on time* :hourglass_flowing_sand:

# Assignments' list

## Assignment 1 :star:

### Description
System Information Logger:
Develop a script that utilizes to log system information such as the current date and time, the host name, operating system details, and available memory(optional).

## Assignment 2 :star: :star:

### Description
File Renamer:
Build a program that utilizes the os module to rename files in a directory. The program should allow users to specify a directory and a naming pattern. It should rename all files in the directory according to the pattern, appending a timestamp from the datetime module to each file name.

```console
python3 main.py ./main.py app.py
```
## Assignment 3 :star: :star: :star: 

### Description
File System Analyzer:
Write a program that utilizes the os module to analyze a directory and its subdirectories. The program should generate a report summarizing the file types, sizes, and last modified dates. It should also display the total number of files and directories.

```console
python3 main.py path/to/folder/
```
The program takes this directory and

* Count how much subdirectory and files it contains
* How much files it contains all, including all files its subdirectories contain
* Should report all file types and their count
* Should report file names
* Should report modified date and convert is datetime
  - Use
  ```python
  datetime.datetime.from_timestamp(modified_date)
  ```

## Assignment 4 :star: :star: :star:

### Description
In this task, you will implement a Python program that executes a terminal command using the cat command as an example. The program will take a filename as a command-line argument and display the contents of the specified file by executing the cat command. If you are using windows then instead of cat command you should use type command.
Linux/MacOS
```console
cat filename
```
Windows
```console
type filename
```
Your task is to create a Python script that utilizes the os and sys modules to execute terminal commands and interact with the operating system. The program should adhere to the following requirements:
Accept a filename as a command-line argument.
Construct a terminal command using the cat command and the provided filename.
Use the os.system() function to execute the constructed terminal command.
Display the contents of the file by running the cat command in the terminal.
Your program should allow users to execute the cat command on any file by providing the filename as a command-line argument when running the Python script. It should work on both Linux and Unix-based systems.
Ensure that your code handles scenarios where no filename is provided or when an invalid file is specified. Provide appropriate error messages or instructions in such cases.

```console
python3 main.py example.txt
