import os

import psutil
import pyparsing as pp
import sh

python_version_prefix = pp.Keyword("Python") + pp.White(exact=1)
number_after_dot = pp.Word(pp.nums) + pp.Optional(pp.Literal("."))
python_version_suffix = pp.OneOrMore(number_after_dot)
python_version = (
    pp.LineStart() + python_version_prefix + python_version_suffix + pp.LineEnd()
)


def get_command(path: str) -> sh.Command:
    return sh.Command(path)


def am_i_root() -> bool:
    id = get_command("id")
    try:
        output = id("-u")
        return int(str(output).strip()) == 0
    except Exception:
        return False


def is_python(exe: str) -> bool:
    if not os.path.isfile(exe):
        return False

    name = exe.split("/")[-1]
    if not name.startswith("python"):
        return False

    python = get_command(exe)
    try:
        output = python("--version")
        return python_version.matches(str(output).strip())
    except Exception:
        return False


def get_python_in_cmdline(cmdline: list[str]) -> str | None:
    if len(cmdline) == 0:
        return None

    first = cmdline[0]
    if is_python(first):
        return first

    return None


def is_python_process(process: psutil.Process) -> bool:
    try:
        return is_python(process.exe())
    except Exception:
        return False


def get_process(pid: int) -> psutil.Process | None:
    try:
        return psutil.Process(pid)
    except Exception:
        pass

    return None


def get_processes() -> list[psutil.Process]:
    pids = psutil.pids()
    processes = [get_process(pid) for pid in pids]
    return [p for p in processes if p is not None]


def get_py_processes() -> list[psutil.Process]:
    processes = get_processes()
    return [p for p in processes if is_python_process(p)]
