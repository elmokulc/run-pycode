import os
import sys


def main():
    sysarg = sys.argv[1]
    key_arg = "--files-to-run="
    if sysarg.startswith(key_arg):
        paths = sysarg[len(key_arg):].replace('[','').replace(']','').replace(' ','').split(',')
        for path in paths :
            if path.endswith(".py"):
                print(f"Running {path}")
                os.system(f"python {path}")
            else:
                print(f"{path} is not a python file")
    else:
        print("not valid argument")
