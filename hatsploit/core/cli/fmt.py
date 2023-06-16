import re

class FMT(object):
    """ Subclass of hatsploit.core.cli module.

    This subclass of hatsploit.core.cli module is intended for
    providing tools for formatting.         #hatsploit.core.cli的子类用于格式化的工具
    """

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def format_commands(command: str) -> list:      
        """ Split command by space and commas.  #空格分割字符串
        
        :param str command: command to split
        :return list: list of commands
        """

        commands = re.split(''' (?=(?:[^'"]|'[^']*'|"[^"]*")*$)''', command)
        formatted_commands = []

        for command in commands:
            if command:
                formatted_commands.append(command.strip('"').strip("'"))

        return formatted_commands
