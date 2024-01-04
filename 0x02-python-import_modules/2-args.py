#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    len = len(args)
    if len == 0:
        print("{} arguments".format(len))
    else:
        print("{} arguments".format(len))
        print("{}: {}".format(len, args))
