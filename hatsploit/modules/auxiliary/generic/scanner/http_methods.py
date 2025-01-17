"""
This module requires HatSploit: https://hatsploit.com
Current source: https://github.com/EntySec/HatSploit
"""

from hatsploit.lib.module.basic import *
from pex.proto.http import HTTPClient
from pex.proto.tcp import TCPTools


class HatSploitModule(HTTPClient, Module, TCPTools):
    def __init__(self):
        super().__init__()

        self.details.update({
            'Category': 'auxiliary',
            'Name': 'HTTP Methods',
            'Module': 'auxiliary/generic/scanner/http_methods',
            'Authors': ['Noah Altunian (naltun) - contributor'],
            'Description': 'Find supported HTTP methods on a server',
            'Platform': 'generic',
            'Rank': 'low',
        })

        self.host = IPv4Option(None, "Remote host.", True)

        self.http_methods = [
            'CONNECT',
            'DELETE',
            'GET',
            'HEAD',
            'OPTIONS',
            'PATCH',
            'POST',
            'PUT',
            'TRACE',
        ]

        self.supported_methods = {'80': [], '443': [], 'count': 0}

    def run(self):
        remote_host = self.host.value

        self.print_process(f'Scanning {remote_host}...')
        for port in [80, 443]:
            if self.check_tcp_port(remote_host, port):
                for method in self.http_methods:
                    resp = self.http_request(
                        method=method,
                        host=remote_host,
                        port=port,
                        path='/',
                    )

                    if resp:
                        if resp.status_code == 200:
                            self.supported_methods[str(port)].append(method)
                            self.supported_methods['count'] += 1
        if len(self.supported_methods['80']):
            self.print_success(
                f'Port 80 Supported Methods: {" ".join(self.supported_methods["80"])}'
            )
        if len(self.supported_methods['443']):
            self.print_success(
                f'Port 443 Supported Methods: {" ".join(self.supported_methods["443"])}'
            )
        if self.supported_methods['count'] == 0:
            self.print_error('No supported HTTP methods detected')
