import os

def run():
    home_dir = os.path.expanduser("~")
    print(f"--- home folder contents ({home_dir}) ---")
    for entry in os.listdir(home_dir):
        print(entry)
