import os

def run():
    home_dir = os.path.expanduser("~")
    print(f"--- Home Folder Contents ({home_dir}) ---")
    for entry in os.listdir(home_dir):
        print(entry)
