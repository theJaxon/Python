# Python
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
