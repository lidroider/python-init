# Python init project



Python init project with pipenv, yapf formatter, precommit hook to format, pylint
Enjoy it


## How to setup

Step 1: Run in terminal

```bash
pip3 install -U pipenv
pipenv sync --dev
pipenv shell
```

Step 2: Run `pipenv --py` to get python path and config your editor

Ex: VS Code append it into `.vscode/settings.json` like

```
{
    "python.linting.enabled": true,
    "python.formatting.provider": "yapf",
    "python.pythonPath": "/home/cec/.local/share/virtualenvs/capturer-n17q30yo/bin/python"
}
```

Remember to DO NOT commit `.vscode/settings.json` about changing of python path config

Step 3: Run command to register git hook auto check format code with yapf

```bash
pre-commit install
```


## How to build
```bash
pipenv lock --requirements > requirements.txt
docker build .
```
