#! /usr/bin/python
import sys

from graphdot import ContextGraph

diagrama = ContextGraph("context")

for line in sys.stdin:
    (orig, dest, event, context) = line.split(",")
    diagrama.add_event(orig, dest, event, context)

diagrama.print_as_dot()