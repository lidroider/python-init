# Python init project

Python init project with poetry, yapf formatter, precommit hook to format, pylint
Enjoy it

## How to setup

Step 1: Run in terminal

```bash
pip3 install -U pipenv
pipenv sync --dev
pipenv shell
```

Step 2: Run `poetry show -v` to get python path and config your editor

Ex: Append it into `.vscode/settings.json` like

```
{
    "python.linting.enabled": true,
    "python.formatting.provider": "yapf",
    "python.pythonPath": "/home/cec/.local/share/virtualenvs/capturer-n17q30yo/bin/python"
}
```

Step 3: Update pylint path

Ex: Append project absolute path to `.vscode/settings.json` like

```
{
    "python.linting.enabled": true,
    "python.formatting.provider": "yapf",
    "python.pythonPath": "/home/cec/.local/share/virtualenvs/capturer-n17q30yo/bin/python",
    "python.linting.pylintArgs": [
        "--init-hook",
        "import sys; sys.path.append('/absolute/path/of/project')"
    ]
}
```

Remember to DO NOT commit `.vscode/settings.json` about changing of python path config

Step 4: Run command to register git hook auto check format code with yapf

```bash
pre-commit install
```

## How to build

```bash
poetry export --without-hashes --without dev --format=requirements.txt > requirements.txt
docker build .
```
