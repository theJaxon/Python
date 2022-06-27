from deepdiff import *

def properties_dict_generator(filename):
  """Grabs all valid Key Value Pairs from Properties file and returns a dictionary"""
  return  { line.split('=')[0] : line.split('=')[1].strip()
    for line in open(filename)

    # Exclude empty new lines
    if not line in ['\n']

    # Exclude comments
    if not line.startswith('#')
  }

def comparison_result(file1, file2):
  """Compares the 2 dictionaries returned from properties_dict_generator function and returns the differences"""
  preprod_dict = properties_dict_generator(file1)
  prod_dict    = properties_dict_generator(file2)
  ddiff = DeepDiff(preprod_dict, prod_dict)
  return ddiff.to_json()

print(comparison_result('file1.properties', 'file2.properties'))