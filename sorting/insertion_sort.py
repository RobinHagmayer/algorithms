#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def insertion_sort(A, n):
    for i in range(1, n):
        key = A[i]
        j = i - 1
        
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1

        A[j+1] = key

    return A


if __name__ == "__main__":
    A = [5, 2, 4, 6, 1, 3]
    print(insertion_sort(A, len(A)))

