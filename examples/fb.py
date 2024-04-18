""" Writes random colors to the framebuffer

Tested on Debian Linux in text mode

Needs /dev/fb0 to be writable:

sudo chmod 777 /dev/fb0
"""

import random

with open('/dev/fb0', 'wb') as fb:
    while True:
        fb.write(bytes([0, random.randint(0, 255), 0, 0]))
