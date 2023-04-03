# This script is designed to be run as root from a brand new Linux installation 
# As root user, commands would not need to be run as sudo. This makes it testable, however, for non-root users and still works for the root user.

import subprocess
import os
from dotenv import load_dotenv
import getpass

# load environment variables
load_dotenv()

# assign env variables
gituser = os.getenv('GITUSER')
gitemail = os.getenv('GITEMAIL')

# setup git
subprocess.run('ssh-keygen -t ed25519 -C \"{}\"'.format(gitemail), shell=True)
subprocess.run('ssh-add ~/.ssh/id_ed25519', shell=True)
subprocess.run('git config --global user.name "{}"'.format(gituser), shell=True)
subprocess.run('git config --global user.email "{}"'.format(gitemail), shell=True)
subprocess.run('cat ~/.ssh/id_ed25519.pub', shell=True)

# get user name
user = getpass.getuser()

# delete setup script
subprocess.run('sudo rm -rf /os.py', shell=True)

# reset permissions
subprocess.run('sudo chown -R {}:sudo /home/{}'.format(user, user), shell=True)