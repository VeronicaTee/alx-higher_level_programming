#!/usr/bin/python3

def safe_print_list(list, x):
    if x != 0:
        for i in range(list[0], list[x]):
            print(i)
