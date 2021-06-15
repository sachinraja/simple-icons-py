# yes, this is quite confusing
import importlib

from simpleicons.icons.simpleicons import simpleicons_icon
from simpleicons.icons.dotnet import dotnet_icon


def test_simpleicons():
    assert simpleicons_icon.title == "Simple Icons"


def test_dot_net():
    assert dotnet_icon.title == ".NET"
