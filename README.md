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

```
poetry install --with chemistry,torch,metabolomics
```

## Setup EFS

### Prerequisite: install `amazon-efs-utils` package

If not installed, need to install the `amazon-efs-utils` package. To do so need to clone it

```
git clone https://github.com/aws/efs-utils
```

Then navigate to the directory that contains the `amazon-efs-utils` package.

```
cd /path/efs-utils
```

Finally install the package

```
./build-deb.sh
sudo apt-get -y install ./build/amazon-efs-utils*deb
```

### Mount EFS

First navigate to the directory that `poetry-science-evn` is cloned into. Then just the first time on a new instance
```
mkdir /efs
chmod u+x scripts/mount_efs.sh
```
Finally mount efs with
```
./scripts/mount_efs.sh
```

### Jupyter

## Setup 

Copy local `jupyter_notebook_config.py` to `~/.jupyter/jupyter_notebook_config.py`

## Lauch

First navigate to the directory that `poetry-science-evn` is cloned into and then if necessary,

```
chmod u+x scripts/launch_jupyter.sh
```

Then (typically through `screen`)

```
./scripts/launch_jupyter.sh <PORT>
```

### Old launch

* on a standard EC2
```
jupyter notebook --no-browser --notebook-dir /efs/gennadyvoronov/jupyter --port <PORT>
```

* on DS-EC2
```
jupyter-nbclassic --no-browser --notebook-dir /efs/gennadyvoronov/jupyter --port 8859
```
