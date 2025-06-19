"""
Script to validate JSON files against a schema.

C:\VirtualEnvs\misc\Scripts\Activate.ps1
cd D:\GitHub\mapserver-templates\scripts
pip install jsonschema


python validate.py api-catalog-schema.json ../isric/data.json

"""

import json
import sys
from jsonschema import validate, ValidationError

def main():
    if len(sys.argv) != 3:
        print("Usage: python validate.py <schema_file.json> <data_file.json>")
        sys.exit(1)

    schema_path = sys.argv[1]
    data_path = sys.argv[2]

    # Load the JSON Schema
    try:
        with open(schema_path, 'r', encoding='utf-8') as f:
            schema = json.load(f)
    except Exception as e:
        print(f"Error loading schema file: {e}")
        sys.exit(1)

    # Load the Linkset JSON data
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error loading data file: {e}")
        sys.exit(1)

    # Validate the data against the schema
    try:
        validate(instance=data, schema=schema)
        print("Linkset is valid.")
    except ValidationError as e:
        print("Linkset is invalid:")
        print(e.message)
        sys.exit(1)

if __name__ == "__main__":
    main()
