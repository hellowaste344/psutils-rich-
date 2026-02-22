import argparse
import sys

from rich import print

parser = argparse.ArgumentParser(description="My first CLI tool")

parser.add_argument("--name", type=str, help="Your name")
parser.add_argument("--age", type=int, help="Your age")
parser.add_argument("filename")
parser.add_argument("--verbose", action="store_true")
parser.add_argument(
    "--mode",
    type=str,
    choices=["r", "w"],
    required=True,
    help="Operation mode read=r, write=w",
)

args = parser.parse_args()
if args.mode == "w":
    with open(args.filename, args.mode) as f:
        msg = f"Hi {args.name}, you must be {args.age} years old."
        f.write(msg)
        print("Message has been saved successfully")
    sys.exit(0)
elif args.mode == "r":
    with open(args.filename, args.mode) as f:
        print(f.read())


if args.verbose:
    print("Verbose mode on")
