import sys


def read_all():
    fails = sum(1 for line in sys.stdin if 'FAIL' in line)
    print("%d lines with 'FAIL' found!" % fails)


def read_some():
    for line in sys.stdin:
        if 'FAIL' in line:
            print("Line with 'FAIL' found!")
            sys.stdin.close()
            break


def read_none():
    sys.stdin.close()


globals()[sys.argv[1]]()
