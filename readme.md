# Stein
    Stein provides a wrapper around [Pint](https://github.com/hgrecco/pint) and zero overhead unit conversion factors. This allows for identifying unit errors during development and then removing the overhead of quantity objects during production.

## Installation
```bash
$ pip install stein
```

## Usage
```python
from stein import UnitSystem

# Create a unit system
US = UnitSystem(verbose=True)  # use verbose=True for Pint and verbose=False for zero overhead

# Create a unit registry
ureg = US.ureg

# Use units as you would with Pint
quantity = 3 * ureg.meter + 4 * ureg.cm

# Convert the units using the unit system
US.magnitude_as(quantity, 'mile')

# Or view the magnitude directly, which is useful for unitless quantities
US.magnitude(quantity/(2*ureg.fathom))
```