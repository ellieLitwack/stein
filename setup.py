import setuptools

setuptools.setup(name='stein',
version='0.1',
description='Stein provides a wrapper around Pint and zero overhead unit conversion factors. This allows for identifying unit errors during development and then removing the overhead of quantity objects during production.',
url='https://github.com/ellieLitwack/stein',
author='Ellie Litwack',
install_requires=['pint'],
author_email='',
packages=['stein'],
zip_safe=False)