#!/usr/bin/python

from . import zero_overhead_units as nu
from pint import UnitRegistry
from os import path
resources_dir = path.join(path.dirname(__file__), 'data')

# Unit text format: Derived from Pint but there are no unit groups, contexts, alternate systems
# (e.g. Gaussian), logbase units, offset units, or % characters, and there are limited imports
# Seperate constant file needed
# units used in constants must be defined before importing constants (need to come up with a good way to do this)

class UnitSystem:
    """
    This is a class contains a unit registry and methods for accessing unit magnitude.

    Attributes:
        ureg (UnitRegistry or namespace): Either a Pint UnitRegistry or a namespace containing unit definitions.
    """
    def __init__(self, verbose, user_filename=None):
        """
        The constructor for the UnitSystem class.

        Parameters:
           verbose (bool): If true, the UnitSystem will use Pint units. If false, the UnitSystem will use floats as conversion factors and will not provide errors for incompatible units.
              user_filename (optional, str): The filename of the unit definition file. If None, the default unit definition file will be used.
        """
        self.verbose = verbose
        if verbose:
            if user_filename is not None:
                self.ureg = UnitRegistry(filename=user_filename)
            else:
                self.ureg = UnitRegistry(filename=resources_dir + '/default_units.txt')
        else:
            if user_filename is not None:
                ureg = UnitRegistry(filename=user_filename)
                nu.define_units(user_filename, ureg)
            else:
                ureg = UnitRegistry(filename=resources_dir + '/default_units.txt')
                nu.define_units(resources_dir + '/default_units.txt', ureg)
            self.ureg = nu

    def magnitude(self, quantity):
        """
        Gets the magnitude of a quantity in SI base units.

        magnitude takes a quantity and returns the quantity's magnitude in SI base units.

        Parameters:
        quantity (Pint quantity or float): The quantity to be converted. For zero overhead mode, this is the quantity in SI base units.

        Returns:
        float: The magnitude of the quantity in Pint's units or

        """
        if self.verbose:
            return quantity.to_base_units().magnitude
        else:
            return quantity

    def magnitude_as(self, quantity, unit):
        """
        Gets the magnitude of a quantity in a specified unit.

        magnitude_as takes a quantity and a unit and returns the quantity's magnitude in the unit.

        Parameters:
        quantity (Pint quantity or float): The quantity to be converted. For zero overhead mode, this is the quantity in SI base units.
        unit (Pint unit or float): The unit to convert to. For zero overhead mode, this is the ratio of the unit to SI base units.

        Returns:
        float: The magnitude of the quantity in the specified unit.

        """
        if self.verbose:
            return quantity.to(unit).magnitude
        else:
            return quantity/unit
