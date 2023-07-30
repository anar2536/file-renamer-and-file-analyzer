import os 
import platform
import datetime
a = 0
login_system = input("log in system: ")
# getting and printing date and time
date_and_time = datetime.datetime.now()
print(f"the time which is entered in system:{date_and_time}")


# getting hostname
# printing cpu and computer operating system details
print(f"processor:{platform.processor()}")
stirng = platform.uname()
tuple = stirng[:]
print("""system:{}
hostname:{}
realease:{}
version:{}
machine:{}""".format(tuple[0],tuple[1],tuple[2],tuple[3],tuple[4]))
#enetring directory
directory = input(r"please enter directory: ")
print(directory)
file_list = os.listdir(directory)


#renaming files from orginal to time which is enetred system
for file in file_list:
    a += 1
    timestamp = datetime.datetime.now().strftime("%m-%d-%Y %H-%M-%S")
    if file.endswith(".txt"):
        old_file = os.path.join(directory,file)
        new_file = os.path.join(directory,timestamp + f"({a}).txt")
        os.rename(old_file,new_file)
    elif file.endswith(".docx"):
        old_file = os.path.join(directory,file)
        new_file = os.path.join(directory,timestamp + f"({a}).docx")
        os.rename(old_file,new_file)
    elif file.endswith(".pptx"):
        old_file = os.path.join(directory,file)
        new_file = os.path.join(directory,timestamp + f"({a}).pptx")
        os.rename(old_file,new_file)
    elif file.endswith(".png"):
        old_file = os.path.join(directory,file)
        new_file = os.path.join(directory,timestamp + f"({a}).png")
        os.rename(old_file,new_file)
    elif file.endswith(".pdf"):
        old_file = os.path.join(directory,file)
        new_file = os.path.join(directory,timestamp + f"({a}).pdf")
        os.rename(old_file,new_file)


# getting a file also subdirectories(if there is....)
#cutting directories until \desktop
while True:
    if directory.endswith("Desktop"):
        break
    directory = directory.rstrip(directory[-1])

for path, dirnames, files in os.walk(directory):
    print(f"path:{path}")
    print(f"dirnames:{dirnames}")
    for file in files:
        path_withfile = os.path.join(path,file)
        print(f"path-withfile:{path_withfile}")
        # getting modified and created time and also acsess time(subdirectories's files and directory which is entered)
        created_time = os.path.getctime(path_withfile)
        modified_time = os.path.getmtime(path_withfile)
        acsess_time = os.path.getatime(path_withfile)
        created_time1 = datetime.datetime.fromtimestamp(created_time)
        modified_time1 = datetime.datetime.fromtimestamp(modified_time)
        acsess_time1 = datetime.datetime.fromtimestamp(acsess_time)
        file_sizes = os.path.getsize(path_withfile)
        print(f"""path with file name:{file} was created {created_time1} was modified {modified_time1}
was acsessed {acsess_time1} and size is {file_sizes} \n """)
