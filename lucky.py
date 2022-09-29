# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:51 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants


Test task
"""


def lucky_series(num):
    result = []
    while num > 0:
        result.append(num % 10)
        num //= 10

    max_series = [0]
    temp_series = []

    for i in result:
        if i in [5, 6]:
            temp_series.append(i)
            if len(max_series) < len(temp_series) and len(set(temp_series)) > 1:
                max_series = temp_series
        else:
            temp_series = []

    return sum(n * 10 ** i for i, n in enumerate(max_series))
