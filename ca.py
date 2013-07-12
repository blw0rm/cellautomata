#!/bin/env python
# -*- coding: utf-8 -*-

"""
Cellular Automata

This is an example implementation of cellular automata algorithm.
"""

import math

__author__ = "Yaroslav Dashivets"
__copyright__ = "Copyright 2013, Cellular Automata example"
__credits__ = ["Yaroslav Dashivets"]

__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Yaroslav Dashivets"
__email__ = "yaroslav.dashivets@gmail.com"
__status__ = "Prototype"

class CA(object):
    def __init__(self, data, nbits, ruleset, iterations):
        """
        Cellular Automata implementation.
        """
        self.data = data
        self.nbits = nbits
        self.ruleset = ruleset
        self.niters = iterations

    def get_ca_size(self):
        """Calculates cellular automata size"""
        if not hasattr(self, "ca_size"):
            self.ca_size = math.log(self.data, 2)*2+1
        return self.ca_size

    def apply_rule(self, ng):
        """
        Applies appropriate rule to the neighbour group.
        """
        return int(bool(self.ruleset & 2**ng))

    def get_ng(self, row, index):
        """Returns neighbours group by the index"""
        num_neighbours = (self.nbits - 1) / 2
        row_size = int(self.get_ca_size())
        if index in (0, row_size - 1):
            if index == 0:
                shift = num_neighbours
                base = self.nbits - num_neighbours
            elif index == row_size - 1:
                shift = self.nbits - num_neighbours
                base = num_neighbours

            high = row & (2**base - 1)
            low = row >> (row_size - shift)
            return high << shift | low

        return row >> index - 1 & 2**self.nbits - 1

    def process_data(self, row):
        """Processes whole the row, prints and returns it"""
        result = 0
        print_result = ""
        for i in xrange(self.get_ca_size()):
            processed_cell = self.apply_rule(self.get_ng(row, i))
            result = result | processed_cell
            if i < self.get_ca_size() - 1:
                result <<= 1
            print_result += str(processed_cell)

        print print_result
        return result

    def iterate(self, iterations):
        """Iterates n times"""
        row = self.data
        bin_row = bin(row)[2:]
        for i in xrange(iterations):
            row = self.process_data(row)