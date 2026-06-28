import os

def run(args):
    if len(args) < 2:
        print("error: please provide a path.")
        return
    target_path = args[1]
    try:
        print(f"--- contents of {target_path} ---")
        for entry in os.listdir(target_path):
            print(entry)
    except Exception as e:
        print(f"error: {e}")
