#!/usr/bin/python3
import os
import sys
import shlex
import subprocess


HOME = os.getenv("HOME")


def run_command(args, out=sys.stdout):
    subprocess.run(args, stdout=out, stderr=out)


def process_cmd(line):
    try:
        args = shlex.split(line)

        if len(args) == 0:
            return None

        if args[0] == 'pwd':
            print(os.getcwd())

        elif args[0] == 'cd':
            if len(args) == 1:
                os.chdir(HOME)
            else:
                os.chdir(args[1])
        elif args[0] == 'exit':
            sys.exit(0)

        else:
            if '>' in args:
                if args.count('>') == 1 and args[-2] == '>':
                    with open(args[-1], 'w') as f:
                        run_command(args[:-2], out=f)
                else:
                    print("An error has occurred", file=sys.stderr)
            else:
                run_command(args)

    except Exception:
        print("An error has occurred", file=sys.stderr)


def prompt():
    while True:
        line = input("mysh$ ")
        process_cmd(line)


def batch_mode(path):
    with open(path, 'r') as f:
        for line in f:
            print(line.strip())
            process_cmd(line)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        batch_mode(sys.argv[1])
    else:
        prompt()