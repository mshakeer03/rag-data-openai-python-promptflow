import os
import json

file_path = os.path.abspath('./evaluation_dataset_small.jsonl')
print(f"Trying to load file from: {file_path}")

try:
    with open(file_path, 'r') as f:
        for line in f:
            data = json.loads(line.strip())
            print(data)
except json.JSONDecodeError as e:
    print(f"JSON decoding failed: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
