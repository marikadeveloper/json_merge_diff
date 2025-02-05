import json
import sys

def merge_json_files(file1, file2, output_file):
    # Load the first JSON file
    with open(file1, 'r', encoding='utf-8') as f1:
        data1 = json.load(f1)
    
    # Load the second JSON file
    with open(file2, 'r', encoding='utf-8') as f2:
        data2 = json.load(f2)
    
    # Find missing keys in file2
    missing_keys = {key: data1[key] for key in data1 if key not in data2}
    
    # Find extra keys in file2
    extra_keys = {key: data2[key] for key in data2 if key not in data1}
    
    # Rename extra keys with "DEPRECATED_" prefix
    renamed_extra_keys = {f"DEPRECATED_{key}": value for key, value in extra_keys.items()}
    
    # Merge the missing keys into file2's data and include renamed extra keys
    merged_data = {**data2, **renamed_extra_keys, **missing_keys}
    
    # Remove old extra keys
    for key in extra_keys:
        del merged_data[key]
    
    # Save the merged result into the output file
    with open(output_file, 'w', encoding='utf-8') as out:
        json.dump(merged_data, out, indent=2, ensure_ascii=False)
    
    print(f"Merged JSON saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <file1.json> <file2.json> <output.json>")
        sys.exit(1)
    
    merge_json_files(sys.argv[1], sys.argv[2], sys.argv[3])
