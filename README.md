# poetry-science-env

Instrucitons for setting up a new EC2

## install pyenv
`curl https://pyenv.run | bash`


Add the following to ~/.bashrc
```
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

# install poetry
`curl -sSL https://install.python-poetry.org | python3 -`
Add the following to ~/.bashrc

```
export PATH="/home/ubuntu/.local/bin:$PATH"
```

# install compiler
sudo apt update; sudo apt install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

# install & setup gh
sudo apt install gh
gh auth login

# setup sci env
git clone https://github.com/gvoronov/poetry-science-env.git
cd poetry-science-env/
pyenv local 3.9
poetry run python -m ipykernel install --user --name sci-env

# setup scripts
~/scripts/launch_jupyter.sh
~/scripts/mount_efs.sh
