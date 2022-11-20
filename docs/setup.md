## Introduction of the lab env

- Python v3.10
- Poetry v1.2+
- CycloneDX v1.4
- Docker v20+
- VS Code + Dev Container
  - Dev Container: `python:3.10` (Debian 11)
  - Installed packages:
    - git
    - curl
    - wget
    - [HTTPie](https://httpie.io/)
    - jq
    - [microsoft/sbom-tool]()https://github.com/microsoft/sbom-tool)
    - [anchore/syft](https://github.com/anchore/syft)

### Directory structure

| Path                                                     | Desc.                               |
|----------------------------------------------------------|-------------------------------------|
| /app/log4j-vulnerable-app/gradle.lockfile                | A Gradle lock file                  |
| /app/python-vulnerable-app/requirements.txt              | A Pip lock file                     |
| /workspaces/jsac2023                                     | A VS Code workspace                 |
| /home/vscode/.cache/pypoetry/virtualenvs/jsac2023-py3.10 | A virtualenv path for the workspace |

### How to setup

```bash
git clone https://github.com/ninoseki/jsac2023
code jsac2023
```

Click the bottom left corner button (Open a Remote Window) of VS Code.

![](https://i.imgur.com/EskbfTT.png)

And select "Reopen in Container".

![](https://i.imgur.com/NYNr49G.png)

It will start a dev container automatically.

See [VS Code: Quick start: Open an existing folder in a container](https://code.visualstudio.com/docs/devcontainers/containers#_quick-start-open-an-existing-folder-in-a-container) for more details.

### How to confirm whether you are ready or not

```bash
# in the host machine
$ docker ps | grep vsc-jsac2023-
2aaad5c554b1   vsc-jsac2023-8fb1a747384eb718800c866a3ca10992   "/bin/sh -c 'echo Co…"   About a minute ago   Up About a minute             admiring_chandrasekhar
```

```bash
# in the dev container

# check poetry is installed
$ poetry --version
Poetry (version 1.2.2)

# check pytest
$pytest --version
pytest 7.2.0

# check Python app is running
$ curl localhost:8000
{"message":"hello, world!"}

# check Java app is running
$ curl localhost:8080
{"timestamp":"2022-11-12T07:10:56.045+00:00","status":400,"error":"Bad Request","path":"/"}
```

Note that Python requirements for the hands-on challenges are installed in a vritual environment via Poetry.

So you have to use `poetry run` prefix or `poetry shell`.

```bash
$ poetry run python ...
$ poetry run pytest ...
# or
$ poetry shell
$ python ...
$ pytest
```
