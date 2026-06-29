import subprocess
import platform
def run():
if platform.system == 'Linux':
    subprocess.run(["lsblk"])
# check if MacOS
elif platform.system == 'Darwin':
subprocess.run(["diskutil", "list"])
# check if run WINDOWS
elif platform.system == 'Windows':
subprocess.run(["wmic", "list", "diskdrive", "brief"], shell=True)
elif platform.system == 'NetBSD':
subprocess.run(["drvctl", -l"])
# psst, slide me a push request in blk.py
elif platform.system == 'FreeBSD':
subprocess.run(["sysctl", hw.disknames"])
# why? I wanna support all Unix systems
elif platform.sysyem == 'OpenBSD':
subprocess.run(["geom", "disk", "list""])
# don't say to support more
# I just like to show this disk drive
