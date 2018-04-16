# coding=utf-8
from __future__ import print_function

import platform
import sys


class MessageColor(object):
    white = '\033[1;97m'
    cyan = '\033[1;36m'
    yellow = '\033[1;33m'
    green = '\033[1;32m'
    red = '\033[1;31m'
    end = '\033[1;m'


class MessageType(object):
    info = u'\033[1;36m[i]\033[1;m'
    warning = u'\033[1;33m[!]\033[1;m'
    decision = u'\033[1;34m[?]\033[1;m'
    error = u'\033[1;31m[✘]\033[1;m'
    success = u'\033[1;32m[✓]\033[1;m'
    task = u'\033[1;97m[>]\033[1;m'


class Console(object):

    @staticmethod
    def write(message, channel=sys.stdout, **kwargs):
        """
        Writes to the channel you specify - stdout by default.

        This is used by the rest of the methods inside the class, but is
        public if you want to print custom messages directly.
        """
        print(message, file=channel, **kwargs)

    @staticmethod
    def info(message, color=''):
        """
        These messages can be used to notify, provide statistics, etc.

        For presenting task steps, use Console.task() instead

        For handled or potential errors use Console.warning() instead
        """
        message = Console.format_message(
            message,
            color,
            MessageType.info,
        )
        Console.write(message)

    @staticmethod
    def warning(message, color=''):
        """
        Deprecation notices, handled errors, or using fallbacks are good
        candidates to be warning messages.
        """
        message = Console.format_message(
            message,
            color,
            MessageType.warning,
        )
        Console.write(message)

    @staticmethod
    def error(message, color=''):
        """
        Error messages are used, when something breaks or fails, or if the user
        input cannot be processed properly.

        If the user input is at least partially usable, Console.warning() is a
        good candidate.
        """
        message = Console.format_message(
            message,
            color,
            MessageType.error,
        )
        Console.write(message, channel=sys.stderr)

    @staticmethod
    def success(message, color=''):
        """
        Successful actions, script completions are good for success messages.
        """
        message = Console.format_message(
            message,
            color,
            MessageType.success,
        )
        Console.write(message)

    @staticmethod
    def decision(message, color=''):
        """
        If you are asking a user for input, or to make a decision, it's a good
        idea to use Console.decision() to print the question itself, before
        expecting the input.
        """
        message = Console.format_message(
            message,
            color,
            MessageType.decision,
        )
        Console.write(message)

    @staticmethod
    def task(message, color=''):
        """
        If you have multiple steps, this method is a good candidate to print
        each step. If you prefer, you can put a success/warning/error message
        after a task has finished.
        """
        message = Console.format_message(
            message,
            color,
            MessageType.task,
        )
        Console.write(message)

    @staticmethod
    def new_line():
        """
        Prints an empty line
        """
        Console.write('')

    @staticmethod
    def format_message(message, color=u'', message_type=u''):
        """
        Prepends the message type and color to the message itself,
        then terminates it with the reset operator.
        """
        return u'{type}{color} {message}{terminator}'.format(
            type=message_type,
            color=color,
            message=message,
            terminator=MessageColor.end,
        )

    @staticmethod
    def command_line_input(question):
        """
        Allows you to ask for a user input, and takes care of deciding
        which method to use based on the version of Python you are executing
        the script with
        :param question: Can be a Console message type, or a raw string
        :return:
        """
        python_version = platform.python_version()
        if str(python_version)[0] == '2':
            # noinspection PyCompatibility
            answer = raw_input(question)
        else:
            answer = input(question)
        return answer