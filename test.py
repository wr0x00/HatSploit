from hatsploit.core.cli.badges import Badges
import re
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
'''
a.print_information('lklllj')
bools=a.input_question('asdjklasjdlkaksldjlkasjd')
print(bools)
'''

#commands=re.split(''' (?=(?:[^'"]|'[^']*'|"[^"]*")*$)''', input(':'))
'''
formatted_commands=[]
for command in commands:
    if command:
        formatted_commands.append(command.strip('"').strip("'"))
print(formatted_commands)
'''
'''
globals()
from colorscript import ColorScript
cl=ColorScript()
print(cl.libreadline(input(':')))


@staticmethod修饰的类被调用不用实例化

判断一个对象是否是一个已知的类型：
        - type() 不会认为子类是一种父类类型，不考虑继承关系。
        - isinstance() 会认为子类是一种父类类型，考虑继承关系。

'''
import subprocess
subprocess.call("ls")