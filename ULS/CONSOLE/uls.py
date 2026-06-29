import sys
import os

# link together by pointing python/PYPY to COMMANDS
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from commands import flags

def main():
    args = sys.argv[1:]
    flags.handle_args(args)

if __name__ == "__main__":
    main()
