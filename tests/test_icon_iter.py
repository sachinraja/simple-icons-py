from simpleicons.all import icons

def test_icon_iter():
  for key, icon in icons.items():
    assert key == icon.title or key == icon.slug
