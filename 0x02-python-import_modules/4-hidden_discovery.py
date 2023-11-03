#!/usr/bin/python3

if __name__ == "__main__":
    import importlib

    module = importlib.import_module('hidden_4')
    filtered_names = [name for name in dir(module) if not name.startswith('__')]
    sorted_names = sorted(filtered_names)
    for name in sorted_names:
        print(name)
