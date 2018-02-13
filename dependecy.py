import os

import sys

from console import Console


def check_external_dependency(command, help=None):
    """
    !! Currently only supports linux !!

    :param command: the name of the command to test like `git`
    :param help: An optional help message - like "you don't have x installed, please
    follow this guide..."
    """
    check_dependency = os.system('command -v %s > /dev/null' % command)
    if check_dependency != 0:
        Console.error('%s is not installed' % command)
        if help:
            Console.info(help)
        sys.exit(1)
