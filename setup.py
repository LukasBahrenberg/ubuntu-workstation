import subprocess
import getpass

# delete setup script
subprocess.run('sudo rm -rf /os.py', shell=True)

# install rust
subprocess.run('curl https://sh.rustup.rs -sSf | sh -s -- -y', shell=True)
# subprocess.run('cargo install --no-default-features --force cargo-make', shell=True)

# install current nodejs version
# subprocess.run('curl -fsSL https://deb.nodesource.com/setup_current.x | sudo -E bash -', shell=True)    
subprocess.run('sudo apt-get update', shell=True)
subprocess.run('sudo apt-get install -y nodejs', shell=True)

# install dotnet
subprocess.run('wget https://dot.net/v1/dotnet-install.sh -O dotnet-install.sh', shell=True)    
subprocess.run('chmod +x ./dotnet-install.sh', shell=True)
subprocess.run('./dotnet-install.sh --version latest', shell=True)

# install conda 
subprocess.run('wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh', shell=True)
subprocess.run('bash Miniconda3-latest-Linux-x86_64.sh -b', shell=True)
subprocess.run('rm Miniconda3-latest-Linux-x86_64.sh', shell=True)

# install poetry
subprocess.run('curl -sSL https://install.python-poetry.org | python3 -', shell=True)
subprocess.run('export PATH=$HOME/.local/bin:$PATH', shell=True)
subprocess.run('echo "export PATH=$HOME/.local/bin:$PATH" >> ~/.bashrc', shell=True)
subprocess.run('poetry config virtualenvs.in-project true', shell=True)

# install go
subprocess.run('sudo snap install go --classic', shell=True)

# get user name
user = getpass.getuser()

# reset permissions
subprocess.run('sudo chown -R {}:sudo /home/{}'.format(user, user), shell=True)

# assign env variables
gituser = input("Enter GITUSER: ")
gitemail = input("Enter GITEMAIL: ")

# setup git
subprocess.run('ssh-keygen -t ed25519 -C \"{}\"'.format(gitemail), shell=True)
subprocess.run('ssh-add ~/.ssh/id_ed25519', shell=True)
subprocess.run('git config --global user.name "{}"'.format(gituser), shell=True)
subprocess.run('git config --global user.email "{}"'.format(gitemail), shell=True)
subprocess.run('cat ~/.ssh/id_ed25519.pub', shell=True)
