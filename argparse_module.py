#!/usr/bin/env python
#
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-c", help='display a square of a given numberi', type=int, metavar='9')
args = parser.parse_args()
print args.square ** 2

