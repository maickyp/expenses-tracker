from json import load, dump
from os import path

def load_settings():
    file_path = path.dirname(__file__)
    settings_path = path.join(file_path, "..", "settings", "configuration.json")

    print(f"Loading settings from {settings_path}")
    if not path.exists(settings_path):
        raise Exception("configuration file not found")
    
    settings_file = open(settings_path)
    settings = load(settings_file)
    settings_file.close()

    return settings

def write_settings(new_settings:dict):
    file_path = path.dirname(__file__)
    settings_path = path.join(file_path, "settings", "configuration.json")
    with open(settings_path, 'w', encoding='utf-8') as f:
        dump(new_settings, f, ensure_ascii=False, indent=4)
