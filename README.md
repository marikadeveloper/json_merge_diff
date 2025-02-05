# JSON Key Merger & Deprecator

This is a script that I created to quickly compare two JSON files and merge them while handling missing and extra keys:
- Adds missing keys from `file1` to `file2`
- Renames extra keys in `file2` (not present in `file1`) by prefixing them with `"DEPRECATED_"`
- Outputs a merged JSON file with all modifications.

## Usage

```sh
python merge_json.py file1.json output.json
```

## Output Example

Here’s a simple example you can include in your README.md:  

---

## Example  

### Input Files  

#### file1.json  
{
  "key.a": "Hello",
  "key.b": "World"
}

#### file2.json  
{
  "key.b": "Mondo",
  "key.c": "Extra key"
}

### Running the Script  
python merge_json.py file1.json file2.json output.json

### Output File (output.json)  
{
  "key.b": "Mondo",
  "DEPRECATED_key.c": "Extra key",
  "key.a": "Hello"
}

## Disclaimer

This is a small script that I did for speeding up my work flow. It works only with first-level keys.
