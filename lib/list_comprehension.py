#!/usr/bin/env python3

def return_evens(num_list):
    even_list = [n for n in num_list if n % 2 == 0]
    return even_list
    pass

def make_exclamation(sentence_list):
    exclamed_list = [n + "!" for n in sentence_list]
    return exclamed_list
    pass