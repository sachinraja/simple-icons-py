import re
from typing import Tuple, List
from unicodedata import normalize

def title_to_slug(title: str):
  slug = title.lower()

  # before normalize
  slug = sub_replacements_list([
    (r'\+', 'plus', re.DOTALL),
    (r'^\.', 'dot-', re.DOTALL),
    (r'\.$', '-dot'),
    (r'\.', '-dot-', re.DOTALL),
    (r'^&', 'and-'),
    (r'&$', '-and'),
    (r'&', '-and-', re.DOTALL),
    (r'đ', 'd', re.DOTALL),
    (r'ħ', 'h', re.DOTALL),
    (r'ı', 'i', re.DOTALL),
    (r'ĸ', 'k', re.DOTALL),
    (r'ŀ', 'l', re.DOTALL),
    (r'ł', 'l', re.DOTALL),
    (r'ß', 'ss', re.DOTALL),
    (r'ŧ', 't', re.DOTALL),
  ], slug)

  slug = normalize('NFD', slug)

  # after normalize
  slug = sub_replacements_list([
    (r'[\u0300-\u036f]', '', re.DOTALL),
    (r'[^a-z0-9\-]', '', re.DOTALL),
  ], slug)

  return slug

def get_icon_slug(icon):
  if 'slug' in icon:
    return icon['slug']
  
  return title_to_slug(icon['title'])

def sub_replacements_list(replacements: List[Tuple[str, str, re.RegexFlag]], value: str):
  """Calls re.sub on multiple replacements.

  Args:
      replacements (List[Tuple[str, str]]): A list of an old and new pattern for replacement.
      value (str): The string to apply the replacements to.
  """

  new_value = value
  for replacement in replacements:
    extra_values = {}
    if len(replacement) > 2:
      extra_values['flags'] = replacement[2]

    new_value = re.sub(replacement[0], replacement[1], new_value, **extra_values)

  return new_value