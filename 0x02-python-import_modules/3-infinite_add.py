#!/usr/bin/python3

if __name__ == "main":
    import sys
    result = 0

    for k in range(len(sys.argv) - 1):
        result += int(sys.argv[k + 1])
    print("{}".format(result))
