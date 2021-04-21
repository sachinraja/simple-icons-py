from typing import TypedDict
import re
from xml.etree import ElementTree as ET

ET.register_namespace("", "http://www.w3.org/2000/svg")


class License(TypedDict):
    """License information for each icon."""

    type: str
    url: str


class Icon:
    """An icon with all relevant data and methods."""

    def __init__(
        self,
        title: str,
        slug: str,
        hex: str,
        source: str,
        svg: str,
        guidelines: str,
        license: License,
    ):
        self.title = title
        self.slug = slug
        self.hex = hex
        self.source = source
        self.svg = svg
        self.guidelines = guidelines
        self.license = license

    @property
    def path(self):
        return re.findall(r'<path\s+d="([^"]*)', self.svg)[0]

    def get_element(self):
        """Get svg's element (parsed XML)."""

        return ET.fromstring(self.svg)

    def get_xml(self, **attrs):
        """Add attributes to the svg element.

        Args:
            **attrs: The attributes to add to the svg element.
        """

        svg = self.get_element()
        for attrName, attrValue in attrs.items():
            svg.set(attrName, attrValue)

        return svg

    def get_xml_bytes(self, **attrs):
        """Get the bytes for the svg's element tree."""

        return ET.tostring(self.get_xml(**attrs))
