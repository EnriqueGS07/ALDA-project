from sys import stdin

import table as t


if __name__ == "__main__":
    columns = int(stdin.readline().strip())
    t.create_table(columns)
