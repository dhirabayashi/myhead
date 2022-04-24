import sys


def print_file(file, n):
    count = 0
    with open(file) as f:
        for line in f:
            if count == n:
                break

            print(line, end='')

            count += 1


def print_stdin(n):
    count = 0
    while line := sys.stdin.readline():
        if count == n:
            break

        print(line, end='')

        count += 1
