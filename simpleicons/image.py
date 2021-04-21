from io import BytesIO
from typing import Tuple

from PIL import Image
from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg


def icon_to_image(
    icon_xml: bytes, bg: int = 0xFFFFFF, scale: Tuple[int, int] = (1, 1)
) -> Image:
    """Convert icon to PIL image.

    Args:
        icon_xml: The XML for an icon as bytes.
        bg: The background color for the image. Defaults to 0xffffff.
        scale: A tuple of the two values for the scale of the image. Defaults to (1, 1).
    """

    drawing = svg2rlg(BytesIO(icon_xml))

    drawing.width *= scale[0]
    drawing.height *= scale[1]
    drawing.scale(*scale)

    img_io = BytesIO()
    renderPM.drawToFile(drawing, img_io, fmt="PNG", bg=bg)
    return Image.open(img_io)
