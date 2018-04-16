import platform
import time

from command_line_tools.console import Console, MessageColor, MessageType
from command_line_tools.loader import Loader, LoadingFrameSets

if __name__ == '__main__':
    Console.write('\n\n1337 Pentagon Hacking Script v1.3.37\n\n')
    time.sleep(0.75)

    Console.task('Determining Python version')
    time.sleep(0.75)

    python_version = platform.python_version()
    Console.success('Python version passes requirements')
    time.sleep(0.25)

    Console.info('Running on Python %s' % python_version)
    time.sleep(0.75)

    answer = ''
    question = Console.format_message(
        'What exploit type should we try? [any] ',
        message_type=MessageType.decision
    )
    answer = Console.command_line_input(question)

    Console.task('Vulnerability library initialized')
    loader = Loader()
    loader.show(
        'Running vulnerability scan on 188.40.92.77',
        LoadingFrameSets.dots
    )
    time.sleep(3.5)
    loader.complete()

    Console.warning('Unable to find vulnerability, resorting to brute force')
    time.sleep(0.15)

    loader.show('Brute forcing 188.40.92.77/admin', LoadingFrameSets.dots)
    Console.task('Brute forcing initiated')
    time.sleep(2.5)
    loader.complete()

    Console.success('Found valid credentials!\n')
    time.sleep(0.15)

    Console.info('Username: Jeff')
    Console.info('Password: Jeffety Jeff')
    time.sleep(0.5)

    Console.new_line()
    Console.task('Covering up trails')
    Console.error('Unable to perform rm -rf /')
    Console.error('Don\'t take it too seriously!', color=MessageColor.red)
    time.sleep(0.5)

    Console.success('Demonstration was successful')
