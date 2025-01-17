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

from pex.type import Type
from pex.socket import Socket

from hatsploit.lib.modules import Modules
from hatsploit.lib.payloads import Payloads
from hatsploit.lib.encoders import Encoders
from hatsploit.lib.sessions import Sessions

from hatsploit.lib.options import Option


class OptionResolver(Option):
    """ Subclass of hatsploit.lib module.

    This subclass of hatsploit.lib module is a wrapper for Option
    implementation which extends basic class allowing to call external
    methods like Modules, Payloads, Encoders or Sessions.
    """

    def __init__(self, *args, **kwargs):
        Option.__init__(self, *args, **kwargs)

        self.modules = Modules()
        self.payloads = Payloads()
        self.encoders = Encoders()
        self.sessions = Sessions()


class IPv4Option(OptionResolver):
    def set(self, value):
        self.check('IPv4', Type().types['ipv4'], value)
        self.value = value

        self.little = Socket().pack_host(self.value)
        self.big = Socket().pack_host(self.value, 'big')


class IPv6Option(OptionResolver):
    def set(self, value):
        self.check('IPv6', Type().types['ipv6'], value)
        self.value = value


class IPOption(OptionResolver):
    def set(self, value):
        self.check('IP', Type().types['ip'], value)
        self.value = value


class MACOption(OptionResolver):
    def set(self, value):
        self.check('MAC', Type().types['mac'], value)
        self.value = value


class IPv4CIDROption(OptionResolver):
    def set(self, value):
        self.check('IPv4 CIDR', Type().types['ipv4_cidr'], value)
        self.value = value


class IPv6CIDROption(OptionResolver):
    def set(self, value):
        self.check('IPv6 CIDR', Type().types['ipv6_cidr'], value)
        self.value = value


class PortOption(OptionResolver):
    def set(self, value):
        self.check('port', Type().types['port'], value)
        self.value = int(value)

        self.little = Socket().pack_port(self.value)
        self.big = Socket().pack_port(self.value, 'big')


class PortRangeOption(OptionResolver):
    def set(self, value):
        self.check('port range', Type().types['port_range'], value)
        self.value = value


class NumberOption(OptionResolver):
    def set(self, value):
        self.check('number', Type().types['number'], value)
        self.value = value


class IntegerOption(OptionResolver):
    def set(self, value):
        self.check('integer', Type().types['integer'], value)
        self.value = int(value)


class FloatOption(OptionResolver):
    def set(self, value):
        self.check('float', Type().types['float'], value)
        self.value = float(value)


class BooleanOption(OptionResolver):
    def set(self, value):
        self.check('boolean', Type().types['boolean'], value)

        if value.lower() in ['y', 'yes']:
            self.value = True
        else:
            self.value = False


class PayloadOption(OptionResolver):
    def set(self, value):
        value = self.modules.find_shorts('payload', value)
        module = self.modules.get_current_module()

        if module:
            if self.payloads.check_module_compatible(value, module):
                module_name = module.details['Module']

                self.payloads.add_payload(module_name, value)

                if 'Payload' not in module.details:
                    module.details['Payload'] = {}

                module.details['Payload']['Value'] = value

                self.payload = self.payloads.get_current_payload(module)
                self.value = value

                return

        raise RuntimeError("Invalid option value, expected valid payload!")


class EncoderOption(OptionResolver):
    def set(self, value):
        value = self.modules.find_shorts('encoder', value)
        module = self.modules.get_current_module()
        payload = self.payloads.get_current_payload(module)

        if module and payload:
            if self.encoders.check_payload_compatible(value, payload):
                module_name = module.details['Module']
                payload_name = payload.details['Payload']

                self.encoders.add_encoder(module_name, payload_name, value)

                if 'Encoder' not in payload.details:
                    payload.details['Encoder'] = {}

                payload.details['Encoder']['Value'] = value

                self.encoder = self.encoders.get_current_encoder(module, payload)
                self.value = value

                return

        raise RuntimeError("Invalid option value, expected valid encoder!")


class SessionOption(OptionResolver):
    def __init__(self, *args, platforms: list = [], type: str = '', **kwargs):
        super(OptionResolver, self).__init__(*args, **kwargs)

        self.platforms = platforms
        self.type = type

    def set(self, value):
        value = int(value)
        module = self.get_current_module()

        if module:
            platform = module.details['Platform']

            if not self.platforms:
                if not self.sessions.check_exist(value, platform, self.type):
                    raise RuntimeError("Invalid value, expected valid session!")
            else:
                session = 0

                for platform in self.platforms:
                    if self.sessions.check_exist(value, platform.strip(), self.type):
                        session = 1
                        break

                if not session:
                    raise RuntimeError("Invalid value, expected valid session!")
        else:
            raise RuntimeError("Invalid value, expected valid session!")

        self.value = value
        self.session = self.sessions.get_session(value)
