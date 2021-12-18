from simpleicons.all import icons
from simpleicons.icons import si_dotnet


def test_simpleicons():
    assert icons["simpleicons"].title == "Simple Icons"


def test_dot_net():
    assert si_dotnet.title == ".NET"
