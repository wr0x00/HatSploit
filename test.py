from hatsploit.core.cli.badges import Badges
class table(object):
    def __init__(self) -> None:
        #super().__init__()

        self.badges = Badges()
        self.badges.print_empty("fuck")

a=Badges()
'''
a.print_error('fuck')           #[-] fuck
a.print_process('fuck')         #[*] fuck
a.print_success('fuck')         #[+] fuck
a.print_warning('fuck')         #[!] fuck
a.print_usage('fuck')           #Usage: fuck
'''
a.print_information('lklllj')
bools=a.input_question('asdjklasjdlkaksldjlkasjd')
print(bools)