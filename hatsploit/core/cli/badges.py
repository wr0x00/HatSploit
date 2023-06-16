
import os

from hatsploit.core.base.io import IO


class Badges(object):
    """ Subclass of hatsploit.core.cli module.

    This subclass of hatsploit.core.cli module is intended for
    providing various printing interfaces.
    """

    def __init__(self) -> None:
        super().__init__()

        self.io = IO()

    def print_empty(self, message: str = '', start: str = '%remove', end: str = '%newline') -> None:
        """ Print string with empty start.  

        :param str message: message to print
        :param str start: string to print before the message
        :param str end: string to print after the message
        :return None: None
        """

        self.io.print(message, start, end)

    def print_usage(self, message: str, start: str = '%remove', end: str = '%newline') -> None:
        """ Print string with Usage: start.

        :param str message: message to print
        :param str start: string to print before the message
        :param str end: string to print after the message
        :return None: None
        """

        self.print_empty(f"Usage: {message}", start, end)

    def print_process(self, message: str, start: str = '%remove', end: str = '%newline') -> None:
        """ Print string with [*] start.

        :param str message: message to print
        :param str start: string to print before the message
        :param str end: string to print after the message
        :return None: None
        """

        self.print_empty(f"%bold%blue[*]%end {message}", start, end)

    def print_success(self, message: str, start: str = '%remove', end: str = '%newline') -> None:
        """ Print string with [+] start.

        :param str message: message to print
        :param str start: string to print before the message
        :param str end: string to print after the message
        :return None: None
        """

        self.print_empty(f"%bold%green[+]%end {message}", start, end)

    def print_error(self, message: str, start: str = '%remove', end: str = '%newline') -> None:
        """ Print string with [-] start.

        :param str message: message to print
        :param str start: string to print before the message
        :param str end: string to print after the message
        :return None: None
        """

        self.print_empty(f"%bold%red[-]%end {message}", start, end)

    def print_warning(self, message: str, start: str = '%remove', end: str = '%newline') -> None:
        """ Print string with [!] start.

        :param str message: message to print
        :param str start: string to print before the message
        :param str end: string to print after the message
        :return None: None
        """

        self.print_empty(f"%bold%yellow[!]%end {message}", start, end)

    def print_information(self, message: str, start: str = '%remove', end: str = '%newline') -> None:
        """ Print string with [i] start.

        :param str message: message to print
        :param str start: string to print before the message
        :param str end: string to print after the message
        :return None: None
        """

        self.print_empty(f"%bold%white[i]%end {message}", start, end)

    def input_empty(self, message: str = '', start: str = '%remove%end', end: str = '%end') -> list:
        """ Input string with empty start.

        :param str message: message to print
        :param str start: string to print before the message
        :param str end: string to print after the message
        :return list: read string separated by space and commas
        """

        return self.io.input(message, start, end)

    def input_question(self, message: str, start: str = '%remove%end', end: str = '%end') -> list:
        """ Input string with [?] start.

        :param str message: message to print
        :param str start: string to print before the message
        :param str end: string to print after the message
        :return list: read string separated by space and commas
        """

        return self.input_empty(f"%bold%white[?]%end {message}", start, end)

    def input_arrow(self, message: str, start: str = '%remove%end', end: str = '%end') -> list:
        """ Input string with [>] start.

        :param str message: message to print
        :param str start: string to print before the message
        :param str end: string to print after the message
        :return list: read string separated by space and commas
        """

        return self.input_empty(f"%bold%white[>]%end {message}", start, end)
