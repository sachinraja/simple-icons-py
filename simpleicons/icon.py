from typing import TypedDict
import re

class License(TypedDict):
  """License information for each icon."""
  type: str
  url: str

class Icon:
  """An icon with all relevant data."""
  def __init__(self, title: str, slug: str, hex: str, source: str, svg: str, guidelines: str, license: License):
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
