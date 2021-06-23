import json
import os
from re import sub
import subprocess
from pathlib import Path

import requests
import semantic_version
import git

from scripts.build_package import build

current_si_pkg = None
with open(Path("simple-icons", "package.json"), "r") as f:
    current_simple_icons_pkg = json.load(f)

current_si_version = semantic_version.Version(current_simple_icons_pkg["version"])

# new_si_pkg = requests.get("https://api.npms.io/v2/package/simple-icons").json()

new_si_version = semantic_version.Version(
    # new_si_pkg["collected"]["metadata"]["version"]
    "5.3.0"
)

new_si_version_str = str(new_si_version)
print(current_si_version, new_si_version)

# do not attempt to update if major versions do not match
if current_si_version.major != new_si_version.major:
    exit(1)

# version is lower - exit
if new_si_version < current_si_version:
    exit()

# update submodule
repo = git.Repo(os.getcwd())
si_submodule = repo.submodule("simple-icons")
si_submodule.module().git.checkout(new_si_version_str)


repo.git.add(si_submodule.path)
repo.index.commit(f"chore: update simple-icons to {new_si_version_str}")
repo.git.push("origin", "main")

# start the build
build()

subprocess.call(["poetry", "version", new_si_version_str])
subprocess.call(["poetry", "build"])
subprocess.call(["poetry", "publish"])
