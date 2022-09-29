# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:22 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants


Test task
"""


def sum_in_array(list, s):
    result = [-1]

    i = 0
    j = len(list) - 1

    while j > i:
        if list[i] + list[j] > s:
            j -= 1
        elif list[i] + list[j] < s:
            i += 1
        else:
            result = [list[i], list[j]]
            break

    return result

# print(sum_in_array([-3,1,4,6], 7))
