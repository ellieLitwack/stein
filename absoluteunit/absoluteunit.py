#!/usr/bin/python

from enum import Enum
from . import zero_overhead_units as nu
from pint import UnitRegistry
from os import path
resources_dir = path.join(path.dirname(__file__), 'data')

class Mode(Enum):
    VERBOSE = 0
    ZERO_OVERHEAD = 1

# TODO: align the unit systems names for units
# TODO: figure out symbol for planck constant and vacuum permeability
# Unit text format: Derived from Pint but there are no unit groups, contexts, alternate systems
# (e.g. Gaussian), logbase units, offset units, or % characters, and there are limited imports
# Seperate constant file needed
# units used in constants must be defined before importing constants (need to come up with a good way to do this)

class UnitSystem:
    def __init__(self, mode):
        self.mode = mode
        if mode == Mode.VERBOSE:
            self.ureg = UnitRegistry(filename=resources_dir + '/default_units.txt')
        elif mode == Mode.ZERO_OVERHEAD:
            nu.define_units(resources_dir + '/default_units.txt')
            self.ureg = nu

    def magnitude(self, quantity):
        if self.mode == Mode.VERBOSE:
            return quantity.magnitude
        elif self.mode == Mode.ZERO_OVERHEAD:
            return quantity

    def magnitude_as(self, quantity, unit):
        if self.mode == Mode.VERBOSE:
            return quantity.to(unit).magnitude
        elif self.mode == Mode.ZERO_OVERHEAD:
            return quantity/unit
