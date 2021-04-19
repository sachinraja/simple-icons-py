from io import BytesIO
from typing import Tuple

from PIL import Image
from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg

from simpleicons.icon_xml import get_xml_bytes


def icon_to_image(icon_xml: bytes, bg: int=0xffffff, scale: Tuple[int, int]=(1, 1)) -> Image:
    """Convert icon to PIL image.

    Args:
        icon_xml (bytes): The XML for an icon as bytes, typically created from icon_xml.get_xml_bytes.
        bg (int, optional): The background color for the image. Defaults to 0xffffff.
        scale (Tuple[int, int], optional): A tuple of the two values for the scale of the image. Defaults to (1, 1).

    Returns:
        PIL.Image: An Image of the svg.
    """

    drawing = svg2rlg(BytesIO(icon_xml))

    drawing.width *= scale[0]
    drawing.height *= scale[1]
    drawing.scale(*scale)

    img_io = BytesIO()
    renderPM.drawToFile(drawing, img_io, fmt="PNG", bg=bg)
    return Image.open(img_io)
