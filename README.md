Cellular Automata
=================

This is an example implementation of cellular automaton algorithm.
It's short description can be found at [The Mendicant Bug](http://mendicantbug.com/2007/10/28/simple-cellular-automata/ "The Mendicant Bug").
For more information about algorithm see [Wikipedia] (http://en.wikipedia.org/wiki/Cellular_automaton "Wikipedia").

Usage:

    $ chmod +x ca.py
    $ ca.py <initial data> <neighbourhood bits> <rules set> <iterations>

Assumptions:

1. nbits - bits number per neighborhood, i.e. 3;
2. data - Initial data which is a number, exponent of two, i.e 1099511627776 (0x10000000000);
3. ruleset - Rules set, 8 bit, i.e. 90;
4. iterations - Recommended number of iterations, i.e. 40;

