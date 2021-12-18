<h1>
  <img src="logo.svg" alt="Logo" width="50" height="50">
  simpleicons
</h1>

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Use a wide-range of icons derived from the [simple-icons](https://github.com/simple-icons/simple-icons) repo in python. Go to [their website](https://simpleicons.org/) for a full list of icons. The slug version must be used for the `icon_name`. The icons folder that accompanies the package has all the files. The package uses the latest verison of [Simple Icons](https://github.com/simple-icons/simple-icons/releases/latest). It does **not** depend on the filesystem.

## Installation

Install with `pip install simpleicons`. Keep in mind that this is a fairly large package due to all the icons.

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
from simpleicons.icons import si_[ICON_SLUG]

# For example:
from simpleicons.icons import si_simpleicons
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

`Icon.get_xml(**attrs) -> ElementTree`

```py
from simpleicons.icons import si_simpleicons

# blue logo, adds the fill attribute: <svg fill="blue"></svg>
si_simpleicons.get_xml(fill="blue")
```

`Icon.get_xml_bytes(**attrs) -> bytes`

```py
from simpleicons.icons import si_simpleicons

si_simpleicons.get_xml_bytes(fill="blue")
```

### Image

In order to use this, you must install the extras: `pip install -e simpleicons[imaging]` . Icons can be converted to PIL Images with `icon_to_image(icon_xml: bytes, bg: int=0xffffff, scale: Tuple[int, int]=(1, 1)) -> Image`:

```py
from simpleicons.icons import si_simpleicons
from simpleicons.image import icon_to_image

xml_bytes = si_simpleicons.get_xml_bytes(fill="blue")

# black background and 5x scale
img = icon_to_image(xml_bytes, bg=0x000000, scale=(5, 5))

# manipulate PIL Image
img.putalpha(32)
img.save("simpleicons_blue.png")
```
