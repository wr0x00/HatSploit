"""
MIT License

Copyright (c) 2020-2023 EntySec

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
import subprocess
import sys

from typing import Any

from hatsploit.core.cli.badges import Badges
from hatsploit.core.cli.fmt import FMT
from hatsploit.core.cli.tables import Tables
from hatsploit.lib.jobs import Jobs
from hatsploit.lib.modules import Modules
from hatsploit.lib.show import Show
from hatsploit.lib.storage import LocalStorage


class Execute(object):
    """ Subclass of hatsploit.core.base module.

    This subclass of hatsploit.core.base module is intended for
    providing interfaces for executing commands in HatSploit interpreter.
    """

    def __init__(self) -> None:
        super().__init__()

        self.jobs = Jobs()
        self.fmt = FMT()
        self.badges = Badges()
        self.tables = Tables()
        self.local_storage = LocalStorage()
        self.modules = Modules()
        self.show = Show()

    def execute_command(self, command: list) -> None:
        """ Execute command.

        :param list command: command with arguments
        :return None: None
        """

        if command:
            if not self.execute_builtin_method(command):
                if not self.execute_core_command(command):
                    if not self.execute_module_command(command):
                        if not self.execute_plugin_command(command):
                            self.badges.print_error(
                                f"Unrecognized command: {command[0]}!"
                            )

    def execute_builtin_method(self, command: list) -> bool:
        """ Execute command as interpreter builtin method.

        :param list command: command with arguments
        :return bool: status, True if success else False

        ?用于显示所有加载的接口命令。

        &用于在后台执行命令。

        !用于执行系统命令。
        """

        if command[0][0] == '#':
            return True

        if command[0][0] == '?':
            self.show.show_all_commands()
            return True

        if command[0][0] == '&':
            command[0] = command[0][1:]

            self.jobs.create_job(
                command[0], None, self.execute_command, [command], hidden=True
            )

            return True

        if command[0][0] == '!':
            if len(command[0]) > 1:
                command[0] = command[0].replace('!', '', 1)
                self.execute_system(command)

            else:
                self.badges.print_usage("!<command>")

            return True
        return False

    def execute_system(self, command: list) -> None:
        """ Execute command as system.

        :param list command: command with arguments
        :return None: None
        """

        self.badges.print_process(f"Executing system command: {command[0]}\n")
        try:
            subprocess.call(command)
        except Exception:
            self.badges.print_error(
                f"Unrecognized system command: {command[0]}!")

    def execute_custom_command(self, command: list, handler: dict) -> bool:
        """ Execute command via custom handler.

        Note: handler is a dictionary containing command names as keys and
        command objects as items.

        :param list command: command with arguments
        :param dict handler: handler to use
        :return bool: status, True if success else False
        """

        if handler:
            if command[0] in handler:
                handle = handler[command[0]]

                if not self.check_arguments(command, handle.details):
                    self.parse_usage(handle.details)
                else:
                    handle.run(len(command), command)

                return True
        return False

    @staticmethod
    def check_arguments(command: list, details: dict) -> bool:
        """ Check if arguments correct for command.

        :param list command: command with arguments
        :param dict details: dictionary of command details
        :return bool: status, True if correct else False
        """

        if (len(command) - 1) < details['MinArgs']:
            return False

        if 'Options' in details:
            if len(command) > 1:
                if command[1] in details['Options']:
                    if (len(command) - 2) < len(
                            details['Options'][command[1]][0].split()
                    ):
                        return False
                else:
                    return False

        if len(command) > 1:
            if command[1] == '?':
                return False

        return True

    def parse_usage(self, details: dict) -> None:
        """ Print usage for specific command details.

        :param dict details: dictionary of command details
        :return None: None
        """

        self.badges.print_usage(details['Usage'])

        if 'Options' in details:
            headers = ('Option', 'Arguments', 'Description')
            data = []

            for option in details['Options']:
                info = details['Options'][option]
                data.append((option, info[0], info[1]))

            self.tables.print_table('Options', headers, *data)

    def execute_core_command(self, command: list) -> bool:
        """ Execute core command.

        :param list command: command with arguments
        :return bool: status, True if success else False
        """

        return self.execute_custom_command(
            command, self.local_storage.get("commands"))

    def execute_module_command(self, command: list) -> bool:
        """ Execute current module command.

        :param list command: command with arguments
        :return bool: status, True if success else False
        """

        module = self.modules.get_current_module()

        if module:
            if hasattr(module, "commands"):
                if command[0] in module.commands:
                    details = module.commands[command[0]]
                    self.parse_and_execute_command(command, details, module)

                    return True
        return False

    def execute_plugin_command(self, command: list) -> bool:
        """ Execute loaded plugin command.

        :param list command: command with arguments
        :return bool: status, True if success else False
        """

        return self.execute_custom_plugin_command(
            command, self.local_storage.get("loaded_plugins")
        )

    def execute_custom_plugin_command(self, command: list, plugins: dict) -> bool:
        """ Execute custom plugin command.

        :param list command: command with arguments
        :param dict plugins: plugins where to search for command
        :return bool: status, True if success else False
        """

        if plugins:
            for plugin in plugins:
                plugin = plugins[plugin]

                for label in plugin.commands:
                    if command[0] in plugin.commands[label]:
                        details = plugin.commands[label][command[0]]

                        self.parse_and_execute_command(
                            command, details, plugin
                        )

                        return True
        return False

    def parse_and_execute_command(self, command: list, details: dict, handle: Any) -> None:
        """ Parse command details and execute handle.

        :param list command: command with arguments
        :param dict details: command details
        :param Any handle: something that has command name as an
        executable attribute, entry point
        :return None: None
        """

        if hasattr(handle, command[0]):
            if not self.check_arguments(command, details):
                self.parse_usage(details)
            else:
                getattr(handle, command[0])(len(command), command)
        else:
            self.badges.print_error("Failed to execute command!")
