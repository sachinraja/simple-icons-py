import json
import os
import subprocess
from pathlib import Path

import requests
import semantic_version
import git

from scripts.build_package import build

current_si_pkg = None
with open(Path("vendor", "simple-icons", "package.json"), "r") as f:
    current_simple_icons_pkg = json.load(f)

current_si_version = semantic_version.Version(current_simple_icons_pkg["version"])

# make request 3 times to hopefully break the cache
new_si_pkg = requests.get("https://registry.npmjs.com/simple-icons").json()

new_si_version_str = new_si_pkg["dist-tags"]["latest"]
new_si_version = semantic_version.Version(new_si_pkg["dist-tags"]["latest"])

# do not attempt to update if major versions do not match
# if current_si_version.major != new_si_version.major:
#    print("Next update is major, exiting.")
#    exit(1)

# version is lower or equal - exit
if new_si_version <= current_si_version:
    print("Already on latest version.")
    exit()

# update submodule
repo = git.Repo(os.getcwd())
si_submodule = repo.submodule("vendor/simple-icons")
si_submodule_repo = si_submodule.module()
si_submodule_repo.remotes.origin.fetch("")

si_submodule_repo.git.checkout(new_si_version_str)
print(f"Checked out branch {new_si_version_str} of simple-icons in submodule.")

subprocess.call(["poetry", "version", new_si_version_str])
print("Bumped package version.")

repo.git.add(si_submodule.path)
repo.git.add(Path("pyproject.toml"))

repo.index.commit(f"chore: update simple-icons to {new_si_version_str}")
print("Commited updates.")


repo.git.push(
    "origin",
    "main",
)
print("Pushed updates to origin.")

# create release after pushing to origin
# reference: https://docs.github.com/en/rest/reference/repos#create-a-release
requests.post(
    "https://api.github.com/repos/sachinraja/simple-icons-py/releases",
    json={
        "tag_name": new_si_version_str,
        "name": new_si_version_str,
        "body": f"Updated to [simple-icons {new_si_version_str}](https://github.com/simple-icons/simple-icons/releases/tag/{new_si_version_str})",
    },
    headers={"Authorization": f"token {os.environ['GITHUB_TOKEN']}"},
)
print(f"Created release {new_si_version_str}.")

# start the build
print("Generating lib...")
build()
print("Finished generating.")

print("Begin package publish steps.")
subprocess.call(["poetry", "build"])
subprocess.call(["poetry", "publish"])
