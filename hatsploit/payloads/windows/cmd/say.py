#!/usr/bin/env python3

#
# This payload requires HatSploit: https://hatsploit.netlify.app
# Current source: https://github.com/EntySec/HatSploit
#

from hatsploit.lib.payload import Payload


class HatSploitPayload(Payload):
    details = {
        'Name': "Windows Say",
        'Payload': "windows/cmd/say",
        'Authors': [
            'Ivan Nikolsky (enty8080) - payload developer'
        ],
        'Description': "Say payload for Windows.",
        'Architecture': "cmd",
        'Platform': "windows",
        'Rank': "low",
        'Type': "one_side"
    }

    options = {
        'MESSAGE': {
            'Description': "Message to say.",
            'Value': "Hello, Friend!",
            'Type': None,
            'Required': True
        }
    }

    def run(self):
        message = self.parse_options(self.options)

        source = (
            "Add-Type -AssemblyName System.speech;"
            "$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer;"
            f"$speak.Speak('{message}')"
        )

        payload = f"powershell -w hidden -nop -c {source}"
        return payload