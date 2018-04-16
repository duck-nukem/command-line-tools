# coding=utf-8
import sys

import time
from multiprocessing import Process


class LoadingFrameSets(object):
    circles = u'○◔◑◕●'
    corners = u'⌜⌝⌟⌞'
    dots = u'⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏'
    dots_alter = u'⠁⠂⠄⡀⢀⠠⠐⠈'
    moon = u'🌑🌒🌓🌔🌕🌖🌗🌘'
    quadrants = u'▖▘▝▗'
    three_dots = (u'.  ', u'.. ', u'...')
    train = (
        u'[     ]', u'[=    ]', u'[==   ]', u'[===  ]', u'[ === ]', u'[  ===]',
        u'[   ==]', u'[    =]')
    vertical_bars = u'▁▂▃▄▅▆▇█'


class Loader(object):
    def __init__(self):
        self.process = None
        self.last_known_frame_length = 0

    def show(
            self,
            message,
            frames,
            seconds_between_frames=0.3
    ):
        self.process = Process(
            target=self.show_loader,
            args=[message, frames, seconds_between_frames]
        )
        self.last_known_frame_length = len(frames) + len(message) + 1
        self.process.start()

    def complete(self):
        sys.stdout.write(u'\r \r\n')
        sys.stdout.flush()
        self.process.terminate()

    def show_loader(
            self,
            message,
            frames,
            seconds_between_frames,
    ):
        while True:
            for frame in frames:
                sys.stdout.write(u'\r%s %s' % (frame, message))
                sys.stdout.flush()
                time.sleep(seconds_between_frames)
