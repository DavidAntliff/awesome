"""Test the awesome package."""


def test_version_is_string():
    import awesome
    assert isinstance(awesome.__version__, str)
