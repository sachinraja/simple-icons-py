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
    print("Next update is major, exiting.")
    exit(1)

# version is lower - exit
if new_si_version < current_si_version:
    print("Already on latest version.")
    exit()

# update submodule
repo = git.Repo(os.getcwd())
si_submodule = repo.submodule("simple-icons")
si_submodule.module().git.checkout(new_si_version_str)
print(f"Checked out branch {new_si_version_str} of simple-icons in submodule.")

subprocess.call(["poetry", "version", new_si_version_str])
print("Bumped package version.")

repo.git.add(si_submodule.path)
repo.git.add(Path("pyproject.toml"))

repo.index.commit(f"chore: update simple-icons to {new_si_version_str}")
print("Commited updates.")

repo.git.push("origin", "main")
print("Pushed updates to origin.")


# start the build
print("Generating lib...")
build()
print("Finished generating.")

print("Begin package publish steps.")
subprocess.call(["poetry", "build"])
subprocess.call(["poetry", "publish"])
