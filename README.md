# poetry-science-env

Instructions for setting up a new EC2

## Install compiler

```
sudo apt update; sudo apt install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

If running an instance with GPUs run the following as well to install CUDA.

```
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.0-1_all.deb
sudo dpkg -i cuda-keyring_1.0-1_all.deb
sudo apt-get update
sudo apt-get -y install cuda
```

## Install pyenv

```
curl https://pyenv.run | bash
```

Add the following to `~/.bashrc`

```
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

Run `source ~/.bashrc`, then install python.

```
pyenv install 3.9.13
```

## Install poetry

```
curl -sSL https://install.python-poetry.org | python3 -
```

Add the following to `~/.bashrc`

```
export PATH="/home/ubuntu/.local/bin:$PATH"
```

run `source ~/.bashrc`

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
poetry env use 3.9
poetry install
```

Can also install with any subset of the following optional dependencies

```
poetry install --with chemistry,torch
```

### Setup notebook kernels

If a jupyter notebook kernel based on this environnement is required, one can be created via

```
poetry run python -m ipykernel install --user --name sci-env
```

Kernels can be removed via

```
poetry run jupyter kernelspec uninstall unwanted-kernel
```

### Setup common packages

Finally if needed add some some typical packages I work with

```
poetry add git+https://github.com/enveda/metabolomics.git#gv-dev
```

```
poetry add git+https://github.com/enveda/numerical-mz.git#gv-dev
```

```
poetry add git+https://github.com/enveda/molecular-library-search.git#gv-dev
```

```
poetry add git+https://github.com/enveda/spectral-similarity.git#gv-dev
```

```
poetry add git+https://github.com/enveda/ms2-inference.git#gv-dev
```

```
poetry add git+https://github.com/enveda/denovo-structure-prediction.git#gv-dev
```

```
poetry add git+https://github.com/enveda/specformers.git#gv-dev
```

```
poetry add git+https://github.com/enveda/spectral-inference-zoo.git#gv-dev
```

```
poetry add git+https://github.com/enveda/molecular-graph-edit.git#gv-dev
```

## Setup AWS

First setup AWS CLI

```
sudo apt install awscli
```

Then run

```
aws configure
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
sudo mkdir /efs
chmod u+x scripts/mount_efs.sh
```

Finally mount efs with

```
./scripts/mount_efs.sh
```

## Jupyter

### Setup 

Copy `/path/poetry-science-env/configs/jupyter_notebook_config.py` to `~/.jupyter/jupyter_notebook_config.py`. From the directory that `poetry-science-evn` is cloned into run

```
mkdir ~/.jupyter
cp configs/jupyter_notebook_config.py ~/.jupyter/jupyter_notebook_config.py
```

### Launch

First navigate to the directory that `poetry-science-evn` is cloned into and then if necessary,

```
chmod u+x scripts/launch_jupyter.sh
```

Then (typically through `screen`)

```
./scripts/launch_jupyter.sh <PORT>
```

## Update permissions

Sometimes e.g. after a fresh git pull need to reenable execute permissions for the following scritps.

```
chmod u+x scripts/mount_efs.sh
chmod u+x scripts/launch_jupyter.sh
```