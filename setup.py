import subprocess
import os
from dotenv import load_dotenv
import getpass

# delete setup script
subprocess.run('sudo rm -rf /os.py', shell=True)

# load environment variables
load_dotenv()

# install Rust
subprocess.run('curl https://sh.rustup.rs -sSf | sh -s -- -y', shell=True)
subprocess.run('cargo install --no-default-features --force cargo-make', shell=True)


# get user name
user = getpass.getuser()

# reset permissions
subprocess.run('sudo chown -R {}:sudo /home/{}'.format(user, user), shell=True)


# assign env variables
gituser = os.getenv('GITUSER')
gitemail = os.getenv('GITEMAIL')

# setup git
subprocess.run('ssh-keygen -t ed25519 -C \"{}\"'.format(gitemail), shell=True)
subprocess.run('ssh-add ~/.ssh/id_ed25519', shell=True)
subprocess.run('git config --global user.name "{}"'.format(gituser), shell=True)
subprocess.run('git config --global user.email "{}"'.format(gitemail), shell=True)
subprocess.run('cat ~/.ssh/id_ed25519.pub', shell=True)
