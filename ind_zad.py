#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def c(n, m):
    if m == n or m == 0:
        return 1
    if m != 1:
        return c(n - 1, m) + c(n - 1, m - 1)
    else:
        return n


if __name__ == '__main__':
    n = int(input('Введите число n: '))
    m = int(input('Введите число m: '))
    print(f"Число сочетаний из {n} по {m}: {c(n, m)}")
