import os
import tempfile
import argparse
import json


def do_storage(key, value=None):
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'r') as f:
        data = json.load(f)

    if(value==None):
        if(key in data):
            print(", ".join(data[key]))
        else:
            print("")
    else:
        do_store_data(key, value, data)


def do_store_data(key, value, data):
    if (key in data):
        data[key].append(value)
    else:
        data[key] = [value]

    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'w') as f:
        json.dump(data, f)


def do_smth():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key")
    parser.add_argument("--val")
    args = parser.parse_args()
    if args.key and args.val:
        do_storage(args.key, args.val)
    elif args.key:
        do_storage(args.key)
    else:
        print("No key_name")


if __name__ == "__main__":
    do_smth()
