#!/usr/bin/env python3
# Author: Pavel Slama

import time
from effects.utils import utils


def effect_solid(strip, color, brightness):
    utils.set_all_leds_color(
        strip, utils.get_color(color, brightness))
    time.sleep(10)

#einzelnes segment ansteuern
def effect_solid_segment(strip, color, brightness, start, end):
    utils.set_segment_color(
        strip, utils.get_color(color, brightness), start, end)
    time.sleep(10)
