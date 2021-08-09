import json
import re
import shutil
from pathlib import Path

from simpleicons.icon import License
from scripts.utils import get_icon_slug, title_to_slug

simpleicons_vendor_dir = Path("vendor", "simple-icons")
data_file = simpleicons_vendor_dir / "_data" / "simple-icons.json"
index_file = Path("simpleicons", "all.py")
icons_dir = Path("simpleicons", "icons")
simpleicons_source_dir = simpleicons_vendor_dir / "icons"

templates_dir = Path("scripts", "templates")
index_template_file = templates_dir / "all.py"
icon_object_template_file = templates_dir / "icon_object.py"

index_template: str = None
with open(index_template_file, "r") as f:
    index_template = f.read()

icon_object_template: str = None
with open(icon_object_template_file, "r") as f:
    icon_object_template = f.read()


def escape(value: str):
    return re.sub(r"(?<!\\)'", r"\\'", value, flags=re.DOTALL)


def icon_to_key_value(icon):
    slug = icon["slug"]
    return f"'{slug}': {icon_to_object(icon)}"


def license_to_object(license: License):
    if not "url" in license:
        license["url"] = f"https://spdx.org/licenses/{license['type']}"

    return license


def icon_to_object(icon):
    for key, value in icon.items():
        if type(value) == str:
            icon[key] = escape(value)

    icon["guidelines"] = icon["guidelines"] if "guidelines" in icon else None
    if type(icon["guidelines"]) == str:
        icon["guidelines"] = f"'{icon['guidelines']}'"

    icon["license"] = license_to_object(icon["license"]) if "license" in icon else None

    return icon_object_template.format(**icon)


def build():
    # reset build
    if icons_dir.exists() and icons_dir.is_dir():
        shutil.rmtree(icons_dir)

    icons_dir.mkdir()

    data = None

    with open(data_file, "r") as f:
        data = json.load(f)

    icons = []
    for icon in data["icons"]:
        icon["slug"] = get_icon_slug(icon)
        svg_filepath = Path(simpleicons_source_dir, f"{icon['slug']}.svg")

        with open(svg_filepath, "r") as f:
            icon["svg"] = re.sub("/\r?\n/", "", f.read())

        icons.append(icon.copy())

        py_filepath = Path(icons_dir, f"{icon['slug']}.py")
        with open(py_filepath, "w") as f:
            f.write(
                f"from simpleicons.icon import Icon\n{icon['slug']}_icon= {icon_to_object(icon)}"
            )

    raw_init_py = index_template.format(
        icons=str.join(",\n", [icon_to_key_value(icon) for icon in icons])
    )
    with open(index_file, "w") as f:
        f.write(raw_init_py)


if __name__ == "__main__":
    build()
