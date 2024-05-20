import sys
import json
import yaml
import xmltodict

source_file_name = sys.argv[1]
dest_file_name = sys.argv[2]

source_file=open(source_file_name,"r")

if source_file_name.endswith('.json'):
  python_dict=json.load(source_file)

if dest_file_name.endswith('.json'):
  with open(dest_file_name, 'w') as dest_file:
    json.dump(python_dict, dest_file, indent=4)

if source_file_name.endswith('.yaml'):
  python_dict=yaml.load(source_file,Loader=yaml.FullLoader)

if dest_file_name.endswith('.yaml'):
  with open(dest_file_name, 'w') as dest_file:
    yaml.dump(python_dict, dest_file)

if source_file_name.endswith('.xml'):
  xml_string=source_file.read()
  python_dict=xmltodict.parse(xml_string)

if dest_file_name.endswith('.xml'):
  with open(dest_file_name, 'w') as dest_file:
    xml_string=xmltodict.unparse(python_dict,pretty=True)
    dest_file.write(xml_string)

print(f"Copying file {source_file_name} to {dest_file_name}. Done.")
