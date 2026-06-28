import os
import sys

# import modules
from commands import rm
from commands import blk
from commands import h
from commands import l

def print_help():
    print("uls - ultra ls")
    print("Usage:")
    print("  uls -rm <dir>   Deletes a subdirectory and everything inside it")
    print("  uls -blk        Shows all storage drives and partitions")
    print("  uls -h          Shows the home folder contents")
    print("  uls -l <path>   Shows specific folder contents")
    print("  uls             Shows current folder contents")

def list_current_dir():
    for entry in os.listdir('.'):
        print(entry)

def handle_args(args):
    if not args:
        list_current_dir()
        sys.exit(0)

    flag = args[0]

    if flag == "-rm":
        rm.run(args)
    elif flag == "-blk":
        blk.run()
    elif flag == "-h":
        h.run()
    elif flag == "-l":
        l.run(args)
    elif flag in ["--help", "help", "-help"]:
        print_help()
    else:
        print(f"warning: unknown flag '{flag}'. Type 'uls --help' for options.")
