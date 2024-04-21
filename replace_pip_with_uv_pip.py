import subprocess
import sys


def pip():
    return subprocess.call(
        [sys.executable, "-m", "uv", "pip"] + sys.argv[1:], close_fds=False
    )
