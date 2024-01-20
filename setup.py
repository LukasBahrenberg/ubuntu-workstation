import subprocess
import getpass

# delete setup script
subprocess.run('sudo rm -rf /os.py', shell=True)

# install rust
subprocess.run('curl https://sh.rustup.rs -sSf | sh -s -- -y', shell=True)
# subprocess.run('cargo install --no-default-features --force cargo-make', shell=True)

# install current nodejs version
subprocess.run('curl -fsSL https://deb.nodesource.com/setup_current.x | sudo -E bash -', shell=True)    
subprocess.run('sudo apt-get update', shell=True)
subprocess.run('sudo apt-get install -y nodejs', shell=True)

# install dotnet
subprocess.run('sudo snap install dotnet-sdk --classic', shell=True)    

# install angular
subprocess.run('sudo npm install -g @angular/cli', shell=True)

# install conda 
subprocess.run('wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh', shell=True)
subprocess.run('bash Miniconda3-latest-Linux-x86_64.sh -b', shell=True)
subprocess.run('rm Miniconda3-latest-Linux-x86_64.sh', shell=True)

# install poetry
subprocess.run('curl -sSL https://install.python-poetry.org | python3 -', shell=True)
subprocess.run('export PATH=$HOME/.local/bin:$PATH', shell=True)
subprocess.run('echo "export PATH=$HOME/.local/bin:$PATH" >> ~/.bashrc', shell=True)
subprocess.run('poetry config virtualenvs.in-project true --global', shell=True)

# install go
subprocess.run('sudo snap install go --classic', shell=True)

#install gcloudcli
subprocess.run('curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg', shell=True)
subprocess.run('echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list', shell=True)
subprocess.run('sudo apt-get update && sudo apt-get install google-cloud-cli', shell=True)

# create python link for python3 in Ubuntu
subprocess.run('sudo ln -s /usr/bin/python3 /usr/bin/python', shell=True)

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

subprocess.run('ssh-keygen -t ed25519 -b 4096 -C "bahrenberg@donex.io" -f ".ssh/bitbucket"', shell=True)
subprocess.run('ssh-add ~/.ssh/bitbucket', shell=True)
subprocess.run('cat ~/.ssh/bitbucket.pub', shell=True)
