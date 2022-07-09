# Shows the total number of file extensions in a specific directory

from collections import Counter
import pathlib, sys , json

directory = pathlib.Path(sys.argv[1])

def file_extension_list():
  return [
    # return only file extension
    file.suffix

    # recursively iterate to get all the files in subdirectories in that path
    for file in directory.glob("**/*")

    # exclued anything indexed that doesn't start with a dot
    if str(file.suffix).startswith(".")
    
    # exclude any extension that consists of a single character (eg: .1)
    if len(str(file.suffix)) > 2
  ]

# print a sorted dictionary of file extensions as keys and their number as value
print(json.dumps(dict(Counter(file_extension_list()).most_common())))