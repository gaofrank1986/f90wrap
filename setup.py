#!/usr/bin/env python
# HF XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# HF X
# HF X   f90wrap: F90 to Python interface generator with derived type support
# HF X
# HF X   Copyright James Kermode 2014
# HF X
# HF X   These portions of the source code are released under the GNU General
# HF X   Public License, version 2, http://www.gnu.org/copyleft/gpl.html
# HF X
# HF X   If you would like to license the source code under different terms,
# HF X   please contact James Kermode, james.kermode@gmail.com
# HF X
# HF X   When using this software, please cite the following reference:
# HF X
# HF X   http://www.jrkermode.co.uk/f90wrap
# HF X
# HF XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

import sys
from f90wrap import __version__
major, minor = sys.version_info[0:2]
if (major, minor) < (2, 4):
    sys.stderr.write('Python 2.4 or later is needed to use this package\n')
    sys.exit(1)

try:
    import numpy
    if not tuple([int(x) for x in numpy.__version__.split('.')[0:2]]) >= (1, 3):
        raise ImportError
except ImportError:
    sys.stderr.write('Numpy 1.3 (http://www.numpy.org) or later needed to use this package\n')
    sys.exit(1)

try:
    import setuptools
except ImportError:
    pass
from numpy.distutils.core import setup, Extension
from numpy.distutils.system_info import get_info

fortran_t = Extension('f90wrap.sizeof_fortran_t', ['f90wrap/sizeoffortran.f90'])

f2py_info = get_info('f2py')
arraydata_ext = Extension(name='f90wrap.arraydata',
                          sources=['f90wrap/arraydatamodule.c'] + f2py_info['sources'],
                          include_dirs=f2py_info['include_dirs'])

setup(name='f90wrap',
      packages=['f90wrap'],
      scripts=['scripts/f90doc', 'scripts/f90wrap', 'scripts/f2py-f90wrap'],
      version=__version__,
      description='Fortran to Python interface generator with derived type support',
      author='James Kermode',
      author_email='james.kermode@gmail.com',
      url='http://www.jrkermode.co.uk/f90wrap',
      ext_modules=[fortran_t, arraydata_ext])
