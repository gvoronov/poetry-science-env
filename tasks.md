```
git clone https://github.com/gvoronov/poetry-science-env.git <NAME>
cd <NAME>
pyenv local 3.9
poetry env use 3.9
EDIT pyproject.toml
poetry install
poetry run python -m ipykernel install --user --name <NAME>
```

```
poetry add git+https://github.com/enveda/specformers.git#gv-dev
```

```
poetry add git+https://github.com/enveda/spectral-inference-zoo.git#gv-dev
```