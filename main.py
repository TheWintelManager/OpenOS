# PyOs
# this is a passion projet based off of maco terminal

import datetime
import psutil
import threading
from colorama import Fore, Style  ## EW WHY SO MANY IMPORTS UAGGHHHHHHHHH
import shutil
import time
import os
from tabulate import tabulate
import random
import string
import math
import sys

Vir = "Version 1.0"

USER = input(Fore.GREEN + Style.BRIGHT + "Username: ")  #lets u input a username

if USER == "":
  print(Fore.RED + Style.BRIGHT + "You didn't input a username!")
  os.execl(sys.executable, sys.executable, *sys.argv)  #restarts program
if USER == "admin":
  print(Fore.RED + Style.BRIGHT + "You can't use this username!")
  os.execl(sys.executable, sys.executable, *sys.argv)

PASSWORD = input(Fore.GREEN + Style.BRIGHT +
                 "Password: ")  #lets u input a password

skiploading = False  #if changed to true, after name input, it just boots to cmd line which i dont want :(
if os.name in ["nt", "dos"]:
  USER = str(os.getlogin())
else:

  if USER == "None":  #adds funny stuff for no username
    USER = str(os.path.expanduser("~"))
    if USER == "None":
      USER = "User"


def show_loading_screen():
  print(Fore.GREEN + Style.BRIGHT +
        f"PyTerminal Is Loading, [ {Fore.MAGENTA}{USER}{Fore.GREEN} ]")
  width = 40
  total = 100
  interval = total / width
  for i in range(width + 1):
    progress = int(i * interval)
    bar = '█' * i  # fancy loading bar yay
    stars = '░' * (width - i)
    loading_text = f"[{bar}{stars}] {progress}%"
    print(Fore.CYAN + loading_text, end='\r')
    time.sleep(0.1)
  print(Style.RESET_ALL)


if not skiploading:
  show_loading_screen()
current_datetime = datetime.datetime.now()
day = current_datetime.isoweekday()

if day == 1:
  day = "Monday"
elif day == 2:
  day = "Tuesday"
elif day == 3:
  day = "Wednesday"
elif day == 4:
  day = "Thursday"  #days of the week *clap clap*
elif day == 5:
  day = "Friday"
elif day == 6:
  day = "Saturday"
elif day == 7:
  day = "Sunday"
os.system('clear')
acv = os.getcwd()
id = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
current_datetime = datetime.datetime.now()
date_string = current_datetime.strftime("%d/%m/%Y")
print(
    f"{Fore.MAGENTA}Run_id: {Fore.CYAN}{id}{Fore.MAGENTA}  Version: {Fore.CYAN}{Vir}  {Fore.MAGENTA}Date: {Fore.CYAN}{day} - {date_string}"
) #colors


def handle_input():
  while True:
    user_input = input(f"{Fore.MAGENTA}@{USER}{os.getcwd()}:{Fore.GREEN}~$ ")
    if not user_input:
      continue
    X, *args = user_input.split()
    if X == 'kill':
      print(Fore.RED + 'This Process has been Terminated')  #quits app lmao
      break
    elif X in ['clear', 'cls']:
      os.system("clear")
      current_datetime = datetime.datetime.now()
      date_string = current_datetime.strftime("%d/%m/%Y")
      print(
          f"{Fore.MAGENTA}Run_id: {Fore.CYAN}{id}{Fore.MAGENTA}  Version: {Fore.CYAN}{Vir}  {Fore.MAGENTA}Date: {Fore.CYAN}{day} / {date_string}"
      )
    elif X in ['help']:
      print("""
            kill: Exits the OS.
            clear or cls: Clears the terminal screen.
            help: Displays a help message with a list of available commands.
            cd [directory]: Changes the current directory to the specified directory.
            ls: Lists the files and directories in the current directory.
            edit [filename]: Opens the specified file in the default editor for editing.
            write [filename]: Appends text to the specified file and allows you to create multiple lines and create text files(type 'exit' to stop).
            run [filetype][filename]: Executes the specified file with support of (python). FILETYPES SUPPORTED: .py and .md
            cat [filename]: Displays the contents of the specified file.
            timer [seconds]: Sets a timer for the specified number of seconds.
            cp [source] [destination]: Copies a file from the source location to the destination location.
            mv [source] [destination]: Moves or renames a file from the source location to the destination location.
            rm [filename]: Deletes a file.
            mkdir [directory]: Creates a new directory.
            rmdir [directory]: Removes a directory (if it's empty).
            howdoi [query]: Assists with coding, and provides snippets of code.
            disk: Displays information about the disk usage.
            cpu: Displays information about the CPU usage.
            """)
    elif X in ['cd', '..']:
      if X == 'cd':
        if not args:
          print(Fore.RED + "Error: Missing directory name" + Style.RESET_ALL)
          continue
        try:
          res = os.chdir(args[0])
          print("Changed directory")

        except FileNotFoundError:
          print(Fore.RED + f"Error: Directory '{args[0]}' not found" +
                Style.RESET_ALL)
      elif X == '..':
        res = os.chdir('..')
        print("Changed directory sucessfully")

    elif X == 'write':
      if not args:
        print(Fore.RED + "Error: Missing file name" + Style.RESET_ALL)
        continue
      filename = args[0]
      try:
        with open(filename, 'a') as file:
          while True:
            line = input()
            if line == 'exit':
              break
            file.write(line + '\n')
          file.close()
      except FileNotFoundError:
        print(Fore.RED + f"Error: File '{filename}' not found" +
              Style.RESET_ALL)

    elif X == 'run':
      if len(args) < 2:
        print(Fore.RED + "Error: Missing file type or file name" +
              Style.RESET_ALL)
        continue

      file_type = args[0]
      filename = args[1]

      try:
        if os.path.isfile(filename):
          if file_type == 'python file':
            os.system(f"python {filename}")
          elif file_type == 'text file':
            os.system(f"g++ {filename} -o {filename}.out && ./{filename}.out")
          else:
            print(Fore.RED +
                  "Error: Unsupported file type: .py and .md supported ONLY" +
                  Style.RESET_ALL)
        else:
          print(Fore.RED + f"Error: File '{filename}' not found" +
                Style.RESET_ALL)
      except Exception as e:
        print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

    elif X.startswith("edit"):
      if not args:
        print(Fore.RED + "Error: Missing file name" + Style.RESET_ALL)
        continue
      filename = args[0]
      try:
        with open(filename, 'r') as file:
          contents = file.read()

        print(f"Editing file: {filename}")
        print("===FILE CONTENTS===")
        print(contents)
        print("===================")

        print("Enter new content or type 'exit' to stop:")
        edited_contents = []
        while True:
          line = input()
          if line == 'exit':
            break
          edited_contents.append(line)

        contents = '\n'.join(edited_contents)

        with open(filename, 'w') as file:
          file.write(contents)
          print(f"File '{filename}' saved successfully.")

      except FileNotFoundError:
        print(Fore.RED + f"Error: File '{filename}' not found" +
              Style.RESET_ALL)

    elif X.startswith("cat"):
      if not args:
        print(Fore.RED + "Error: Missing file name" + Style.RESET_ALL)
        continue
      filename = args[0]
      if os.path.isdir(filename):
        print(Fore.RED + f"Error: '{filename}' is a directory." +
              Style.RESET_ALL)
      else:
        try:
          with open(filename, 'r') as file:
            contents = file.read()

          print(f"Editing file: {filename}")
          print("===FILE CONTENTS===")
          print(contents)
          print("===================")

        except FileNotFoundError:
          print(Fore.RED + f"Error: File '{filename}' not found" +
                Style.RESET_ALL)

    elif X.startswith("timer"):
      if not args:
        print(Fore.RED + "Error: Missing timer duration" + Style.RESET_ALL)
        continue
      duration = args[0]
      try:
        duration = int(duration)
        threading.Timer(duration, times_up).start()
      except ValueError:
        print(Fore.RED + f"Error: Invalid timer duration '{duration}'" +
              Style.RESET_ALL)

    elif X == 'cp':
      if len(args) != 2:
        print(Fore.RED + "Usage: cp [source] [destination]" + Style.RESET_ALL)
      else:
        source, destination = args
        try:
          shutil.copy(source, destination)
          print(f"File '{source}' copied to '{destination}'")
        except FileNotFoundError:
          print(Fore.RED + f"Error: File '{source}' not found" +
                Style.RESET_ALL)

    elif X == 'mv':
      if len(args) != 2:
        print(Fore.RED + "Usage: mv [source] [destination]" + Style.RESET_ALL)
      else:
        source, destination = args
        try:
          shutil.move(source, destination)
          print(f"File '{source}' moved to '{destination}'")
        except FileNotFoundError:
          print(Fore.RED + f"Error: File '{source}' not found" +
                Style.RESET_ALL)

    elif X == 'rm':
      if not args:
        print(Fore.RED + "Error: Missing file name" + Style.RESET_ALL)
      else:
        filename = args[0]
        try:
          os.remove(filename)
          print(f"File '{filename}' deleted")
        except FileNotFoundError:
          print(Fore.RED + f"Error: File '{filename}' not found" +
                Style.RESET_ALL)

    elif X == 'mkdir':
      if not args:
        print(Fore.RED + "Error: Missing directory name" + Style.RESET_ALL)
      else:
        directory = args[0]
        try:
          os.mkdir(directory)
          print(f"Directory '{directory}' created")
        except FileExistsError:
          print(Fore.RED + f"Error: Directory '{directory}' already exists" +
                Style.RESET_ALL)

    elif X == "JANK#":
      import shell
    elif X == 'rmdir':
      if not args:
        print(Fore.RED + "Error: Missing directory name" + Style.RESET_ALL)
      else:
        directory = args[0]
        try:

          os.rmdir(directory)
          print(f"Directory '{directory}' removed")
        except FileNotFoundError:
          print(Fore.RED + f"Error: Directory '{directory}' not found" +
                Style.RESET_ALL)
        except OSError as e:
          print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
    elif X == 'howdoi':
      asking = input('> ')
      os.system("howdoi " + asking)
    elif X == 'disk':
      try:
        df = psutil.disk_usage('/')
        print(f"Total space: {df.total / (2**30)} GB")
        print(f"Used space: {df.used / (2**30)} GB")
        print(f"Free space: {df.free / (2**30)} GB")
      except Exception as e:
        print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
    elif X == 'cpu':
      try:
        print(f"CPU Usage: {psutil.cpu_percent()}%")
      except Exception as e:
        print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
    elif X == 'ls':
      directory = os.getcwd()
      items = os.listdir(directory)

      file_list = []
      folder_list = []

      for item in items:
        if os.path.isfile(item):
          file_list.append(('text', item))
        else:
          folder_list.append(('folder', item))

      sorted_items = sorted(folder_list) + sorted(file_list)

      print(Fore.GREEN + Style.BRIGHT + f"Contents of Directory: {directory}")
      headers = [('', 'Type'), ('', 'Name')]
      table = tabulate(sorted_items, headers, tablefmt="fancy_grid")
      print(Fore.CYAN + table)


def times_up():
  print(Fore.YELLOW + 'Time is up!')  ##timesup


threading.Thread(target=handle_input).start()
