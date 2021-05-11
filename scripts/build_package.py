import json
import re
import os
import shutil
from pathlib import Path

from simpleicons.icon import License
from scripts.utils import get_icon_slug, title_to_slug

data_file = Path("scripts", "_data", "simple-icons.json")
index_file = Path("simpleicons", "all.py")

simple_icons_dir = Path("simple-icons", "icons")
icons_dir = Path("simpleicons", "icons")

index_template_file = Path("scripts", "templates", "all.py")
icon_object_template_file = Path("scripts", "templates", "icon_object.py")

index_template: str = None
with open(index_template_file, "r") as f:
    index_template = f.read()

icon_object_template: str = None
with open(icon_object_template_file, "r") as f:
    icon_object_template = f.read()

data = None
with open(data_file, "r") as f:
    data = json.load(f)


def escape(value: str):
    return re.sub(r"(?<!\\)'", r"\\'", value, flags=re.DOTALL)


def icon_to_key_value(icon):
    icon_name = escape(icon["title"])
    if not icon["slug"] == title_to_slug(icon["title"]):
        icon_name = icon["slug"]

    return f"'{icon_name}': {icon_to_object(icon)}"


def license_to_object(license: License):
    new_license = license
    if not "url" in new_license:
        new_license["url"] = f"https://spdx.org/licenses/{new_license['type']}"

    return new_license


def icon_to_object(icon):
    for key, value in icon.items():
        if type(value) == str:
            icon[key] = escape(value)

    icon["guidelines"] = icon["guidelines"] if "guidelines" in icon else None
    if type(icon["guidelines"]) == str:
        icon["guidelines"] = f"'{icon['guidelines']}'"

    license = None
    if "license" in icon:
        license = license_to_object(icon["license"])

    icon["license"] = license
    return icon_object_template.format(**icon)


def build():
    shutil.copytree(simple_icons_dir, icons_dir)

    icons = []
    for icon in data["icons"]:
        filename = get_icon_slug(icon)
        svg_filepath = Path(icons_dir, f"{filename}.svg")

        with open(svg_filepath, "r") as f:
            icon["svg"] = re.sub("/\r?\n/", "", f.read())

        icon["slug"] = filename
        icons.append(icon.copy())

        py_filepath = Path(icons_dir, f"{filename}.py")
        with open(py_filepath, "w") as f:
            f.write("from simpleicons.icon import Icon\nicon= " + icon_to_object(icon))

    raw_init_py = index_template.format(
        icons=str.join(",\n", [icon_to_key_value(icon) for icon in icons])
    )
    with open(index_file, "w") as f:
        f.write(raw_init_py)


if __name__ == "__main__":
    build()
