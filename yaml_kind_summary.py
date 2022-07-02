from collections import Counter
import json, sys

def yaml_kind_summary():
  """Stores all kind value mentioned in the file into a list"""
  # Use the passed argument after python script as YAML file input
  with open(sys.argv[1]) as file:
    return [
      # Grab only the Value
      line.split(":")[1].strip()
      for line in file
      if line.startswith("kind")
    ]

# Counter gives a summary of the amount of repeated items in the list
# It results in a key value pair where the key is the list item and the value is how many time that list item was repeated
# json.dumps is used to convert the output to json format so that a tool like jq can easily display the output in a better way
print(json.dumps(Counter(yaml_kind_summary())))