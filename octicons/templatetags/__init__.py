#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from json import load

# load the icon data and make it available module-wide.
ICON_DATA_FILE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), 'data.json'
)
with open(ICON_DATA_FILE, 'r') as f:
    OCTICON_DATA = load(f)


__all__ = ('OCTICON_DATA',)
