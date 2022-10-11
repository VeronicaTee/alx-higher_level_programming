#!/usr/bin/python3

def safe_print_list(list, x):
    res = [i for i in list[ : x]]
    print(*res, sep = "")
    return len(res)
