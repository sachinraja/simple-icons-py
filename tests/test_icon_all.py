from simpleicons.all import icons


def test_simpleicons():
    assert icons.get("Simple Icons").slug == "simpleicons"
