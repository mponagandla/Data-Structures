#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases():
    # Write your code here
    sentence = input()
    sentence_split = sentence.split()
    string = ""
    l = len(sentence_split) - 1
    #print(sentence_split[1])
    while l >= 0:
        #print(sentence_split[l])
        string += sentence_split[l]
        string += " "
        l-=1
    print(string)

def swap_case():
    sentence = input()
    #for ele in range(len(sentence)):
        #if (sentence[ele].islower()):
            #sentence[ele].upper()
        #elif (sentence[ele].isupper()):
            #sentence[ele].lower()
    sentence = sentence.swapcase()
    print(sentence)


#reverse_words_order_and_swap_cases()
swap_case()

# !/bin/python3

import math
import os
import random
import re
import sys


class Multiset:

    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        self.append(val)

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        self.remove(val)

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        flag = False
        for value in self:
            if value == val:
                flag = True
        return flag

    def __len__(self):
        # returns the number of elements in the multiset
        return len(self)


if __name__ == '__main__':