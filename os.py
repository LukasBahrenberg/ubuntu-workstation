import subprocess
import random
import string

# updates & upgrades
subprocess.run('apt-get update', shell=True)
subprocess.run('apt-get upgrade -y', shell=True)
subprocess.run('apt update', shell=True)
subprocess.run('apt upgrade -y', shell=True)

# installations
subprocess.run('apt install -y build-essential', shell=True)
subprocess.run('apt install -y libssl-dev', shell=True)
subprocess.run('apt install -y whois', shell=True)
subprocess.run('apt-get install -y pkg-config', shell=True)

subprocess.run('apt install -y fail2ban', shell=True)
subprocess.run('apt-get install -y git', shell=True)

subprocess.run('apt-get install -y python3-pip', shell=True)
subprocess.run('pip3 install requests', shell=True)
subprocess.run('pip3 install python-dotenv', shell=True)

subprocess.run('apt install -y software-properties-common', shell=True)
subprocess.run('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor --yes -o /etc/apt/trusted.gpg.d/docker-archive-keyring.gpg', shell=True)
subprocess.run('add-apt-repository -y "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"', shell=True)
subprocess.run('apt update', shell=True)
subprocess.run('apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin', shell=True)

subprocess.run('apt install -y snapd', shell=True)
subprocess.run('snap install go --classic', shell=True)

# ufw
subprocess.run('ufw logging on', shell=True)
subprocess.run('ufw allow 22', shell=True) #ssh
subprocess.run('ufw --force enable', shell=True)

# fail2ban
subprocess.run('systemctl enable fail2ban', shell=True)
subprocess.run('systemctl start fail2ban', shell=True)
subprocess.run('systemctl status fail2ban', shell=True)

# create new user
user = input("Enter user name: ")
subprocess.run('adduser --disabled-password --gecos \"\" {}'.format(user), shell=True)
subprocess.run('usermod -aG sudo {}'.format(user), shell=True)

# set password hash, use pwd.py script on seperate machine to generate password
passwordhash = input("Enter user password hash: ")
subprocess.run('printf \'{}:{}\' | sudo chpasswd --encrypted'.format(user, passwordhash), shell=True)

# git repo
subprocess.run('git clone https://github.com/LukasBahrenberg/ubuntu-workstation.git /home/{}/ubuntu-workstation'.format(user), shell=True)

# reset permissions
subprocess.run('chown -R {}:sudo /home/{}'.format(user, user), shell=True)

# switch to user
subprocess.run('su - {}'.format(user), shell=True)
