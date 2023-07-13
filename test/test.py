import unittest
from absoluteunit import absoluteunit as a
from math import isclose

class UnitRegistryTests(unittest.TestCase):
    def test_feet_and_inches(self):
        u_verbose = a.UnitSystem(a.Mode.VERBOSE)
        x_verbose = 1 * u_verbose.ureg.foot
        u_zero_overhead = a.UnitSystem(a.Mode.ZERO_OVERHEAD)
        x_zero_overhead = 1 * u_zero_overhead.ureg.foot
        self.assertTrue(isclose(u_verbose.magnitude_as(x_verbose, u_verbose.ureg.foot),
                                u_zero_overhead.magnitude_as(x_zero_overhead, u_zero_overhead.ureg.ft),
                                rel_tol=1e-9))


if __name__ == '__main__':
    unittest.main()
