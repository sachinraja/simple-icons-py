import xml.etree.ElementTree as ET

ET.register_namespace("", "http://www.w3.org/2000/svg")

def get_str(icon_name: str) -> str:
    """Read an icon's svg file.

    Args:
        icon_name (str): The name of an icon.

    Returns:
        str: The unparsed xml in the svg file.
    """

    with open(f"simpleicons/icons/{icon_name.lower()}.svg", "r") as f:
        return f.read()

def get_et(icon_name: str) -> ET:
    """Get an icon's element tree (parsed XML).

    Args:
        icon_name (str): The name of an icon.

    Returns:
        xml.etree.ElementTree: An icon's parsed XML.
    """

    return ET.parse(f"simpleicons/icons/{icon_name.lower()}.svg")

def get_xml(icon_name: str, **attrs) -> ET:
    """Add attributes to an icon's svg element.

    Args:
        icon_name (str): The name of an icon.
        **attrs: The attributes to add to the svg element.
    
    Returns:
        xml.etree.ElementTree: An icon's parsed XML with the attributes.
    """

    tree = get_et(icon_name)
    svg = tree.getroot()
    
    for attrName, attrValue in attrs.items():
        svg.set(attrName, attrValue)
    
    return tree

def get_xml_bytes(icon_name: str, **attrs) -> bytes:
    """Get an icon's bytes.

    Args:
        icon_name (str): The name of an icon.
        **attrs: The attributes to add to the svg element.

    Returns:
        bytes: The byte representation of an icon's element tree.
    """

    return ET.tostring(get_xml(icon_name, **attrs).getroot())
