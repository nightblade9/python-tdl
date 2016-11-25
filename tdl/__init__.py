
from __future__ import absolute_import as _
from __future__ import division as _
from __future__ import print_function as _
from __future__ import unicode_literals as _

import os

class TDLError(Exception):
    """Depreciated Exception name, do not use."""

class Error(TDLError):
    """Catch-all for most TDL specific errors."""

from tdl.tcod import *
from tdl.tcod import __all__

from tdl.tcod import event
from tdl import map
from tdl import noise

__all__ += [
            'event',
            'map',
            'noise',
            ]

__license__ = "Simplified BSD License"
__author__ = 'Kyle Stewart'
__contact__ = "4b796c65+pythonTDL@gmail.com"
__email__ = "4b796c65+pythonTDL@gmail.com"
__version__ = open(os.path.join(__path__[0], 'version.txt'), 'r').read()