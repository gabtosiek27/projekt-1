import sys
import json

source_file_name = sys.argv[1]
dest_file_name = sys.argv[2]

source_file=open(source_file_name,"r")

if source_file_name.endswith('.json'):
  python_dict=json.load(source_file)
