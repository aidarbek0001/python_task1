import os
import sys
import subprocess

DIR = sys.argv[1]
FILES_PY = sorted([os.path.join(root, file) for root, _, files in os.walk(DIR) for file in files if file.endswith('.py')])
COMMANDS = {}

for FILE_PY in FILES_PY:
    local_vars = {}
    with open(FILE_PY, 'r', encoding='utf-8') as file:
        exec(file.read(), {}, local_vars)

    if 'CMDS' in local_vars:
        COMMANDS[FILE_PY] = local_vars['CMDS']

COMMANDS_2 = set()

for script in sorted(COMMANDS.keys()):
    for cmd in COMMANDS[script]:
        if cmd in COMMANDS_2:
            print("Команда '" + cmd + "' уже выполнялась")
        else:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            print(result.stdout.strip())
            COMMANDS_2.add(cmd)


