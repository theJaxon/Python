# Python

![Python](https://img.shields.io/badge/-Python-3776AB?style=for-the-badge&logo=Python&logoColor=yellow)

Python related scripts

### properties_compare
- Compares 2 application.properties files
- Split occurs on `equal` sign where the part on the left of the equal is treated as dictionary key and the part to the right is treated as dictionary value
- New lines and hashes (file comments) are excluded
- Each file generates a dictionary and [deepdiff](https://github.com/seperman/deepdiff) compares between them
- The output is in json format making it easy to call the script as follows 

#### Example
- Assume the contents of the files are as follows 
```properties
# file1
key1=value1
key2=value3

# file2
key1=value1
key2=value2
```

```bash
python3 properties_compare.py | jq
```

```json
# The following output is returned highlighting that key2 is different 
{
  "values_changed": {
    "root['key2']": {
      "new_value": "value2",
      "old_value": "value3"
    }
  }
}
```

---

### yaml_kind_summary
- Shows a summary for kubernetes resource `kind` field
- Sometimes before installing any YAML manifests one needs to get an idea about what exactly will be deployed so this script is fed a YAML file name and it shows the number of kinds found

```python
python3 yaml_kind_summary.py <yaml_file>.yaml | jq
```

```json
{
  "CustomResourceDefinition": 5,
  "ServiceAccount": 1,
  "ClusterRole": 4,
  "ClusterRoleBinding": 1,
  "Secret": 1,
  "Service": 1,
  "Deployment": 1
}
```

---

### file_extension_summary
- Recursively iterates over all files under a given path (so sub-directories are indexed as well)
- Returns a sorted dictionary containing existing file extensions in a specific directory as a key and their total number as a value

```python
python3 file_extention_summary.py /opt | jq
```

```json
# Removed the rest of file extensions so that's a snippet
{
  ".rb": 3025,
  ".html": 145,
  ".so": 132,
  ".gemspec": 114,
  ".md": 82,
  ".erb": 64,
  ".mo": 61,
}
```