#!/usr/bin/python3
for j in reversed(range(97, 123)):
    print("{:c}".format(j if (j % 2 == 0) else (j - 32)), end='')
