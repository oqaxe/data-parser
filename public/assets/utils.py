import os
import re
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def get_config(path):
    try:
        with open(path, 'r') as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        logging.error(f"Configuration file '{path}' not found.")
        return None
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON in configuration file: {e}")
        return None

def extract_values(config, pattern):
    if config is None:
        return None
    
    values = []
    for key, value in config.items():
        match = re.match(pattern, str(value))
        if match:
            values.append(match.group(0))
    return values

def get_data_file_path(root, type):
    return os.path.join(root, f"{type}.csv")

def get_data_files(root):
    return [f for f in os.listdir(root) if f.endswith('.csv')]

def parse_data(file_path):
    # TO DO: implement data parsing logic here
    return []