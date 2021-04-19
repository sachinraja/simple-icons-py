# simpleicons
Use a wide-range of icons derived from the [simple-icons](https://github.com/simple-icons/simple-icons) repo in python. Go to [their website](https://simpleicons.org/) for a full list of icons. The slug version (all lowercase and no spaces with some exceptions) must be used for the `icon_name`. The icons folder that accompanies the package has all the files. The package searches for icons by filename.

## Installation
Install with `pip install simpleicons`. Keep in mind that this is a fairly large package due to all the icons (a couple of megabytes).

## Usage
### General Usage
The API can then be used as follows, where [ICON SLUG] is replaced by a slug:
```py
from simpleicons.all import icons

# Get a specific icon by its slug as:
icons.get('[ICON SLUG]')

# For example:
icon = icons.get('simpleicons')

print(icon.__dict__)

"""
{
    'title': 'Simple Icons',
    'slug': 'simpleicons',
    'hex': '111111',
    'source': 'https://simpleicons.org/',
    'svg': '<svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">...</svg>',
    'path': 'M12 12v-1.5c-2.484 ...',
    'guidelines': 'https://simpleicons.org/styleguide',
    'license': {
        type: '...',
        url: 'https://example.com/'
    }
}
"""
```
NOTE: The `guidelines` entry will be `None` if we do not yet have guidelines data for the icon.

NOTE: The `license` entry will be `None` if we do not yet have license data for the icon.

Alternatively you can import the needed icons individually, where [ICON SLUG] is replaced by a slug:
```py
# Import a specific icon by its slug as:
from simpleicons.icons.[ICON SLUG] import icon

# For example:
from simpleicons.icons.simpleicons import icon

print(icon)
```
NOTE: If the icon's slug is not compatible with python imports (e.g. it has a dash) you must use importlib to import it:
```py
import importlib

importlib.import_module('simpleicons.icons.[ICON SLUG]').icon

# For example:
importlib.import_module('simpleicons.icons.dot-net').icon
```

Lastly, the `icons` object is also enumerable. This is useful if you want to do a computation on every icon:
```py
from simpleicons.all import icons

for (key, icon in icons) {
    # do stuff
}
```

### XML
The XML for each icon can be easily manipulated with either of two functions:

`get_xml(icon_name: str, **attrs) -> ElementTree`

```py
from simpleicons.icon_xml import get_xml

# blue logo (simply adds <svg fill="blue"></svg>)
get_xml("github", fill="blue")
```

`get_xml_bytes(icon_name: str, **attrs) -> bytes`

```py
from simpleicons.icon_xml import get_xml_bytes

get_xml_bytes("github", fill="blue")
```

To simply get the unparsed XML string for each icon, use `get_str(icon_name: str) -> str`:

```py
from simpleicons.icon_xml import get_str

get_str("github")
```

This string representation will allow for quick implementation in web pages, however it cannot be manipulated. Use `get_xml_bytes` for easy web page implementation alongside manipulation.

### Image
Icons can be converted to PIL Images with `icon_to_image(icon_xml: bytes, bg: int=0xffffff, scale: Tuple[int, int]=(1, 1)) -> Image`:

```py
from simpleicons.icon_xml import get_xml_bytes
from simpleicons.image import icon_to_image

xml_bytes = get_xml_bytes("github", fill="blue")

# black background and x5 scale
img = icon_to_image(xml_bytes, bg=0x000000, scale=(5, 5))

# manipulate PIL Image
img.putalpha(32)
img.save("github.png")
```
