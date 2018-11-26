# -*- coding: utf-8 -*-
"""
@author: Xarly
"""

import win32gui
import time
import PIL.ImageGrab

# resolution
# PIL.ImageGrab.grab().size

for i in range(4):
    print("Point the place")
    time.sleep(3)
    flags, hcursor, (x, y) = win32gui.GetCursorInfo()
    rgb = PIL.ImageGrab.grab().load()[x, y]
    print("coordinates :", x, y, " and color:", rgb)

# 1 None
# 2 1582
# 3 1570
# 4 1557
# 5 1545
# 6 1534
# 7 1522?
# 8 1510
# 9 1500
# red: (253, 80, 104)
# grey: (240, 240, 240)
# grey scroll: (205, 205, 205)
