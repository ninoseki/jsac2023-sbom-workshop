- [I want to install XXX in the dev container](#i-want-to-install-xxx-in-the-dev-container)
- [I want to recreate the dev container](#i-want-to-recreate-the-dev-container)
- [The interpreter is not set in the dev container](#the-interpreter-is-not-set-in-the-dev-container)⏎

## I want to install XXX in the dev container

You can install anything what you want. Note that it will be disappeared if you rebuild the container.

```bash
sudo apt install XXX
```

## I want to recreate the dev container

Open the command pallette by `⇧⌘P` in Mac / `Ctrl+Shift+P` in Windows and select `Dev Containers: Rebuild and Reopen in Container`.

![](https://i.imgur.com/WIHptQy.png)

### References

- [VS Code: Create a Dev Container](https://code.visualstudio.com/docs/devcontainers/create-dev-container)
- [VS Code: Keyboard Shortcuts Reference](https://code.visualstudio.com/docs/getstarted/keybindings#_keyboard-shortcuts-reference)

## The interpreter is not set in the dev container

If the Python interpreter is not configured in the dev container, please set to use `/workspaces/jsac2023-sbom-workshop/.venv/bin/python` (= `python.defaultInterpreterPath`) as the interpreter.

![](https://i.imgur.com/1k5z9xA.png)
