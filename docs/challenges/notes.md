# Notes on the hands-on challenges

- `jsac2023/` already has a scaffold to build CycloneDX SBOM
- A challenge is implementing a function incomplete
- An implementation of a challenge is testable by `pytest`
- You will be able to create SBOM by the CLI tool (`jsac2023-cli`) after finishing the challenges
- The CLI tools is built on [Typer](https://typer.tiangolo.com/)

```bash
$ jsac2023-cli python --help

 Usage: jsac2023-cli python [OPTIONS] COMMAND [ARGS]...

╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                       │
╰───────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ────────────────────────────────────────────────────────────────────────────────────────╮
│ requirements    Parse requirements.txt and build CycloneDX SBOM                                   │
│ site-packages   Build CycloneDX SBOM based on site packages used by running Python processes      │
╰───────────────────────────────────────────────────────────────────────────────────────────────────╯

$ jsac2023-cli java --help

 Usage: jsac2023-cli java [OPTIONS] COMMAND [ARGS]...

╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                       │
╰───────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ────────────────────────────────────────────────────────────────────────────────────────╮
│ gradle        Parse gradle.lockfile and build CycloneDX SBOM                                      │
│ jar           Parse JAR file and build CycloneDX SBOM                                             │
╰───────────────────────────────────────────────────────────────────────────────────────────────────╯
```
