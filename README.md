# poetry-science-env

Instrucitons for setting up a new EC2

## Install pyenv

`curl https://pyenv.run | bash`


Add the following to `~/.bashrc`
```
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

run `source ~/.bashrc`

## Install poetry

`curl -sSL https://install.python-poetry.org | python3 -`

Add the following to `~/.bashrc`

```
export PATH="/home/ubuntu/.local/bin:$PATH"
```

run `source ~/.bashrc`

## Install compiler

```
sudo apt update; sudo apt install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

## Install & setup gh
```
sudo apt install gh
gh auth login
```

## Setup sci env
```
git clone https://github.com/gvoronov/poetry-science-env.git
cd poetry-science-env/
pyenv local 3.9
poetry install
poetry run python -m ipykernel install --user --name sci-env
```

Can also install with any subset of the following optional dependencies

`poetry install --with chemistry,torch,metabolomics`

## Setup scripts
`mkdir ~/scripts`

If `/efs` doesn't exist run `sudo mkdir /efs`

Create `~/scripts/mount_efs.sh` with following contents
```
sudo mount -t nfs4 \
-o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,\
noresvport fs-3bb6048f.efs.us-east-1.amazonaws.com:/ /efs
```

Create `~/scripts/launch_jupyter.sh` with following contents

* on a standard EC2
```
jupyter notebook --no-browser --notebook-dir /efs/gennadyvoronov/jupyter --port <PORT>
```

* on DS-EC2
```
jupyter-nbclassic --no-browser --notebook-dir /efs/gennadyvoronov/jupyter --port 8859
```

Grant execute permissions

```
chmod u+x ~/scripts/mount_efs.sh
chmod u+x ~/scripts/launch_jupyter.sh
```