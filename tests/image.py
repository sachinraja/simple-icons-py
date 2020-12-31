from simpleicons.icon_xml import get_xml_bytes
from simpleicons.image import icon_to_image

def download_github_image():
    xml_bytes = get_xml_bytes("gItHub", fill="blue")

    # black background and x5 scale
    img = icon_to_image(xml_bytes, bg=0x000000, scale=(5, 5))

    # manipulate PIL Image
    img.putalpha(32)
    img.save("github.png")

download_github_image()