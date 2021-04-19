# yes, this is quite confusing
import importlib

from simpleicons.icon import Icon
from simpleicons.icons.simpleicons import icon as simple_icon

# cannot import with "-" in filename
dot_net: Icon = importlib.import_module("simpleicons.icons.dot-net").icon


def test_simpleicons():
    assert simple_icon.title == "Simple Icons"


def test_dot_net():
    assert dot_net.title == ".NET"
