import os
import sys

print("""
██████  ██    ██ ████████ ██   ██  ██████  ███    ██ 
██   ██  ██  ██     ██    ██   ██ ██    ██ ████   ██ 
██████    ████      ██    ███████ ██    ██ ██ ██  ██ 
██   ██    ██       ██    ██   ██ ██    ██ ██  ██ ██ 
██████     ██       ██    ██   ██  ██████  ██   ████ 
v1                                       Florinnst ©
""")

if len(sys.argv) < 3:
  print('Not enough arguments. Use as such: python3 bython.py folder/1 folder/2 ...')
  sys.exit()

def remove_file_extension(file):
  return os.path.splitext(file)[0]

directories = {}
for index, value in enumerate(sys.argv):
  if index == 0:
    continue
  directories[value] = []

for key in directories.keys():
  for (path, names, files) in os.walk(key):
    directories[key].extend(map(remove_file_extension, files))

for index, (directory, files) in enumerate(directories.items()):
  if len(files) > 0:
    print(f'Directory at {directory}:')
    for file in files:
      for index2, (directory2, files2) in enumerate(directories.items()):
        if directory2 == directory:
          continue
        if (file not in files2):
          print(f'File {file} not in {directory2}')
  else:
    print(f'Directory at {key} is empty')
  print('-----------------------------\n')