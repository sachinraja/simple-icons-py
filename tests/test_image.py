from pathlib import Path

from simpleicons.icons.simpleicons import simpleicons_icon
from simpleicons.image import icon_to_image


def test_save_github_image():
    xml_bytes = simpleicons_icon.get_xml_bytes(fill="blue")

    # black background and x5 scale
    img = icon_to_image(xml_bytes, bg=0x000000, scale=(5, 5))

    # manipulate PIL Image - very transparent
    img.putalpha(32)
    img.save(Path("tests", "simpleicons_blue.png"))
