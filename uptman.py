#!/usr/bin/python3
import requests, argparse, os
def install(package):
    maintainer = package.split('/')[0]
    name = package.split('/')[1]
    print('Installing', name)
    requirements = requests.get(f'https://github.com/{maintainer}/{name}/requirements.txt')
    if requirements.status_code == 200:
        requirements_list = requirements.content.split('\n')
    else:
        print('Error 404 - requirements.txt')
        requirements_list = []
    print('Following package be installed:')
    print('   ', name)
    print('Requirements:')
    print('   ', requirements_list)
    if requirements_list:
        for req in requirements_list:
            install(req)
    else:
        pass
    try:
        os.system(f'git clone https://github.com/{maintainer}/{name}')
    except:
        print('Error')
    print('Installed', name)

def meow():
    print("""
( meoW )
       \\
         \\ 
           ^ _ ^
          (o   o)
          \\  w  /           ^
            \\  \\           //
             _------------//
             | |________| |
             | |        | |
             _\\|        _\\|
     -- Have you meowed today? -- 
          0x6d0x650x6f0x77
""")

parser = argparse.ArgumentParser()
parser.add_argument('option', help="install option (install u/p)") #install/update
parser.add_argument('package', help="package name (e.g. microsoft/vscode)")
args = parser.parse_args()
if args.option == "install":
    install(args.package)
elif args.option == 'meow':
    meow()