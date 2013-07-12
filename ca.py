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