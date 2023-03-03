"""
This command requires HatSploit: https://hatsploit.com
Current source: https://github.com/EntySec/HatSploit
"""

import sys

from hatsploit.lib.command import Command
from hatsploit.lib.jobs import Jobs
from hatsploit.lib.sessions import Sessions


class HatSploitCommand(Command):
    def __init__(self):
        super().__init__()

        self.jobs = Jobs()
        self.sessions = Sessions()

        self.details = {
            'Category': "core",
            'Name': "exit",
            'Authors': [
                'Ivan Nikolsky (enty8080) - command developer',
            ],
            'Description': "Exit HatSploit Framework.",
            'Usage': "exit",
            'MinArgs': 0,
        }

    def run(self, argc, argv):
        if self.jobs.get_jobs():
            self.print_warning("You have some running jobs.")

            if self.input_question("Exit anyway? [y/N] ")[0].lower() in ['yes', 'y']:
                self.jobs.stop_jobs()
            else:
                return

        if self.sessions.get_sessions():
            self.print_warning("You have some opened sessions.")

            if self.input_question("Exit anyway? [y/N] ")[0].lower() in ['yes', 'y']:
                self.sessions.close_sessions()
            else:
                return

        sys.exit(0)
