import sys
import json

source_file_name = sys.argv[1]
dest_file_name = sys.argv[2]

source_file=open(source_file_name,"r")

if source_file_name.endswith('.json'):
  python_dict=json.load(source_file)

if dest_file_name.endswith('.json'):
  with open(dest_file_name, 'w') as dest_file:
    json.dump(python_dict, dest_file, indent=4)
