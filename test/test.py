import unittest
from stein import UnitSystem
from math import isclose

class UnitRegistryTests(unittest.TestCase):
    def test_feet_and_inches(self):
        u_verbose = UnitSystem(verbose=True)
        x_verbose = 1 * u_verbose.ureg.foot
        u_zero_overhead = UnitSystem(verbose=False)
        x_zero_overhead = 1 * u_zero_overhead.ureg.foot
        self.assertTrue(isclose(u_verbose.magnitude_as(x_verbose, u_verbose.ureg.milliinch),
                                u_zero_overhead.magnitude_as(x_zero_overhead, u_zero_overhead.ureg.milliinch),
                                rel_tol=1e-9))

    def test_miles_and_angstroms(self):
        u_verbose = UnitSystem(verbose=True)
        x_verbose = 1 * u_verbose.ureg.mile
        u_zero_overhead = UnitSystem(verbose=False)
        x_zero_overhead = 1 * u_zero_overhead.ureg.mile
        self.assertTrue(isclose(u_verbose.magnitude_as(x_verbose, u_verbose.ureg.angstrom),
                                u_zero_overhead.magnitude_as(x_zero_overhead, u_zero_overhead.ureg.angstrom),
                                rel_tol=1e-9))

    def test_square_inches_and_acres(self):
        u_verbose = UnitSystem(verbose=True)
        x_verbose = 1 * u_verbose.ureg.inch**2
        u_zero_overhead = UnitSystem(verbose=False)
        x_zero_overhead = 1 * u_zero_overhead.ureg.inch**2
        self.assertTrue(isclose(u_verbose.magnitude_as(x_verbose, u_verbose.ureg.acre),
                                u_zero_overhead.magnitude_as(x_zero_overhead, u_zero_overhead.ureg.acre),
                                rel_tol=1e-9))

    def test_atmospheres_and_torr(self):
        u_verbose = UnitSystem(verbose=True)
        x_verbose = 1 * u_verbose.ureg.atmosphere
        u_zero_overhead = UnitSystem(verbose=False)
        x_zero_overhead = 1 * u_zero_overhead.ureg.atmosphere
        self.assertTrue(isclose(u_verbose.magnitude_as(x_verbose, u_verbose.ureg.torr),
                                u_zero_overhead.magnitude_as(x_zero_overhead, u_zero_overhead.ureg.torr),
                                rel_tol=1e-9))


if __name__ == '__main__':
    unittest.main()
