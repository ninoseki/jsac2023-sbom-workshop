- [Introduction of the lab env](#introduction-of-the-lab-env)
  * [Directory structure](#directory-structure)
- [How to setup](#how-to-setup)
- [How to confirm whether you are ready or not](#how-to-confirm-whether-you-are-ready-or-not)

## Introduction of the lab env

- Python v3.10
- Poetry v1.2+
- CycloneDX v1.4
- Docker v20+
- VS Code + [Remote Development extension pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)
  - Dev Container: `python:3.10` (Debian 11)
  - Installed packages:
    - git
    - vim
    - curl
    - wget
    - [HTTPie](https://httpie.io/)
    - jq
    - [microsoft/sbom-tool](https://github.com/microsoft/sbom-tool)
    - [anchore/syft](https://github.com/anchore/syft)

### Directory structure

| Path                                        | Desc.                               |
|---------------------------------------------|-------------------------------------|
| /app/log4j-vulnerable-app/gradle.lockfile   | A Gradle lock file                  |
| /app/python-vulnerable-app/requirements.txt | A Pip lock file                     |
| /workspaces/jsac2023-sbom-workshop          | A VS Code workspace                 |
| /workspaces/jsac2023-sbom-workshop/.venv    | A virtualenv path for the workspace |


## How to setup

Please make sure to install the [Remote Development extension pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) before proceeding further.

```bash
git clone https://github.com/ninoseki/jsac2023-sbom-workshop
code jsac2023-sbom-workshop
```

Click the bottom left corner button (Open a Remote Window) of VS Code.

![](https://i.imgur.com/EskbfTT.png)

And select "Reopen in Container".

![](https://i.imgur.com/NYNr49G.png)

It will start a dev container automatically.

See [VS Code: Quick start: Open an existing folder in a container](https://code.visualstudio.com/docs/devcontainers/containers#_quick-start-open-an-existing-folder-in-a-container) for more details.

## How to confirm whether you are ready or not

```bash
# in the host machine
$ docker ps | grep vsc-jsac2023-sbom-workshop-
552de0a989ad   vsc-jsac2023-sbom-workshop-3fca6e376833fdc5e8366e8f0fcde96e   "/bin/sh -c 'echo Co…"   About a minute ago   Up About a minute             admiring_hofstadter
```

```bash
# in the dev container

# check poetry is installed
$ poetry --version
Poetry (version 1.2.2)

# check pytest
$ pytest --version
pytest 7.2.0

# check Python app is running
$ curl localhost:8000
{"message":"hello, world!"}

# check Java app is running
$ curl localhost:8080
{"timestamp":"2022-11-12T07:10:56.045+00:00","status":400,"error":"Bad Request","path":"/"}
```

Note that Python requirements for the hands-on challenges are installed in the virtual environment via Poetry. It is activated by default.

```bash
$ python ...
$ pytest ...
# or
$ deactivate
$ poetry run python ...
$ poetry run pytest
```

