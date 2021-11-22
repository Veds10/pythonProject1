import argparse# it is used to make command line utility
import sys

def calc(args):
    if args.o=="add":
        return args.x + args.y
    elif args.o=="sub":
        return args.x - args.y
    elif args.o=="mul":
        return args.x * args.y
    elif args.o=="div":
        return args.x / args.y
    else:
        return"something went wrong"


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x',type=float,default=1.0,
                        help="enter 1st no.for calculation")
    parser.add_argument('--y', type=float, default=1.0,
                        help="enter 2nd no.for calculation")
    parser.add_argument('--o', type=str, default="add",
                        help="for calculation")

    args=parser.parse_args()
    sys.stdout.write(str(calc(args)))

# on powershell

# PS C:\Users\Vendanti> cd .\PycharmProjects\
# PS C:\Users\Vendanti\PycharmProjects> cd .\pythonProject1\
# PS C:\Users\Vendanti\PycharmProjects\pythonProject1> python command_line_utility
# C:\New folder\python.exe: can't open file 'C:\Users\Vendanti\PycharmProjects\pythonProject1\command_line_utility': [Errno 2] No such file or directory
# PS C:\Users\Vendanti\PycharmProjects\pythonProject1> python .\tut66command_line_utility.py
# Traceback (most recent call last):
#   File "C:\Users\Vendanti\PycharmProjects\pythonProject1\tut66command_line_utility.py", line 27, in <module>
#     sys.stdout.write(str(calc(args)))
#   File "C:\Users\Vendanti\PycharmProjects\pythonProject1\tut66command_line_utility.py", line 5, in calc
#     if args.o=="add":
# AttributeError: 'Namespace' object has no attribute 'o'
# PS C:\Users\Vendanti\PycharmProjects\pythonProject1> python .\tut66command_line_utility.py --x 3 --y 6 --o add
# usage: tut66command_line_utility.py [-h] [--x X] [--y Y] [--0 0]
# tut66command_line_utility.py: error: unrecognized arguments: --o add
# PS C:\Users\Vendanti\PycharmProjects\pythonProject1> python .\tut66command_line_utility.py --x 3 --y 6 --o add
# 9.0
# PS C:\Users\Vendanti\PycharmProjects\pythonProject1> python .\tut66command_line_utility.py --x 3 --y 6 --o sub
# -3.0
# PS C:\Users\Vendanti\PycharmProjects\pythonProject1> python .\tut66command_line_utility.py --x 3 --y 6 --o mul
# 18.0
# PS C:\Users\Vendanti\PycharmProjects\pythonProject1> python .\tut66command_line_utility.py --x 3 --y 6 --o mul
# 18.0
# PS C:\Users\Vendanti\PycharmProjects\pythonProject1> python .\tut66command_line_utility.py --x 3 --y 6 --o div
# 0.5
# PS C:\Users\Vendanti\PycharmProjects\pythonProject1>
