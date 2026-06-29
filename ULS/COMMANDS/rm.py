import shutil

def run(args):
    if len(args) < 2:
        print("error: please specify subdirectory")
        return
    target_dir = args[1]
    try:
        shutil.rmtree(target_dir)
        print(f"[uls] successfully deleted: {target_dir}")
    except Exception as e:
        print(f"error: {e}")
